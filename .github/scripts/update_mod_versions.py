#!/usr/bin/env python3

import json
import os
import re
import requests
import sys
import time
from datetime import datetime
from pathlib import Path

# GitHub API rate limits are higher with authentication
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
HEADERS = {'Authorization': f'token {GITHUB_TOKEN}'} if GITHUB_TOKEN else {}

def extract_repo_info(repo_url):
    """Extract owner and repo name from GitHub repo URL."""
    match = re.search(r'github\.com/([^/]+)/([^/]+)', repo_url)
    if match:
        owner = match.group(1)
        repo = match.group(2)
        # Remove .git suffix if present
        repo = repo.removesuffix('.git')
        return owner, repo
    return None, None

def get_version_string(source, owner, repo, start_timestamp, n = 1):
    """Get the version string from a given GitHub repo."""
    
    if source == 'release':
        url = f'https://api.github.com/repos/{owner}/{repo}/releases/latest'
    else:
        url = f'https://api.github.com/repos/{owner}/{repo}/commits'

    try:
        response = requests.get(url, headers=HEADERS)
        
        api_rate_limit = int(response.headers.get('x-ratelimit-limit'))
        api_rate_usage = int(response.headers.get('x-ratelimit-used'))
        api_rate_remaining = int(response.headers.get('x-ratelimit-remaining'))
        api_reset_timestamp = int(response.headers.get('x-ratelimit-reset'))
        api_resource = response.headers.get('x-ratelimit-resource')
        print(f"GitHub API ({api_resource}) calls: {api_rate_usage}/{api_rate_limit}")

        if response.status_code == 200:
            if source == 'release':
                data = response.json()
                # Return name of latest tag
                return data.get('tag_name')
            else:
                commits = response.json()
                if commits and len(commits) > 0:
                    # Return shortened commit hash (first 7 characters)
                    return commits[0]['sha'][:7]
        elif response.status_code == 404:
            # Not found
            return None
        elif api_rate_remaining == 0 or (response.status_code == 403 and 'rate limit exceeded' in response.text.lower()):
            print(f"GitHub API access is being rate limited!")
            current_timestamp = int(time.time())
            
            # Check if primary rate limit is okay
            if api_rate_remaining > 0:
                # Secondary rate limit hit, follow GitHub instructions
                if 'retry-after' in response.headers:
                    wait_time = int(response.headers.get('retry-after')) + 5
                    print(f"Response retry-after {wait_time}s")
                else:
                    # Start at 60 seconds and double wait time with each new attempt
                    print(f"Attempt {n}")
                    wait_time = 60 * pow(2, n - 1)
            else:
                api_reset_time = datetime.fromtimestamp(api_reset_timestamp).strftime('%H:%M:%S')
                print(f"GitHub API rate limit resets at {api_reset_time}")
                wait_time = api_reset_timestamp - current_timestamp + 5

            # Wait only if the wait time would finish less than 1800 seconds (30 min) after program start time
            if current_timestamp + wait_time - start_timestamp < 1800:
                print(f"Waiting {wait_time} seconds until next attempt...")
                time.sleep(wait_time)
                n += 1
                return get_version_string(source, owner, repo, start_timestamp, n)  # Retry
            else:
                print(f"Next attempt in {wait_time} seconds, but Action run time would exceed 1800 seconds - Stopping...")
                sys.exit(1)

        else:
            print(f"Error fetching {source}s: HTTP {response.status_code} - {response.text}")
            return None
    except Exception as e:
        print(f"Exception while fetching {source}s: {str(e)}")
        return None

def process_mods(start_timestamp):
    """Process all mods and update versions where needed."""
    mods_dir = Path('mods')
    updated_mods = []
    
    print(f"Scanning {mods_dir} for mods with automatic version control...")
    
    # Find all mod directories
    for mod_dir in [d for d in mods_dir.iterdir() if d.is_dir()]:
        meta_file = mod_dir / 'meta.json'
        
        if not meta_file.exists():
            continue
            
        try:
            with open(meta_file, 'r', encoding='utf-8') as f:
                meta = json.load(f)
                
            # Skip mods without automatic version checking enabled
            if not meta.get('automatic-version-check', False):
                continue
                
            print(f"Processing {mod_dir.name}...")
            
            repo_url = meta.get('repo')
            if not repo_url:
                print(f"⚠️ Warning: Mod {mod_dir.name} has automatic-version-check but no repo URL")
                continue
                
            owner, repo = extract_repo_info(repo_url)
            if not owner or not repo:
                print(f"⚠️ Warning: Could not extract repo info from {repo_url}")
                continue
                
            print(f"Checking GitHub repo: {owner}/{repo}")
                
            # If download url links to latest head, use version of latest commit hash
            download_url = meta.get('downloadURL')
            if "/archive/refs/heads/" in download_url:
                print("Download URL links to HEAD, checking latest commit...")
                version_source = "commit"
                new_version = get_version_string(version_source, owner, repo, start_timestamp)
            else:
                # Try to get latest release version
                print("Checking releases for latest version tag...")
                version_source = "release"
                new_version = get_version_string(version_source, owner, repo, start_timestamp)
                
                # If no releases, fall back to latest commit
                if not new_version:
                    print("No releases found, checking latest commit...")
                    version_source = "commit"
                    new_version = get_version_string(version_source, owner, repo, start_timestamp)

            if not new_version:
                print(f"⚠️ Warning: Could not determine version for {mod_dir.name}")
                continue
                
            current_version = meta.get('version')
            
            # Update version if it changed
            if current_version != new_version:
                print(f"✅ Updating {mod_dir.name} from {current_version or 'none'} to {new_version} ({version_source})")
                meta['version'] = new_version
                
                with open(meta_file, 'w', encoding='utf-8') as f:
                    # Preserve formatting with indentation
                    json.dump(meta, f, indent=2, ensure_ascii=False)
                    f.write("\n")  # Add newline at end of file
                    
                updated_mods.append({
                    'name': meta.get('title', mod_dir.name),
                    'old_version': current_version,
                    'new_version': new_version,
                    'source': version_source
                })
            else:
                print(f"ℹ️ No version change for {mod_dir.name} (current: {current_version})")
                
        except Exception as e:
            print(f"❌ Error processing {mod_dir.name}: {str(e)}")
            
    return updated_mods

def generate_commit_message(updated_mods):
    """Generate a detailed commit message listing all updated mods."""
    if not updated_mods:
        return "No mod versions updated"
        
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    message = f"Auto-update mod versions ({timestamp})\n\n"
    message += "Updated mods:\n"
    
    for mod in updated_mods:
        old_ver = mod['old_version'] or 'none'
        message += f"- {mod['name']}: {old_ver} → {mod['new_version']} ({mod['source']})\n"
        
    return message

if __name__ == "__main__":
    start_timestamp = int(time.time())
    start_datetime = datetime.fromtimestamp(start_timestamp).strftime('%H:%M:%S')
    print(f"🔄 Starting automatic mod version update at {start_datetime}...")
    updated_mods = process_mods(start_timestamp)
    
    if updated_mods:
        # Write commit message to a file that the GitHub Action can use
        commit_message = generate_commit_message(updated_mods)
        with open('commit_message.txt', 'w', encoding='utf-8') as f:
            f.write(commit_message)
        
        print(f"✅ Completed. Updated {len(updated_mods)} mod versions.")
    else:
        print("ℹ️ Completed. No mod versions needed updating.")
    
    # Exit with status code 0 even if no updates were made
    sys.exit(0)

