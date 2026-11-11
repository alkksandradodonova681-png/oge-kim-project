from DataBase import DB
from Units import Task
from Exeptions import LevelSumError
import random
import base64
import io
import os
from datetime import datetime
from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt
from PIL import Image

class Generator():
    def __init__(self,subject: str, level_sum: int, base: DB):
        self.subject = subject
        self.level_sum = level_sum
        self.base = base
        if not((self.subject == "MATH-OGE" and 25 <= level_sum <= 75) or (self.subject == "PHYS-OGE" and 22 <= level_sum <= 66)):
            raise LevelSumError


    def level_gen(self, task_am: int) -> list:
        if not (task_am <= self.level_sum <= 3 * task_am):
            raise ValueError()

        levels = []
        for i in range(task_am):
            rem = self.level_sum - sum(levels)
            k = task_am - i - 1
            lo = max(1, rem - 3 * k)
            hi = min(3, rem - k)
            levels.append(random.randint(lo, hi))
        random.shuffle(levels)

        return levels


    def generate(self) -> list:
        if self.subject == "MATH-OGE":
            levels = self.level_gen(25)
            tasks = []
            for position in range(1,26):
                 rand_buf = random.choice(self.base.get(task_id=None, subject_id="MATH-OGE", position_id=position,
                              topic_id="", difficulty=levels[position - 1], type_ans=None, text=None, image=None))
                 tasks.append(Task(rand_buf["text"], rand_buf["image"]))

        elif self.subject == "PHYS-OGE":
            levels = self.level_gen(22)
            tasks = []
            for position in range(1,23):
                 rand_buf = random.choice(self.base.get(task_id=None, subject_id="PHYS-OGE", position_id=position,
                              topic_id="", difficulty=levels[position - 1], type_ans=None, text=None, image=None))
                 tasks.append(Task(rand_buf["text"], rand_buf["image"]))
        return tasks

    def _image_par(self, doc, img, width, max_h=None, indent=0.0, new_page=False, keep=False):
        if max_h and width * img.height / img.width > max_h:
            width = max_h * img.width / img.height
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.left_indent = Cm(-indent)
        p.paragraph_format.right_indent = Cm(-indent)
        p.paragraph_format.page_break_before = new_page
        p.paragraph_format.keep_with_next = keep
        run = p.add_run()
        run.font.size = Pt(1)
        buf = io.BytesIO()
        img.save(buf, format="PNG")
        run.add_picture(buf, width=Cm(width))

    def _add_task(self, doc, number: int, task, answer_line: bool):
        p = doc.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_together = True
        p.paragraph_format.keep_with_next = bool(task.picture) or answer_line
        p.add_run(f"{number}. ").bold = True
        p.add_run(task.text)

        if task.picture:
            img = Image.open(io.BytesIO(base64.b64decode(task.picture)))
            width = min(img.width / 96 * 2.54, 12)
            self._image_par(doc, img, width, max_h=8, keep=answer_line)

        if answer_line:
            p = doc.add_paragraph("Ответ: " + "_" * 28 + ".")
            p.paragraph_format.space_after = Pt(14)

    def render(self, tasks: list = None, out_dir: str = "Variants", assets_dir: str = "Assets") -> str:
        if tasks is None:
            tasks = self.generate()

        if self.subject == "MATH-OGE":
            prefix, part1_end = "math", 19
            front = ["cover", "instructions", "ref_alg", "ref_pow", "ref_geo", "ref_sq"]
        else:
            prefix, part1_end = "phys", 16
            front = ["cover", "instructions", "ref_table1", "ref_table2"]

        def load(name):
            im = Image.open(os.path.join(assets_dir, f"{prefix}_{name}.png")).convert("RGBA")
            bg = Image.new("RGBA", im.size, "white")
            bg.alpha_composite(im)
            return bg.convert("RGB")

        doc = Document()
        doc.styles["Normal"].font.name = "Times New Roman"
        doc.styles["Normal"].font.size = Pt(12)

        sec = doc.sections[0]
        sec.page_width, sec.page_height = Cm(21), Cm(29.7)
        sec.top_margin = sec.bottom_margin = sec.left_margin = sec.right_margin = Cm(0)
        for i, name in enumerate(front):
            self._image_par(doc, load(name), 21, max_h=29, new_page=(i > 0))

        header = load("blank")
        header_h = 21 * header.height / header.width
        sec = doc.add_section(WD_SECTION.NEW_PAGE)
        sec.top_margin, sec.bottom_margin = Cm(header_h + 0.3), Cm(2)
        sec.left_margin = sec.right_margin = Cm(2.5)
        sec.header_distance = Cm(0)
        hp = sec.header.paragraphs[0]
        hp.paragraph_format.space_after = Pt(0)
        hp.paragraph_format.left_indent = hp.paragraph_format.right_indent = Cm(-2.5)
        hr = hp.add_run()
        hr.font.size = Pt(1)
        buf = io.BytesIO()
        header.save(buf, format="PNG")
        hr.add_picture(buf, width=Cm(21))

        for number, task in enumerate(tasks, start=1):
            if number in (1, part1_end + 1):
                banner = load("part1" if number == 1 else "part2")
                banner = banner.crop((0, header.height, banner.width, banner.height))
                self._image_par(doc, banner, 21, indent=2.5, new_page=(number != 1), keep=True)
            self._add_task(doc, number, task, answer_line=(number <= part1_end))

        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, f"{prefix}_variant_{datetime.now():%Y%m%d_%H%M%S}.docx")
        doc.save(path)
        return path

    def get_variants(self,amount: int) -> int:
        for _ in range(amount):
            self.render(self.generate())
