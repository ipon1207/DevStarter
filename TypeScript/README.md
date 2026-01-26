# TypeScript 開発環境

TypeScript/Node.jsを使ったWebアプリケーション開発のための環境です。

## ベースイメージ

- `mcr.microsoft.com/devcontainers/typescript-node:1-22-bookworm`

## 環境概要

| 項目 | 内容 |
|------|------|
| 言語 | TypeScript |
| ランタイム | Node.js 22 |
| OS | Debian Bookworm |

## VS Code 設定

### 自動フォーマット
- 保存時に自動フォーマット有効
- Prettierをデフォルトフォーマッターに設定

### ESLint
- 保存時にESLintの自動修正を実行

## VS Code 拡張機能

| 拡張機能 | 用途 |
|----------|------|
| dbaeumer.vscode-eslint | ESLintによるリント・コード品質チェック |
| esbenp.prettier-vscode | Prettierによる自動コードフォーマット |

## 使い方

1. このディレクトリをコピーして任意の場所に配置
2. VS Codeで開き、「Dev Containers: Reopen in Container」を実行
3. プロジェクトを初期化してコーディング開始

## プロジェクト初期化例

```bash
# 新規プロジェクト作成
npm init -y

# TypeScript & 型定義のインストール
npm install -D typescript @types/node

# tsconfig.json生成
npx tsc --init

# ESLint設定（任意）
npm init @eslint/config

# Prettier設定（任意）
echo '{}' > .prettierrc
```

## 備考

- Node.js 22 (LTS) がプリインストールされています
- npm/npxがすぐに使用可能です
- 必要に応じてyarnやpnpmをインストールできます
