from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR # center textbox
from pptx.enum.shapes import MSO_SHAPE #shapes
from pptx.dml.color import RGBColor #customize font

class pptx():
    def __init__(self):
        self.prs = Presentation()

    def add_title_slide(self, title_text, subtitle_text):
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[0])
        title = slide.shapes.title
        subtitle = slide.placeholders[1]
        title.text = str(title_text)
        subtitle.text = str(subtitle_text)

    def add_song_slide(self, songlyrics):
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])
        slide_width = self.prs.slide_width
        slide_height = self.prs.slide_height
        text_box_width = Inches(6)
        text_box_height = Inches(6)
        left = (slide_width - text_box_width) / 2
        top = (slide_height - text_box_height) / 2
        txBox = slide.shapes.add_textbox(left, top, text_box_width, text_box_height)
        tf = txBox.text_frame
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        p = tf.add_paragraph()
        p.text = str(songlyrics)
        p.font.bold = True
        p.alignment = PP_ALIGN.CENTER

    def save_presentation(self, filename):
        self.prs.save(filename)


if __name__ == "__main__":
    prs = pptx()
    prs.add_title_slide("Butter", "Cup")
    prs.add_song_slide("Build me up buttercup \n Baby")
    prs.add_song_slide("13 going on 30")
    prs.save_presentation("test buttercup.pptx")
