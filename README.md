# Balatro Mod Index Guide
![Balatro Image](https://github.com/skyline69/balatro-mod-index/blob/main/media/Balatro.jpg?raw=true)
This guide explains how to structure and publish your Balatro mods in the *Balatro Mod Index* repository. Follow the instructions below carefully to ensure your mod is properly added.

## Directory Structure

Your mod should have the following structure inside the `mods/` directory:
- mods/
    - Author@Modname/
        - thumbnail.jpg (optional but preferred)
        - description.md (required)
        - meta.json (required)

### Example
For a mod titled "Pokermon" by "InertSteak":

- mods/
    - InertSteak@Pokermon/
        - thumbnail.jpg
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
  "requires-talisman": false,
  "categories": ["Content"],
  "author": "Joe Mama",
  "repo": "https://github.com/joemama/extended-cards",
  "downloadURL": "https://github.com/joemama/extended-cards/releases/latest/extended-cards.tar.gz",
  "folderName": "ExtendedCards"
}

```
- **title**: The name of your mod.
- **requires-steamodded**: If your mod requires the [Steamodded](https://github.com/Steamodded/smods) mod loader, set this to `true`.
- *requires-talisman*: (*Optional*) If your mod requires the [Talisman](https://github.com/MathIsFun0/Talisman) mod, set this to `true`.
- **categories**: Must contain at least one of `Content`, `Joker`, `Quality of Life`, `Technical`, `Miscellaneous`, `Resource Packs` or `API`.
- **author**: Your chosen username or handle.
- **repo**: A link to your mod's repository.
- **downloadURL**: A direct link to the latest version of your released mod. (Can be same as `repo` if no separate download link exists.)
- *folderName*: (*Optional*) The name for the mod's install folder. This must not contain characters `<` `>` `:` `"` `/` `\` `|` `?` `*`

### 3. thumbnail.jpg (Optional)
If included, this image will appear alongside your mod in the index. Maximum and recommended size is 1920x1080 pixels.

## How to Publish

1. **Fork the Balatro Mod Index Repository**  
   Go to the main Balatro Mod Index repository on GitHub and click **Fork** to create your own copy.

2. **Create a New Mod Directory**  
   Under `mods/`, add a folder named `Author@Modname` (e.g., `InertSteak@Pokermon`).  
   Inside it, include:  
   - `description.md` (**required**)  
   - `meta.json` (**required**)  
   - `thumbnail.jpg` (optional but recommended)

3. **Write Your Mod Description**  
   Use `description.md` to explain what your mod does, key features, and any usage instructions.

4. Populate `meta.json`

5. **Commit and Push**  
Commit your directory and files, then push them to your fork.

6. **Open a Pull Request (PR)**  
From your fork, open a Pull Request to the main repository's default branch (e.g., `main`):  
- **Title**: *"Add Author@Modname mod"*  
- **Description**: Briefly describe your mod's purpose or any extra details.

7. **Automated Checks**  
As soon as you open the PR, GitHub Actions runs the automated checks to ensure your mod meets the required standards. If any checks fail, you will need to address the issues before your PR can be merged.

8. **Manual Review**  
A project maintainer or designated reviewer will review your PR to confirm it meets ethical, technical, and overall quality standards.

9. **Merge**  
Once the automated checks and manual review pass, your PR will be merged. Your mod then becomes part of the **Balatro Mod Index**!

Once your submission is reviewed and approved, your mod will be added to the Balatro Mod Index!

---

Thanks for contributing to the **Balatro Mod Index** and helping the community grow! 
