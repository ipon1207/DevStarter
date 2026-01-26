# Rust 開発環境

Rustを使ったシステムプログラミング・アプリケーション開発のための環境です。

## ベースイメージ

- `mcr.microsoft.com/devcontainers/rust:latest`

## 環境概要

| 項目 | 内容 |
|------|------|
| 言語 | Rust (最新安定版) |
| ビルドツール | Cargo |

## VS Code 設定

### 自動フォーマット
- 保存時に自動フォーマット有効
- rust-analyzerをデフォルトフォーマッターに設定

### Clippy
- `cargo check` の代わりに `cargo clippy` を使用
- より厳密なリントチェックを実行

### その他
- インレイヒントを有効化
- Cargoの自動リロードを有効化

## VS Code 拡張機能

| 拡張機能 | 用途 |
|----------|------|
| rust-lang.rust-analyzer | Rustの公式言語サーバー（インテリセンス、補完、リファクタリング等） |
| vadimcn.vscode-lldb | LLDBデバッガ（ブレークポイント、ステップ実行等） |
| tamasfe.even-better-toml | TOML（Cargo.toml等）のシンタックスハイライト・検証 |
| fill-labs.dependi | 依存関係の可視化・バージョン管理 |

## 使い方

1. このディレクトリをコピーして任意の場所に配置
2. VS Codeで開き、「Dev Containers: Reopen in Container」を実行
3. `cargo new project_name` でプロジェクト作成
4. コーディング開始

## よく使うコマンド

```bash
# 新規プロジェクト作成
cargo new project_name

# ビルド
cargo build

# 実行
cargo run

# テスト
cargo test

# リント（Clippy）
cargo clippy

# フォーマット
cargo fmt
```
