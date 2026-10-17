"""Unit tests for the repository metadata checker (not the Skript scripts)."""

import json
import tempfile
import unittest
from pathlib import Path

from tools.verify_catalog import validate_repository


class CatalogValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.root = Path(self.temp_dir.name)
        (self.root / "Misc").mkdir()
        (self.root / "Parkour").mkdir()
        (self.root / "docs").mkdir()
        (self.root / "Misc" / "example.sk").write_text(
            "command /example:\n    trigger:\n        send \"ok\"\n", encoding="utf-8"
        )
        self.item = {
            "path": "Misc/example.sk",
            "title": "Example",
            "category": "Administration",
            "summary": "A test script.",
            "dependencies": [],
            "status": "legacy-example",
        }
        self.write_catalog([self.item])
        (self.root / "docs" / "SCRIPTS.md").write_text(
            "[example](../Misc/example.sk)", encoding="utf-8"
        )

    def write_catalog(self, entries):
        (self.root / "catalog.json").write_text(
            json.dumps({"schema_version": 1, "scripts": entries}),
            encoding="utf-8",
        )

    def test_valid_catalog(self):
        self.assertEqual(validate_repository(self.root), [])

    def test_duplicate_path_is_detected(self):
        self.write_catalog([self.item, self.item])
        self.assertTrue(any("Duplicate catalog path" in x
                            for x in validate_repository(self.root)))

    def test_unlisted_script_is_detected(self):
        (self.root / "Parkour" / "new.sk").write_text("", encoding="utf-8")
        self.assertTrue(any("Script missing from catalog" in x
                            for x in validate_repository(self.root)))

    def test_missing_script_is_detected(self):
        (self.root / "Misc" / "example.sk").unlink()
        self.assertTrue(any("Missing script" in x
                            for x in validate_repository(self.root)))

    def test_path_traversal_is_rejected(self):
        self.write_catalog([{**self.item, "path": "../secret.sk"}])
        self.assertTrue(any("Invalid script path" in x
                            for x in validate_repository(self.root)))

    def test_broken_docs_link_is_detected(self):
        (self.root / "docs" / "SCRIPTS.md").write_text("empty", encoding="utf-8")
        self.assertTrue(any("not linked" in x
                            for x in validate_repository(self.root)))


if __name__ == "__main__":
    unittest.main()
