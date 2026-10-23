import os
from docx import Document
from docx.shared import Inches

class Exporter:
    def export_to_docx(self, variant, output_path):
        doc = Document()
        
        # Заголовок документа
        doc.add_heading(f"КИМ ОГЭ. Вариант {variant['variantId']}", 0)
        
        # Проходимся по всем заданиям
        for task in variant["tasks"]:
            doc.add_paragraph(f"{task['positionId']}. {task['text']}")
            
            # Вставляем картинки для участника
            for img_path in task.get("resources", []):
                if os.path.exists(img_path):
                    doc.add_picture(img_path, width=Inches(4.0))
                else:
                    print(f"ВНИМАНИЕ: Картинка не найдена: {img_path}")
                
            # Генерируем таблицы (если есть)
            for table_data in task.get("tables", []):
                table = doc.add_table(rows=1, cols=len(table_data["headers"]))
                hdr_cells = table.rows[0].cells
                for i, header in enumerate(table_data["headers"]):
                    hdr_cells[i].text = header
                
                for row_data in table_data["rows"]:
                    row_cells = table.add_row().cells
                    for i, cell_text in enumerate(row_data):
                        row_cells[i].text = cell_text
            
            doc.add_paragraph("") # Отступ между заданиями
            
        doc.save(output_path)
        print(f"Файл сохранен: {output_path}")