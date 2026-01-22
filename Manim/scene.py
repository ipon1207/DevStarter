from manim import *

class JapaneseTest(Scene):
    def construct(self):
        # 1. Textクラス（Pango）: ここはOSのフォント(Noto Sans)を使います
        text = Text("こんにちは、Manim！", font="Noto Sans CJK JP")
        text.to_edge(UP)

        # 2. Texクラス（LaTeX）: HaranoAjiフォント(デフォルト)を使います
        tex_template = TexTemplate()
        tex_template.tex_compiler = "lualatex"
        tex_template.output_format = ".pdf" 
        
        # 以前の複雑なフォント設定をやめ、標準的なプリセットを使います
        tex_template.add_to_preamble(r"\usepackage{luatexja}")
        tex_template.add_to_preamble(r"\usepackage[haranoaji]{luatexja-preset}")

        tex = Tex(
            r"円の面積は $S = \pi r^2$ です。",
            tex_template=tex_template,
        )
        
        self.play(Write(text))
        self.play(Write(tex))
        self.wait(2)