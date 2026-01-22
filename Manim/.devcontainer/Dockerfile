FROM manimcommunity/manim:latest

USER root

# 1. OSパッケージのインストール
# fonts-noto-cjk: 日本語フォント
# ghostscript: PDF処理用
# dvisvgm: PDFをSVGに変換するツール (OS版をインストール)
RUN apt-get update && apt-get install -y \
    fonts-noto-cjk \
    ghostscript \
    dvisvgm \
    && rm -rf /var/lib/apt/lists/*

# 2. TeXパッケージのインストール (tlmgr)
# 日本語環境とフォント
RUN tlmgr install luatex85 luatexja haranoaji

# 3. 【重要】競合の解消
# PATHの優先順位により TeX Live版の dvisvgm が使われてしまうため、
# それを削除して、上記で入れた OS版 (/usr/bin/dvisvgm) が使われるようにする
RUN rm -f /usr/local/texlive/*/bin/*/dvisvgm

USER manimuser