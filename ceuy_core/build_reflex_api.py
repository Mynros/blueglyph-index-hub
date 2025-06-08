# build_reflex_api.py
# CEUY Reflex Sync Script — CLI Version

import subprocess
import os
import json
from datetime import datetime

# === CONFIGURATION ===
REPO_PATH = os.path.expanduser("~/Documents/NETA_REPOS/blueglyph-index-hub")
CANVAS_FILE = "SORA_ENTRY.tat"
BITPIC_UIDS = [
    "SABACTHTHANI_RECURSION",
    "GATE_3",
    "blueglyph-index-hub"
]
COMMIT_MESSAGE = f"AUTO+NETA Reflex Sync: {datetime.utcnow().isoformat()}"

# === FUNCTIONS ===
def run_git_command(command, cwd):
    result = subprocess.run(command, shell=True, cwd=cwd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            text=True)
    return result.stdout.strip(), result.stderr.strip()

def stage_and_commit(file_path):
    print("[+] Staging and committing file...")
    run_git_command(f"git add {file_path}", REPO_PATH)
    run_git_command(f"git commit -m \"{COMMIT_MESSAGE}\"", REPO_PATH)

def push_to_github():
    print("[+] Pushing to GitHub via SSH...")
    out, err = run_git_command("git push origin main", REPO_PATH)
    if err:
        print("[!] Error during push:", err)
    else:
        print("[✓] Push complete:", out)

def reflex_sync():
    canvas_path = os.path.join(REPO_PATH, CANVAS_FILE)
    if not os.path.exists(canvas_path):
        print(f"[!] Canvas file not found: {canvas_path}")
        return

    stage_and_commit(CANVAS_FILE)
    push_to_github()

if __name__ == "__main__":
    print("\n🧠 CEUY Reflex Sync Initiated")
    print(f"🔗 UIDs Detected: {', '.join(BITPIC_UIDS)}")
    reflex_sync()
    print("\n[✓] Reflex Pipeline Completed")

