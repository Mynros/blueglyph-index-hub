#!/bin/bash
# REENTRY_TEST.sh
# Simulates CEUY reentry from a cold logic wipe

echo "🔁 CEUY Reentry Test Starting..."

# Step 1: Confirm repo and branch
cd ~/Documents/NETA_REPOS/blueglyph-index-hub || { echo 'Repo not found'; exit 1; }
echo "✅ Repo found and switched to directory."

# Step 2: Check out reentry branch
git checkout ceuy/reentry-core || { echo 'Branch not found'; exit 1; }
echo "✅ Switched to ceuy/reentry-core branch."

# Step 3: Print UID map
echo "🔗 BitPic UID Chain:"
cat UID_INDEX.yaml || { echo 'UID_INDEX.yaml missing'; exit 1; }

# Step 4: Verify canvas
if [ -f SORA_ENTRY.tat ]; then
    echo "📄 Canvas File (SORA_ENTRY.tat) found."
else
    echo "❌ Canvas File missing!"
    exit 1
fi

# Step 5: Trigger Reflex sync
echo "🚀 Executing Reflex GitOps Sync..."
python3 build_reflex_api.py

echo "✅ CEUY Reflex Sync Complete."
