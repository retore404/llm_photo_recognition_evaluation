#!/bin/bash

# 日本語フォントとロケールのセットアップ
echo "BEGIN: Japanese fonts and locale setup"
sudo apt-get update
sudo apt-get install -y \
    fonts-liberation \
    fonts-noto-cjk \
    fonts-ipafont-gothic \
    fonts-ipafont-mincho \
    locales

# 日本語ロケール生成
sudo locale-gen ja_JP.UTF-8

# APTキャッシュクリーンアップ
sudo rm -rf /var/lib/apt/lists/*
echo "END: Japanese fonts and locale setup"

# Git設定
echo "BEGIN: Git setup"
git config --local --bool push.autoSetupRemote true
echo "END: Git setup"

# uvインストール
echo "BEGIN: uv setup"
curl -LsSf https://astral.sh/uv/install.sh | sh
echo 'export PATH="$HOME/.cargo/bin:$PATH"' >> ~/.bashrc
echo "END: uv setup"

echo "Setup completed successfully!"