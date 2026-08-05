#!/bin/bash
echo "=== Daily GitHub Tool - First Time Setup ==="
git init
git add .
git commit -m "Initial commit: Daily GitHub Contribution Tool"
echo
echo "Next:"
echo "1. Create an empty GitHub repository."
echo "2. Copy its HTTPS URL."
echo "3. Run:"
echo '   git remote add origin YOUR_GITHUB_REPOSITORY_URL'
echo '   git branch -M main'
echo '   git push -u origin main'
