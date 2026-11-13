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


# Класс для второй страницы(работа с БД)
class DBWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DBWindow()
        self.ui.setupUi(self)
        
        self.db = DB()
        try:
            self.db.load()
        except Exception:
            print("База не найдена, создаем новую...")
            self.db.create()
            self.db.save()

        self.base64_image = ""
        self.base64_answer = ""
        self.ui.label.setAcceptDrops(True)
        self.ui.label.dragEnterEvent = self.dragEnterEvent
        self.ui.label.dropEvent = self.dropEvent

        self.ui.label_answer.setAcceptDrops(True)
        self.ui.label_answer.dragEnterEvent = self.dragEnterEvent
        self.ui.label_answer.dropEvent = self.dropEvent_answer

        self.ui.pushButton.clicked.connect(self.add_task)       
        self.ui.pushButton_2.clicked.connect(self.delete_task)  
        self.ui.pushButton_3.clicked.connect(self.close)        

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
                    self.base64_image = base64.b64encode(image_file.read()).decode('utf-8')
                
                pixmap = QPixmap(file_path)
                self.ui.label.setPixmap(pixmap.scaled(self.ui.label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
                break

    def dropEvent_answer(self, event):
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                with open(file_path, "rb") as image_file:
                    self.base64_answer = base64.b64encode(image_file.read()).decode('utf-8')

                pixmap = QPixmap(file_path)
                self.ui.label_answer.setPixmap(pixmap.scaled(self.ui.label_answer.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
                break

    def add_task(self):
        try:
            #Заполняем дыры в ID, начиная с 100_000(метод для заполнения отрезка после удаления)
            task_id = 100_000
            if self.db.df_data is not None and not self.db.df_data.empty:
                existing_ids = sorted(self.db.df_data["taskId"].dropna().astype(int).tolist())
                
                for existing_id in existing_ids:
                    if existing_id == task_id:
                        task_id += 1
                    elif existing_id > task_id:
                        break


            subject_id = self.ui.comboBox.currentText()         
            position_id = int(self.ui.lineEdit_2.text())        
            prototype_id = int(self.ui.lineEdit_3.text())       
            difficulty = int(self.ui.comboBox_2.currentText())  
            type_ans = self.ui.comboBox_3.currentText()         
            text = self.ui.textEdit.toPlainText()               

            if not subject_id or not text.strip() or not type_ans:
                QMessageBox.warning(self, "Ошибка заполнения", "Выберите предмет, тип ответа и введите текст задания!")
                return

            #Отправляем в базу (8 аргументов)
            self.db.push(task_id, subject_id, position_id, prototype_id, "", difficulty, type_ans, text, self.base64_image, self.base64_answer)
            self.db.save()
            print(f"Задание успешно добавлено! Присвоен ID: {task_id}")


            self.ui.lineEdit_2.clear()
            self.ui.lineEdit_3.clear()
            self.ui.textEdit.clear() 
            self.ui.label.clear()
            self.ui.label_answer.clear()
            self.base64_image = ""
            self.base64_answer = ""
            
        except ValueError:
            QMessageBox.critical(self, "Ошибка формата", "В поля 'Номер по порядку' и 'Номер прототипа' нужно вводить ЧИСЛА!")


    def delete_task(self):
        try:
            task_id = int(self.ui.lineEdit_5.text()) 
            success = self.db.delete(task_id)
            
            if success:
                self.db.save()
                QMessageBox.information(self, "Успех", f"Задание с ID {task_id} успешно удалено!")
                self.ui.lineEdit_5.clear()
            else:
                QMessageBox.warning(self, "Не найдено", f"Задания с ID {task_id} не существует в базе!")
                
        except ValueError:
            QMessageBox.critical(self, "Ошибка формата", "ID для удаления должен быть числом!")


# Класс для главной страницы (генератора)
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
        elif self.ui.radioButton_5.isChecked():
            subject = "PHYS-OGE"
        else:
            QMessageBox.warning(self, "Внимание", "Пожалуйста, выберите предмет и сложность!")
            return

        count = self.ui.spinBox_2.value() 

        result_text = f"Предмет: {subject}\nКол-во: {count}"
        self.ui.textBrowser_4.setText(result_text)

        db = DB()
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
            self.ui.textBrowser_4.setText(f"Файл сохранен по пути:\n{path}")

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

# Старт
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())