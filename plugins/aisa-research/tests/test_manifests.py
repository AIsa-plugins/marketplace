import json
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[3]
PLUGIN_ROOT = REPO_ROOT / "plugins" / "aisa-research"


class ManifestTests(unittest.TestCase):
    def load_json(self, path):
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)

    def test_plugin_names_and_versions_match(self):
        codex = self.load_json(PLUGIN_ROOT / ".codex-plugin" / "plugin.json")
        claude = self.load_json(PLUGIN_ROOT / ".claude-plugin" / "plugin.json")
        self.assertEqual(codex["name"], PLUGIN_ROOT.name)
        self.assertEqual(claude["name"], PLUGIN_ROOT.name)
        self.assertEqual(codex["version"].split("+", 1)[0], "0.1.0")
        self.assertEqual(claude["version"], "0.1.0")
        self.assertEqual(codex["skills"], "./skills/")

    def test_marketplaces_point_to_the_same_plugin(self):
        codex = self.load_json(REPO_ROOT / ".agents" / "plugins" / "marketplace.json")
        claude = self.load_json(REPO_ROOT / ".claude-plugin" / "marketplace.json")
        self.assertEqual(codex["name"], "aisa")
        self.assertEqual(claude["name"], "aisa")
        self.assertEqual(codex["plugins"][0]["name"], "aisa-research")
        self.assertEqual(codex["plugins"][0]["source"]["path"], "./plugins/aisa-research")
        self.assertEqual(claude["plugins"][0]["source"], "./plugins/aisa-research")
        self.assertEqual(
            codex["plugins"][0]["policy"],
            {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
        )


if __name__ == "__main__":
    unittest.main()
