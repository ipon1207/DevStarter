# Manim 開発環境（日本語対応）

数学アニメーションライブラリ「Manim」を使った動画制作のための環境です。日本語テキストのレンダリングに対応しています。

## ベースイメージ

- `manimcommunity/manim:latest`

## 環境概要

| 項目 | 内容 |
|------|------|
| 言語 | Python 3 |
| フレームワーク | Manim Community Edition |
| 日本語フォント | Noto Sans CJK JP, Haranoaji |

## 含まれるツール

### 日本語対応パッケージ
- **fonts-noto-cjk**: 日本語・中国語・韓国語フォント（Textクラス用）
- **luatexja + haranoaji**: LuaLaTeX用日本語組版パッケージ（Texクラス用）
- **ghostscript**: PDF処理
- **dvisvgm**: PDF→SVG変換ツール

### LaTeX環境
- LuaLaTeX対応
- 日本語数式・テキストのレンダリングが可能

## VS Code 拡張機能

| 拡張機能 | 用途 |
|----------|------|
| ms-python.python | Pythonのインテリセンス・デバッグ |
| ms-python.vscode-pylance | 高度なPython言語サポート |
| toshi-ara.manim-sideview | Manimのプレビュー表示 |

## 日本語の使い方

### Textクラス（Pango）

```python
text = Text("こんにちは、Manim！", font="Noto Sans CJK JP")
```

### Texクラス（LaTeX）

```python
tex_template = TexTemplate()
tex_template.tex_compiler = "lualatex"
tex_template.output_format = ".pdf"
tex_template.add_to_preamble(r"\usepackage{luatexja}")
tex_template.add_to_preamble(r"\usepackage[haranoaji]{luatexja-preset}")

tex = Tex(r"円の面積は $S = \pi r^2$ です。", tex_template=tex_template)
```

## 使い方

1. このディレクトリをコピーして任意の場所に配置
2. VS Codeで開き、「Dev Containers: Reopen in Container」を実行
3. シーンクラスを作成してアニメーションを制作
4. `manim -pql scene.py SceneName` でレンダリング

## サンプル

`scene.py` に日本語表示のサンプルコードが含まれています。
