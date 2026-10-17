# Getting started safely

These files are historical Skript examples rather than version-pinned, independently tested releases.

## Prerequisites

- A **disposable** Minecraft Java test server. Use Paper or Bukkit-compatible server software appropriate for your target Skript version.
- A supported Skript plugin matching that server version: [SkriptLang/Skript](https://github.com/SkriptLang/Skript).
- Optional addons only where the chosen script needs them. Examples identified in comments include [SkBee](https://github.com/ShaneBeee/SkBee), [SkQuery](https://github.com/SkQuery/SkQuery), [skRayFall](https://dev.bukkit.org/projects/skrayfall), and WorldGuard.
- Console access for syntax errors and permission testing, plus a world backup.

No specific server/Skript version combination is currently certified.

## Install one example

1. Read the [script catalog](SCRIPTS.md) and choose an appropriate file.
2. Read the entire script before installing: look for `options:`, custom worlds, variables, external commands, and permissions.
3. Copy the file into the **test server's** `plugins/Skript/scripts/` folder. Retain a backup of the original.
4. Start the server or execute `/sk reload <filename>` through the console. Use the actual script filename without angle brackets.
5. Read console output. If Skript reports unknown syntax, missing addons, or conflicts, **stop** and investigate rather than loading unrelated addons indiscriminately.
6. Try commands with a regular player and an admin separately. Confirm they cannot bypass permissions.
7. Restore your test state and only consider production use after repeatable tests.

## Common problems

**Unknown expression or effect:** The script may require an addon or use syntax removed in your installed version. Compare its comments and the addon documentation.

**Command collision:** `/ban`, `/broadcast`, `/admin`, and other examples may conflict with installed plugins. Test one at a time.

**World or teleport errors:** The parkour examples use custom world names, teleports, and game modes. They are not a standalone minigame installer.

**Economy / permissions not working:** Some scripts expect other plugins, custom variables, and server-specific permission nodes.

**Placeholder links and server names:** Replace example URLs and names before showing the interface to players.

## Runtime test record

When you test a script, note:

```text
Script:
Minecraft server software/build:
Skript version:
Addons and versions:
Worlds/plugins involved:
Steps to reproduce:
Expected outcome:
Actual outcome and console errors:
```

For help contributing tested compatibility data, see [CONTRIBUTING.md](../CONTRIBUTING.md).
