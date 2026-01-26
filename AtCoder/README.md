# AtCoder 開発環境

C++を使った競技プログラミング（AtCoder）のための開発環境です。

## ベースイメージ

- `mcr.microsoft.com/devcontainers/cpp:1-ubuntu-22.04`

## 環境概要

| 項目 | 内容 |
|------|------|
| 言語 | C++ (C++20) |
| コンパイラ | GCC (g++) |
| OS | Ubuntu 22.04 |

## 含まれるツール

- **online-judge-tools (oj)**: サンプルケースの自動取得・テスト実行ツール
- **atcoder-cli (acc)**: AtCoderの問題管理・提出支援CLIツール
- **AtCoder Library (AC Library)**: AtCoder公式の競技プログラミング用ライブラリ（`/opt/ac-library`に配置）

## VS Code 拡張機能

| 拡張機能 | 用途 |
|----------|------|
| ms-vscode.cpptools | C++のインテリセンス・デバッグ |
| ms-vscode.cpptools-extension-pack | C++開発ツールパック |
| formulahendry.code-runner | ワンクリックでコード実行 |
| wmaurer.change-case | 変数名のケース変換 |

## コンパイル設定

Code Runnerの実行コマンドは以下の通り設定されています：

```bash
g++ $fileName -o $fileNameWithoutExt -std=c++20 -Wall -Wextra -O2 -D_GLIBCXX_DEBUG -I/opt/ac-library
```

- `-std=c++20`: C++20規格を使用
- `-Wall -Wextra`: 警告を有効化
- `-O2`: 最適化レベル2
- `-D_GLIBCXX_DEBUG`: デバッグ用のランタイムチェックを有効化
- `-I/opt/ac-library`: AC Libraryのインクルードパスを追加

## 使い方

1. このディレクトリをコピーして任意の場所に配置
2. VS Codeで開き、「Dev Containers: Reopen in Container」を実行
3. `.cpp` ファイルを作成してコーディング開始
4. `Ctrl + Alt + N` (Code Runner) でコンパイル＆実行
