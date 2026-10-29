#!/bin/bash
# ==============================================================================
# EXPORT SCRIPT: Copy E-Commerce Project to Desktop & Eclipse Workspace
# ==============================================================================

set -e

SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DESKTOP_TARGET="/Users/somaindra/Desktop/ecommerce-app"
ECLIPSE_DIR="/Users/somaindra/eclipse-workspace/ecommerce-app"

echo "=========================================================="
echo "🚀 EXPORTING TRENDVIBE E-COMMERCE TO DESKTOP & ECLIPSE"
echo "=========================================================="

# 1. Export to Desktop
echo "📁 Copying to Desktop ($DESKTOP_TARGET)..."
mkdir -p "$DESKTOP_TARGET"
rsync -av --exclude 'target' --exclude '.git' "$SOURCE_DIR/" "$DESKTOP_TARGET/"
echo "✅ Copied to Desktop: $DESKTOP_TARGET"

# 2. Export to Eclipse Workspace if directory exists or create it
echo "📁 Copying to Eclipse Workspace ($ECLIPSE_DIR)..."
mkdir -p "$ECLIPSE_DIR"
rsync -av --exclude 'target' --exclude '.git' "$SOURCE_DIR/" "$ECLIPSE_DIR/"
echo "✅ Copied to Eclipse Workspace: $ECLIPSE_DIR"

# 3. Setup Git
echo "🔧 Setting up Git repository..."
cd "$DESKTOP_TARGET"
if [ ! -d ".git" ]; then
    git init
    git add .
    git commit -m "Initial commit: TrendVibe E-Commerce App (Myntra/Ajio/Nykaa style with Jakarta EE & MySQL)"
    echo "✅ Git repository initialized on Desktop!"
fi

echo "=========================================================="
echo "🎉 EXPORT COMPLETE!"
echo ""
echo "To push to your GitHub:"
echo "1. Create a new repository on https://github.com/new"
echo "2. Run these commands:"
echo "   cd $DESKTOP_TARGET"
echo "   git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/<YOUR_REPO_NAME>.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo "=========================================================="
