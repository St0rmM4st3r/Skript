# Minecraft Skript collection

**Historical server scripting projects • Minecraft Java Edition • Skript**

A curated collection of **19 Skript scripts** spanning parkour gameplay, server administration, cosmetics, and community utilities. This repository makes earlier scripting work publicly inspectable and provides examples to study, adapt, and improve.

> [!IMPORTANT]
> **Reference material, not a verified plugin distribution.** Many scripts were written for specific server configurations, earlier Minecraft/Skript versions, or third-party addons. They have **not** been retested for current Paper/Skript releases. Review them individually and test on a disposable server before use.

## Explore the code

| Area | What you'll find |
| --- | --- |
| [Parkour](Parkour/) | Courses, checkpoints, spawn management, timers, statistics, and signs |
| [Misc](Misc/) | AFK rewards, GUI ideas, staff chat, moderation, cosmetics, and more |
| [Complete script catalog](docs/SCRIPTS.md) | File-by-file descriptions and known dependencies |
| [Getting started](docs/GETTING_STARTED.md) | Safe setup steps and a minimal local testing workflow |
| [Configuration notes](docs/CONFIGURATION.md) | Variables, placeholders, addon needs, and operational cautions |
| [Project status](docs/PROJECT_STATUS.md) | What's verified, what's legacy, and how to help |

## Quick start

1. Create a **test** Paper or compatible Bukkit server; install a Skript build compatible with that server version.
2. Select **one** file from [the catalog](docs/SCRIPTS.md) and review its code and dependencies.
3. Place it in `plugins/Skript/scripts/`, then run `/sk reload <filename>` in the test server.
4. Read console output, check for unknown effects or expressions, and test commands with a non-admin account before production use.

Start with a small utility and **do not load the entire collection at once**. Some scripts register common command names such as `/ban` and `/broadcast`, or rely on shared variables and custom worlds.

## Current limitations

- **No verified version matrix:** there is no claim of current Paper, Folia, or modern Skript compatibility.
- **Addon dependencies vary:** check script comments and [configuration notes](docs/CONFIGURATION.md); the catalog lists only dependencies explicitly identified.
- **Server-specific assumptions:** references to world names, currencies, commands, permissions, GUI implementations, and example URLs must be adapted.
- **Potentially disruptive behavior:** punishment, economy, purchases, and automated rewards must be audited before enabling.
- **Static CI only:** repository checks validate catalog consistency; they **do not** compile, execute, or certify the Skript runtime.

## Development and contributions

Want to help modernize an example or reproduce a bug? Please read [CONTRIBUTING.md](CONTRIBUTING.md). Include your server/Skript versions, relevant addons, logs, and repeatable test instructions.

The machine-readable [catalog.json](catalog.json) is checked by [tools/verify_catalog.py](tools/verify_catalog.py) and [repository CI](.github/workflows/catalog-checks.yml). Run locally:

```bash
python tools/verify_catalog.py
python -m unittest discover -s tests -v
```

These checks only validate repository metadata and inventory.

## Maintainer

GitHub: [@St0rmM4st3r](https://github.com/St0rmM4st3r) · Other development work: [Crystal Developments](https://crystaldevs.xyz)

## Licensing

**No open-source license has been granted for this collection at this time.** Public source visibility alone does not authorize redistribution or modification by third parties. Licensing and provenance must be confirmed before treating these files as an openly licensed project.
