# ceuy_reader.py
# CEUY Logic Tree Parser from UID, BitPic, and TAT

import yaml
import json
from pathlib import Path
from datetime import datetime

class CEUYReader:
    def __init__(self, base_path):
        self.base_path = Path(base_path)
        self.uid_index = []
        self.manifest = {}
        self.canvas_raw = None

    def load_uid_index(self):
        path = self.base_path / "UID_INDEX.yaml"
        if path.exists():
            with open(path, 'r') as f:
                data = yaml.safe_load(f)
                self.uid_index = data.get("uids", [])
            print("[✓] UID Index loaded:", self.uid_index)
        else:
            print("[!] UID_INDEX.yaml not found")

    def load_manifest(self):
        path = self.base_path / "ceuy_manifest.json"
        if path.exists():
            with open(path, 'r') as f:
                self.manifest = json.load(f)
            print("[✓] Manifest loaded:", self.manifest.get("thread"))
        else:
            print("[!] ceuy_manifest.json not found")

    def load_canvas(self):
        path = self.base_path / "SORA_ENTRY.tat"
        if path.exists():
            self.canvas_raw = path.read_text()
            print("[✓] Canvas file loaded (symbolic memory)")
        else:
            print("[!] SORA_ENTRY.tat not found")

    def parse_all(self):
        print("\n🧠 CEUY_READER: Initializing parse pipeline...")
        self.load_uid_index()
        self.load_manifest()
        self.load_canvas()

    def describe_state(self):
        print("\n=== CEUY CURRENT STATE ===")
        print(f"BitPic UID Chain: {self.uid_index}")
        print(f"Branch: {self.manifest.get('repo_branch')}")
        print(f"Last Sync: {self.manifest.get('last_action')}")
        print("\nCanvas Fragment:\n----------------")
        print(self.canvas_raw[:300] + '...')

if __name__ == "__main__":
    reader = CEUYReader("./")  # adjust if running from different path
    reader.parse_all()
    reader.describe_state()

