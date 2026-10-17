# Project status and roadmap

## Current status

The public repository contains **19 historical script files** in `Parkour/` and `Misc/`.

| Area | Status |
| --- | --- |
| Code inventory and descriptions | Documented |
| Contributor and security instructions | Documented |
| Catalog consistency checks | Automated static checks |
| Modern Minecraft/Skript compatibility | **Not verified** |
| In-game behavior and performance | **Not verified** |
| External adoption / monthly downloads | **Not measured** |
| Reuse / distribution license | **Pending owner confirmation** |

There are no published releases or verified compatibility claims.

## Improvement priorities

1. **Confirm licensing and file provenance:** review each script's authorship and choose an appropriate license only for owned or properly licensed content.
2. **Create a version matrix:** test representative scripts against chosen Paper + Skript + addon versions and record evidence.
3. **Isolate and modernize scripts:** remove hardcoded server details, validate permissions, and address incompatibilities.
4. **Test risky behavior first:** moderation, economy, console execution, and player-state mutation should have repeatable test cases.
5. **Create tagged releases when ready:** include versions, known limitations, and upgrade notes.

## Reporting progress

An open issue, proposed pull request, or a passing catalog check **is not proof of runtime compatibility**. When an improvement is tested, include the exact versions and reproducible evidence in the PR.

Want to help? Follow [CONTRIBUTING.md](../CONTRIBUTING.md).
