# AUTO+NETA Git Push Module

This module allows you to auto-push UID and reflex logic to GitHub.

## Setup Instructions

1. Clone your GitHub repo locally.

2. Copy `gitbridge_push.py` into the repo directory.

3. Create a `.env` file from `.env.example` and fill in:
   - `GIT_REPO_DIR` — the path to your cloned Git repo
   - `GITHUB_TOKEN` — your GitHub personal access token (classic)

4. Authenticate Git:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git remote set-url origin https://<token>@github.com/your-username/your-repo.git
```

💡 You may need to URL-encode your token.

5. Run the script:

```bash
python gitbridge_push.py
```

If all is well, your commit is live.

## Important:

- NEVER commit `.env` to Git.
- Keep token secure. Use GitHub secrets for GitHub Actions alternatives.
