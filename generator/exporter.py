import os
from docx import Document
from docx.shared import Cm, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

class Exporter:
    def export_to_docx(self, variant, subject, output_path):
        doc = Document()
        
        # --- НАСТРОЙКА СТИЛЕЙ (Times New Roman, 12pt, интервал 1.0) ---
        style = doc.styles['Normal']
        font = style.font
        font.name = 'Times New Roman'
        font.size = Pt(12)
        paragraph_format = style.paragraph_format
        paragraph_format.line_spacing = 1.0
        paragraph_format.space_after = Pt(6)
        
        # Настраиваем поля страницы
        section = doc.sections[0]
        section.page_width = Cm(21)
        section.page_height = Cm(29.7)
        section.left_margin = Cm(2)
        section.right_margin = Cm(1.5)
        section.top_margin = Cm(1.5)
        section.bottom_margin = Cm(1.5)

        templates_dir = "data/templates"

        # --- БЛОК 1: ТИТУЛЬНЫЙ ЛИСТ, ИНСТРУКЦИЯ И СПРАВОЧНИКИ ---
        cover_path = os.path.join(templates_dir, f"{subject}_cover.png")
        if os.path.exists(cover_path):
            doc.add_picture(cover_path, width=Cm(17))
            doc.add_page_break()

        instr_path = os.path.join(templates_dir, f"{subject}_instructions.png")
        if os.path.exists(instr_path):
            doc.add_picture(instr_path, width=Cm(17))
            doc.add_page_break()

        if subject == "math":
            refs = ["math_ref_alg.png", "math_ref_pow.png", "math_ref_geo.png", "math_ref_sq.png"]
            for ref in refs:
                ref_path = os.path.join(templates_dir, ref)
                if os.path.exists(ref_path):
                    doc.add_picture(ref_path, width=Cm(17))
                    doc.add_page_break()

        # --- ФУНКЦИЯ ДЛЯ ВСТАВКИ ЗАДАНИЯ С КАРТИНКОЙ СПРАВА ---
        def add_task_with_image(doc, task):
            # Если у задания есть картинки, создаем таблицу из 2 колонок
            if task.get("resources"):
                table = doc.add_table(rows=1, cols=2)
                table.autofit = False
                # Ширина колонок: текст - 11 см, картинка - 6 см
                table.columns[0].width = Cm(11)
                table.columns[1].width = Cm(6)

                # Левая колонка (Текст)
                cell_text = table.cell(0, 0)
                p = cell_text.paragraphs[0]
                run = p.add_run(f"{task['positionId']}. ")
                run.bold = True
                p.add_run(task['text'])

                # Правая колонка (Картинка)
                cell_img = table.cell(0, 1)
                p_img = cell_img.paragraphs[0]
                p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
                # Берем первую картинку из списка
                img_path = task["resources"][0]
                if os.path.exists(img_path):
                    run_img = p_img.add_run()
                    run_img.add_picture(img_path, width=Cm(5)) # Одинаковый размер для всех картинок
            else:
                # Если картинки нет, просто пишем текст
                p = doc.add_paragraph()
                run = p.add_run(f"{task['positionId']}. ")
                run.bold = True
                p.add_run(task['text'])

        # --- БЛОК 2: ЧАСТЬ 1 ---
        part1_path = os.path.join(templates_dir, f"{subject}_part1.png")
        if os.path.exists(part1_path):
            doc.add_picture(part1_path, width=Cm(17))

        for task in variant["tasks"]:
            if task["positionId"] > 19:
                continue
            add_task_with_image(doc, task)
            
            # Таблицы (если есть)
            for table_data in task.get("tables", []):
                doc.add_paragraph()
                table = doc.add_table(rows=1, cols=len(table_data["headers"]))
                table.style = 'Table Grid'
                hdr_cells = table.rows[0].cells
                for i, header in enumerate(table_data["headers"]):
                    hdr_cells[i].text = header
                    for run in hdr_cells[i].paragraphs[0].runs:
                        run.bold = True
                
                for row_data in table_data["rows"]:
                    row_cells = table.add_row().cells
                    for i, cell_text in enumerate(row_data):
                        row_cells[i].text = cell_text
            
            doc.add_paragraph("")

        # --- БЛОК 3: ЧАСТЬ 2 ---
        doc.add_page_break() 
        
        part2_path = os.path.join(templates_dir, f"{subject}_part2.png")
        if os.path.exists(part2_path):
            doc.add_picture(part2_path, width=Cm(17))

        for task in variant["tasks"]:
            if task["positionId"] <= 19:
                continue
            add_task_with_image(doc, task)
            doc.add_paragraph("")

        # --- БЛОК 4: ЛИСТ ПРОВЕРЯЮЩЕГО (ОТВЕТЫ) ---
        doc.add_page_break()
        
        ans_header_path = os.path.join(templates_dir, f"{subject}_answers_header.png")
        if os.path.exists(ans_header_path):
            doc.add_picture(ans_header_path, width=Cm(17))
        
        doc.add_paragraph("Таблица ответов на задания первой части:")
        
        part1_tasks = [t for t in variant["tasks"] if t["positionId"] <= 19]
        
        if part1_tasks:
            table = doc.add_table(rows=2, cols=len(part1_tasks))
            table.style = 'Table Grid'
            table.alignment = WD_ALIGN_PARAGRAPH.CENTER
            
            for i, task in enumerate(part1_tasks):
                cell = table.cell(0, i)
                cell.text = str(task["positionId"])
                cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
                for run in cell.paragraphs[0].runs:
                    run.bold = True
                    
            for i, task in enumerate(part1_tasks):
                cell = table.cell(1, i)
                answer = ", ".join(task.get("correctKey", []))
                cell.text = answer
                cell.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

        doc.add_paragraph("\nКритерии оценивания заданий с развернутым ответом (20-25):")
        
        for task in variant["tasks"]:
            if task["positionId"] > 19:
                p = doc.add_paragraph()
                run = p.add_run(f"Задание {task['positionId']}:\n")
                run.bold = True
                p.add_run(f"Ответ: {', '.join(task.get('correctKey', []))}\n")
                
                if "criteria" in task and task["criteria"]:
                    for crit in task["criteria"]:
                        p.add_run(f"- {crit['description']} ({crit['points']} б.)\n")
                doc.add_paragraph("")

        doc.save(output_path)
        print(f"\nФайл сохранен: {output_path}")