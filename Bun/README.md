# Bun 開発環境

Bunランタイムを使った高速なJavaScript/TypeScript開発のための環境です。

## ベースイメージ

- `oven/bun:latest`

## 環境概要

| 項目 | 内容 |
|------|------|
| 言語 | JavaScript / TypeScript |
| ランタイム | Bun (最新版) |
| OS | Debian ベース |

## VS Code 設定

### 自動フォーマット
- 保存時に自動フォーマット有効
- Prettierをデフォルトフォーマッターに設定

### ターミナル
- デフォルトシェル: bash

## VS Code 拡張機能

| 拡張機能 | 用途 |
|----------|------|
| esbenp.prettier-vscode | Prettierによる自動コードフォーマット |

## 使い方

1. このディレクトリをコピーして任意の場所に配置
2. VS Codeで開き、「Dev Containers: Reopen in Container」を実行
3. プロジェクトを初期化してコーディング開始

## プロジェクト初期化例

```bash
# 新規プロジェクト作成
bun init

# パッケージのインストール
bun add <package-name>

# スクリプトの実行
bun run index.ts
```

## Bunの特徴

- **高速**: Node.jsよりも高速なランタイム
- **TypeScriptネイティブサポート**: 設定なしでTypeScriptを実行可能
- **ビルトインバンドラー**: 追加ツールなしでバンドル可能
- **npm互換**: 既存のnpmパッケージをそのまま利用可能
