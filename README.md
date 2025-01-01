# Balatro Mod Index Guide
![Balatro Image](https://github.com/skyline69/balatro-mod-index/blob/main/media/Balatro.jpg?raw=true)
This guide explains how to structure and publish your Balatro mods in the *Balatro Mod Index* repository. Follow the instructions below carefully to ensure your mod is properly added.

## Directory Structure

Your mod should have the following structure inside the `mods/` directory:
- mods/
    - Author@Modname/
        - thumbnail.png (optional but preferred)
        - description.md (required)
        - meta.json (required)

### Example
For a mod titled "Pokermon" by "InertSteak":

- mods/
    - InertSteak@Pokermon/
        - thumbnail.png
        - description.md
        - meta.json

## Required Files

### 1. description.md
A markdown file describing your mod's features, installation steps, and any additional details you wish to share.

### 2. meta.json
This file stores essential metadata in JSON format. **Make sure you adhere to the valid categories and mod-loader options.** Below is an example:
```json
{
  "title": "Extended Cards",
  "requires-steamodded": true,
  "category": "Content",
  "author": "Joe Mama",
  "repo": "https://github.com/joemama/extended-cards",
  "downloadURL": "https://github.com/joemama/extended-cards/releases/latest/extended-cards.tar.gz"
}
```

- **title**: The name of your mod.
- **requires-steamodded**: If your mod requires the Steamodded mod loader, set this to `true`.
- **category**: Must be one of `Content`, `Joker`, `Quality of Life`, `Technical`, `Miscellaneous`, `Resource Packs` or `API`.
- **author**: Your chosen username or handle.
- **repo**: A link to your mod’s repository.
- **downloadURL**: A direct link to the latest version of your released mod. (Can be same as `repo` if no separate download link exists.)

### 3. thumbnail.jpg (Optional)
If included, this image will appear alongside your mod in the index. Maximum and recommended size is 1920 × 500 pixels.

## How to Publish

1. **Clone the Balatro Mod Index Repository**  
   Clone the repository to your local machine and create a new branch for your mod by running:
   ```bash
    git clone https://github.com/skyline69/balatro-mod-index.git
    cd balatro-mod-index
    git checkout -b add-<modname>
   ```
   > Replace `<modname>` with your mod’s name (e.g., `add-pokermon`).

2. **Create a New Mod Directory**  
   Under `mods/`, add a folder named `Author@Modname` (e.g., `InertSteak@Pokermon`).  
   Inside it, include:  
   - `description.md` (**required**)  
   - `meta.json` (**required**)  
   - `thumbnail.png` (optional but recommended)

3. **Write Your Mod Description**  
   Use `description.md` to explain what your mod does, key features, and any usage instructions.

4. Populate `meta.json`

5. **Commit and Push**  
Commit your new folder and files in your fork’s `mods/` directory, then push your changes to GitHub.

6. **Open a Pull Request (PR)**  
Go to the **Balatro Mod Index** repository on GitHub and open a new PR.
- **PR Title**: “Add Author@Modname mod”  
- **Description**: Briefly describe your mod.

7. **Automated Checks**  
As soon as you open the PR, GitHub Actions runs the automated checks to ensure your mod meets the required standards. If any checks fail, you will need to address the issues before your PR can be merged.

8. **Manual Review**  
A project maintainer or designated reviewer will review your PR to confirm it meets ethical, technical, and overall quality standards.

9. **Merge**  
Once the reviewer approves and your automated checks have passed, your mod will be merged into the **Balatro Mod Index**!

Once your submission is reviewed and approved, your mod will be added to the Balatro Mod Index!

---

Thanks for contributing to the **Balatro Mod Index** and helping the community grow! 
