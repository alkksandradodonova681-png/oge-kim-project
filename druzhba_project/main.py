import sys
import base64
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from ui_genpage import Ui_MainWindow 
from ui_dbpage import Ui_MainWindow as Ui_DBWindow
from DataBase import DB
from Generator import Generator
from Exeptions import LevelSumError


#класс для второй страницы(работа с БД)
class DBWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DBWindow()
        self.ui.setupUi(self)
        
        self.db_path = None
        self.db = None
        self._load_db_for_current_subject()

        self.base64_images = []        # список картинок задания
        self.base64_answer_images = [] # список картинок ответа
        
        self.ui.label.setAcceptDrops(True)
        self.ui.label.dragEnterEvent = self.dragEnterEvent
        self.ui.label.dropEvent = self.dropEvent

        self.ui.label_answer.setAcceptDrops(True)
        self.ui.label_answer.dragEnterEvent = self.dragEnterEvent
        self.ui.label_answer.dropEvent = self.dropEvent_answer

        self.ui.pushButton.clicked.connect(self.add_task)       
        self.ui.pushButton_2.clicked.connect(self.delete_task)  
        self.ui.pushButton_3.clicked.connect(self.close)
        
        #при смене предмета — переключаем базу
        self.ui.comboBox.currentIndexChanged.connect(self._on_subject_changed)

    def _load_db_for_current_subject(self):
        subject = self.ui.comboBox.currentText()
        if subject == "PHYS-OGE":
            self.db_path = "phys_data.json"
        else:
            self.db_path = "math_data.json"
        self.db = DB(self.db_path)
        try:
            self.db.load()
        except Exception:
            print("База не найдена, создаем новую...")
            self.db.create()
            self.db.save()

    def _on_subject_changed(self):
        if self.db is not None:
            self.db.save()
        self._load_db_for_current_subject()
        self.ui.lineEdit_2.clear()
        self.ui.lineEdit_3.clear()
        self.ui.textEdit.clear()
        self.ui.label.clear()
        self.ui.label_answer.clear()
        if hasattr(self.ui, "answer_side"):
            self.ui.answer_side.clear()
        self.base64_images = []
        self.base64_answer_images = []

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                with open(file_path, "rb") as image_file:
                    b64 = base64.b64encode(image_file.read()).decode('utf-8')
                    self.base64_images.append(b64)
                
                pixmap = QPixmap(file_path)
                self.ui.label.setPixmap(pixmap.scaled(self.ui.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
                break

    def dropEvent_answer(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                with open(file_path, "rb") as image_file:
                    b64 = base64.b64encode(image_file.read()).decode('utf-8')
                    self.base64_answer_images.append(b64)

                pixmap = QPixmap(file_path)
                self.ui.label_answer.setPixmap(pixmap.scaled(self.ui.label_answer.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
                break

    def add_task(self):
        try:
            # Заполняем дыры в ID, начиная с 100_000, проверяя обе базы
            used_ids = set()
            for path in ("math_data.json", "phys_data.json"):
                other_db = DB(path)
                try:
                    other_db.load()
                except Exception:
                    continue
                if other_db.df_data is not None and not other_db.df_data.empty:
                    used_ids.update(other_db.df_data["taskId"].dropna().astype(int).tolist())
            
            task_id = 100_000
            while task_id in used_ids:
                task_id += 1


            subject_id = self.ui.comboBox.currentText()         
            position_id = int(self.ui.lineEdit_2.text())        
            prototype_id = int(self.ui.lineEdit_3.text())       
            difficulty = int(self.ui.comboBox_2.currentText())  
            type_ans = self.ui.comboBox_3.currentText()         
            text = self.ui.textEdit.toPlainText()               

            if not subject_id or not text.strip() or not type_ans:
                QMessageBox.warning(self, "Ошибка заполнения", "Выберите предмет, тип ответа и введите текст задания!")
                return

            #текстовый ответ
            answer_text = ""
            if hasattr(self.ui, "answer_side"):
                answer_text = self.ui.answer_side.toPlainText().strip()

            self.db.push(task_id, subject_id, position_id, prototype_id, "", difficulty, type_ans, text, 
                         self.base64_images, answer_text, self.base64_answer_images)
            self.db.save()
            print(f"Задание успешно добавлено! Присвоен ID: {task_id}")


            self.ui.lineEdit_2.clear()
            self.ui.lineEdit_3.clear()
            self.ui.textEdit.clear() 
            self.ui.label.clear()
            self.ui.label_answer.clear()
            if hasattr(self.ui, "answer_side"):
                self.ui.answer_side.clear()
            self.base64_images = []
            self.base64_answer_images = []
            
        except ValueError:
            QMessageBox.critical(self, "Ошибка формата", "В поля 'Номер по порядку' и 'Номер прототипа' нужно вводить ЧИСЛА!")


    def delete_task(self):
        try:
            task_id = int(self.ui.lineEdit_5.text())
        except ValueError:
            QMessageBox.critical(self, "Ошибка формата", "ID для удаления должен быть числом!")
            return

        #Ищем, в какой базе находится ID
        found_in = None
        for path in ("math_data.json", "phys_data.json"):
            db = DB(path)
            try:
                db.load()
            except Exception:
                continue
            if db.df_data is not None and not db.df_data.empty:
                if task_id in db.df_data["taskId"].values:
                    found_in = (path, db)
                    break

        if found_in is None:
            QMessageBox.warning(self, "Не найдено", f"Задания с ID {task_id} нет ни в одной базе!")
            return

        path, db = found_in
        db.delete(task_id)
        db.save()

        #Обновляем текущую открытую базу, если это она
        if path == self.db_path:
            self.db = db

        QMessageBox.information(self, "Успех", f"Задание с ID {task_id} удалено из {path}!")
        self.ui.lineEdit_5.clear()


#класс для главной страницы (генератора)
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.on_button_click) 
        self.ui.pushButton.clicked.connect(self.open_db_window)    

        self.db_window = None 

    def on_button_click(self):
        if self.ui.radioButton_4.isChecked(): 
            subject = "MATH-OGE" 
            db_path = "math_data.json"
        elif self.ui.radioButton_5.isChecked():
            subject = "PHYS-OGE"
            db_path = "phys_data.json"
        else:
            QMessageBox.warning(self, "Внимание", "Пожалуйста, выберите предмет и сложность!")
            return

        count = self.ui.spinBox_2.value() 

        result_text = f"Предмет: {subject}\nКол-во: {count}"
        self.ui.textBrowser_4.setText(result_text)

        db = DB(db_path)
        try:
            db.load()
            
            if not os.path.exists("Assets"):
                os.makedirs("Assets")
            if not os.path.exists("Variants"):
                os.makedirs("Variants")

            gen = Generator(subject, count, db)
            
            QMessageBox.information(self, "Генерация", "Начинаем генерацию варианта... Это может занять время.")
            path = gen.render()
            
            QMessageBox.information(self, "Успех", f"Вариант успешно сохранен:\n{path}")

        except LevelSumError:
            QMessageBox.critical(self, "Ошибка суммы уровней", "Сумма уровней не соответствует выбранному предмету!")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Произошла ошибка при генерации: {e}")

    def open_db_window(self):
        if self.db_window is None:
            self.db_window = DBWindow()
        self.db_window.show()
        self.db_window.raise_()          
        self.db_window.activateWindow()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())