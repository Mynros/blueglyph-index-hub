import os
import subprocess
from datetime import datetime

REPO_DIR = os.getenv("GIT_REPO_DIR", ".")
COMMIT_MSG = f"AUTO+NETA reflex push at {datetime.now().isoformat()}"

def git_push():
    os.chdir(REPO_DIR)
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", COMMIT_MSG], check=True)
    subprocess.run(["git", "push"], check=True)

if __name__ == "__main__":
    try:
        git_push()
        print("✅ Push successful.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Git push failed: {e}")
