# IMPORTANT! The mod will NOT work otherwise!

## Setup Instructions
- **Upload Key**: To use this mod, you'll need an upload key to the Slay the Jokers server.
1. Acquire an `upload.key` file using **one** of the following methods:
    - Email me at `itsedalo@gmail.com`
        - Absolutely no need for anything formal or polite, you can just say `Hi, I'm <twitch name>, give me a key.`, word for word if you want. I'll try to send you the key quickly.
    - Use the automated system at https://edalo.net/stj/get-key (you will need to verify your Twitch account to prove it's really you)
        - This feature is new; if something fails, fall back to emailing me
2. Place `upload.key` in the mod folder (Usually `%appdata%\Balatro\Mods\slay-the-jokers-main` or similar)
3.  Enable the [extension](https://dashboard.twitch.tv/extensions/iaofk5k6d87u31z9uy2joje2fwn347) on your Twitch channel

## Things to Know Before Installing
- **Stream Overlays**: This mod currently only works correctly if the game is shown at a 16:9 resolution (like 1920x1080 / 4K / 8K) and **fills the entire visible area of the stream**. Overlays that crop or reposition the game may cause card positions to misalign.
    - If that's a dealbreaker, feel free to contact me - I might be able to make it work for your setup.

- **Other Mods & Compatibility**: This mod should be compatible with most other mods.
    - Compatible mods:
        - Reskins, QoL mods, and other non-card-related mods should work in their entirety, but have not been tested (except for the [Handy](https://github.com/SleepyG11/HandyBalatro) mod, which was confirmed to work).
        -  Mods that add new cards should generally work, aside from some potential minor formatting quirks. Among mods that were confirmed to work are [Extra Credit](https://github.com/GuilloryCraft/ExtraCredit), [Paperback](https://github.com/Balatro-Paperback/paperback), [Neato](https://github.com/neatoqueen/NeatoJokers), [Cryptid](https://github.com/MathIsFun0/Cryptid), and [The Balatro Multiplayer Mod](https://github.com/V-rtualized/BalatroMultiplayer).
    - Incompatible mods:
        - Mods that modify existing card effects are **not** compatible (the original card's effect will be shown instead).

- **Disclaimer**: This mod is still under development, so some features might not work perfectly. If you encounter any issues, please let me know!
    - *More formal disclaimer for meanies: this project is a hobby project, provided as-is, with no guarantees of stability, correctness, or suitability for any purpose. You're welcome to use it - but I take no responsibility if something goes wrong.*

---

If anything is unclear or you run into issues, try referring to the [full installation guide](../INSTALL.md). 

## Known Issues and Missing Features

### Effects and Formatting
- Level text on Planet cards lacks color
- Floating and waving text effects do not work

## UI Elements
- Tags and Boss Blinds are not hoverable

## Mods
- Some Cryptid card titles are not shown correctly

## Codebase
- `uvx` re-installs libraries after the game has not been opened for a while