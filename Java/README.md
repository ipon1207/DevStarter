# Java 開発環境

Java 21を使ったアプリケーション開発のための環境です。

## ベースイメージ

- `mcr.microsoft.com/devcontainers/java:1-21-bullseye`

## 環境概要

| 項目 | 内容 |
|------|------|
| 言語 | Java 21 (LTS) |
| OS | Debian Bullseye |

## 含まれるツール

- **JDK 21**: 最新のLTS版Java Development Kit
- 標準的なJava開発ツールチェーン

## VS Code 拡張機能

| 拡張機能 | 用途 |
|----------|------|
| vscjava.vscode-java-pack | Java開発に必要な拡張機能パック（Language Support, Debugger, Test Runner, Maven, IntelliCode等） |

## 使い方

1. このディレクトリをコピーして任意の場所に配置
2. VS Codeで開き、「Dev Containers: Reopen in Container」を実行
3. `.java` ファイルまたはプロジェクトを作成してコーディング開始

## 備考

- MavenやGradleは事前インストールされていませんが、必要に応じてプロジェクト作成時にインストール可能です
