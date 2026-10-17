# Contributing

Thanks for helping improve these Minecraft Skript examples. This collection is currently historical reference material, so contributions that document or fix reproducible issues are especially valuable.

## Good first contributions

- Verify one script against a specified Minecraft, Skript, and addon version.
- Replace hardcoded names, worlds, and URLs with documented configuration options.
- Investigate a reproducible syntax or permission error.
- Expand safe install instructions without claiming untested compatibility.
- Improve documentation or catalog descriptions based on the source.

## Before making changes

1. Search existing issues and pull requests to avoid duplicate work.
2. For code changes, describe the **specific observable problem** and versions affected.
3. Work on a focused branch. Avoid unrelated refactors or reformatting in the same change.
4. Do **not** include credentials, server backups, purchased plugin binaries, or player data.
5. If editing `.sk` files, test on a disposable server with a matching plugin/addon stack.
6. Update `catalog.json` and `docs/SCRIPTS.md` when adding, renaming, or removing a script.

## Checks

These Python checks require no third-party packages:

```bash
python tools/verify_catalog.py
python -m unittest discover -s tests -v
```

They confirm repository inventory consistency only; they **do not parse Skript syntax or simulate Minecraft behavior**.

## Pull request details

Please include:

- What changed and why
- Before/after behavior and reproduction steps
- Minecraft, server software, Skript, and addon versions
- Screenshots or sanitized logs when relevant
- Manual test results and any known limitations
- Whether the change affects permissions, purchases, currencies, or console commands

A change should not be described as production-ready until it has appropriate real runtime test evidence.

## Authorship and license

Please contribute only material you own or are authorized to share. The current repository does **not** publish an open-source reuse license, so contributions or licensing terms should be discussed with the maintainer before external redistribution.
