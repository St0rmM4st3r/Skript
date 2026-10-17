# Configuration and integration notes

This repository has **no universal config file**. Most scripts contain inline `options:`, server-specific commands, or persistent Skript variables.

## Before loading a file

1. Search for URLs like `https://yoursite.com`, `YOUR-DISCORD-LINK`, and references to `server_name`.
2. Review commands executed as console (for example `/mvtp`, `/crate`, or `/sudo`) and verify the command exists on your server.
3. Check custom worlds such as `parkourmaps` or `parkourlobby`; change them to your own world setup.
4. Inspect permission nodes for each command. A command declared `executable by: console` must never be exposed to arbitrary players through another command.
5. Review economic units and custom variables: points, tickets, jewels, purchases, and balances are **not** guaranteed to be compatible.
6. Back up all Skript variables before experimenting. Some scripts change persistent game/player state and include reset commands.
7. Confirm command conflicts: multiple scripts or installed plugins may implement the same command name.

## Known external references

| Script | Reference | Context |
| --- | --- | --- |
| `Misc/admingui.sk` | SkBee | Listed in the script header; actual feature compatibility unverified |
| `Misc/deathban.sk` | SkQuery, skRayFall | Explicitly listed in comments; verify real need on your version |
| `Misc/afkpool.sk` | SkQuery, WorldGuard | Custom region and reward logic |
| `Parkour/parkour.sk` | Custom teleports, economy, worlds | Requires your own network configuration and testing |
| `Parkour/checkpoints.sk` | Custom economy, placeholder web URL | Paid checkpoint routines require review |
| `Misc/pets.g.sk` | Custom purchase permissions and server commands | Historical cosmetics example |
| `Misc/perks.g.sk` | GUI/command integrations | Some target subcommands are not provided here |

Other scripts may need addons even when not explicitly declared in their source.

## Security-sensitive workflows

- **Moderation:** `punishmentsystem.sk` and `deathban.sk` can affect player access and require extra review.
- **Economy:** `purchase.sk`, `checkpoints.sk`, and `moneyonkill.sk` use persistent state or balances.
- **Console commands:** treat any string interpolated into privileged console commands as untrusted until validated.
- **Legacy GUIs:** script-era inventory formatting may no longer function on current Skript versions.

If you discover a reproducible bug, use the [issue template](../.github/ISSUE_TEMPLATE/bug_report.md). Avoid posting live tokens, database credentials, private player information, or exploitable vulnerabilities in public issues.
