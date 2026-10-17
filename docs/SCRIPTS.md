# Script catalog

This is the human-readable index for [catalog.json](../catalog.json). All entries are **legacy examples**; none has an independently verified modern runtime compatibility result.

The dependencies listed here are **known references, not complete dependency audits**.

| File | Purpose | Explicitly identified dependencies |
| --- | --- | --- |
| [`Misc/admingui.sk`](../Misc/admingui.sk) | Experimental inventory interface; depends on SkBee syntax. | SkBee |
| [`Misc/afkpool.sk`](../Misc/afkpool.sk) | Region-based AFK reward loop with server-specific currency variables. | SkQuery, WorldGuard |
| [`Misc/deathban.sk`](../Misc/deathban.sk) | Tracks deaths and bans after a threshold; dangerous to enable unchanged. | SkQuery, skRayFall |
| [`Misc/discord.sk`](../Misc/discord.sk) | Options snippet containing an unconfigured Discord invite placeholder. | Not specified; inspect source |
| [`Misc/hats.g.sk`](../Misc/hats.g.sk) | Legacy GUI-backed hat menu with custom permission and purchase hooks. | Not specified; inspect source |
| [`Misc/koth.sk`](../Misc/koth.sk) | Timed hill capture concept with hardcoded broadcast and reward commands. | Not specified; inspect source |
| [`Misc/moneyonkill.sk`](../Misc/moneyonkill.sk) | Kill-point bookkeeping and an unfinished shop GUI template. | Not specified; inspect source |
| [`Misc/perks.g.sk`](../Misc/perks.g.sk) | Legacy perks GUI integrating other commands and server-specific worlds. | Not specified; inspect source |
| [`Misc/pets.g.sk`](../Misc/pets.g.sk) | Legacy pet selection and management routines with custom entitlements. | Not specified; inspect source |
| [`Misc/punishmentsystem.sk`](../Misc/punishmentsystem.sk) | Ban, mute, kick, and warning routines; security-sensitive, not verified. | Not specified; inspect source |
| [`Misc/purchase.sk`](../Misc/purchase.sk) | Legacy purchase variables and player-identity migration examples. | Not specified; inspect source |
| [`Misc/rulesgui.sk`](../Misc/rulesgui.sk) | Inventory-based rules navigation with server-specific content. | Not specified; inspect source |
| [`Misc/staffchat.sk`](../Misc/staffchat.sk) | Toggleable staff-only messaging example with chat event handling. | Not specified; inspect source |
| [`Parkour/checkpoints.sk`](../Parkour/checkpoints.sk) | Checkpoint commands and variables with economy integration. | Not specified; inspect source |
| [`Parkour/parkour.sk`](../Parkour/parkour.sk) | Course tracking, teleportation, and progress scripting for a custom map setup. | Not specified; inspect source |
| [`Parkour/parkoursigns.sk`](../Parkour/parkoursigns.sk) | Sign-based course counters and scheduled display refresh. | Not specified; inspect source |
| [`Parkour/parkourspawn.sk`](../Parkour/parkourspawn.sk) | Per-course spawn points, teleport commands, and player counters. | Not specified; inspect source |
| [`Parkour/parkourstats.sk`](../Parkour/parkourstats.sk) | Statistics signboards and periodic refresh routines. | Not specified; inspect source |
| [`Parkour/timer.sk`](../Parkour/timer.sk) | Timed runs and sign-based leaderboards with extensive custom variables. | Not specified; inspect source |

## What is safe to try first?

For learning, inspect a small utility such as [staff chat](../Misc/staffchat.sk) or [parkour spawns](../Parkour/parkourspawn.sk) **without enabling it**. Check permissions, command conflicts, and version-specific syntax before loading it.

## High-risk / incomplete examples

- [Punishment system](../Misc/punishmentsystem.sk) registers commands that can affect player access. Review permission, console, and state handling.
- [Death-based ban](../Misc/deathban.sk) can ban players; use only in a disposable test environment.
- [Kill-point shop](../Misc/moneyonkill.sk) contains unfinished shop actions/placeholders.
- [Parkour courses](../Parkour/parkour.sk), [timer](../Parkour/timer.sk), and [checkpoints](../Parkour/checkpoints.sk) assume linked commands, custom world setup, currency variables, and other state.
- [Discord options](../Misc/discord.sk) is a configuration snippet, not a complete Discord integration.

See [Getting started](GETTING_STARTED.md) and [Configuration](CONFIGURATION.md) for a setup checklist.
