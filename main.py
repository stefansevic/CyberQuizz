import sys
import sqlite3
import random
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QRadioButton,
    QPushButton, QButtonGroup, QComboBox, 
)
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import Qt
from quiz_ui import QuizUI

class QuizApp(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()

        self.chapter_combo = QComboBox()
        self.chapter_combo.currentIndexChanged.connect(self.update_subchapters)
        self.layout.addWidget(self.chapter_combo)

        self.subchapter_combo = QComboBox()
        self.subchapter_combo.currentIndexChanged.connect(self.load_questions)
        self.layout.addWidget(self.subchapter_combo)

        self.question_label = QLabel("Questions will appear here")
        self.layout.addWidget(self.question_label)

        self.options_group = QButtonGroup()
        self.option_buttons = []
        for i in range(4):
            btn = QRadioButton()
            self.option_buttons.append(btn)
            self.options_group.addButton(btn)
            self.layout.addWidget(btn)

        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.check_answer)
        self.layout.addWidget(self.next_button)

        self.setLayout(self.layout)
        
        self.ui = QuizUI(self)

        self.populate_chapters()  

        self.current_question_index = 0
        self.score = 0
        self.answers = []
        
        self.make_quiz_elements_visible()

    def populate_chapters(self):
        conn = sqlite3.connect("quiz.db")
        cursor = conn.cursor()
        cursor.execute("SELECT DISTINCT chapter FROM questions ORDER BY chapter")
        chapters = cursor.fetchall()
        conn.close()

        self.chapter_combo.addItem("Choose chapter", None)
        for chapter in chapters:
            self.chapter_combo.addItem(f" {chapter[0]}", chapter[0])

    def update_subchapters(self):
        self.subchapter_combo.clear()
        selected_chapter = self.chapter_combo.currentData()

        if selected_chapter is None:
            self.subchapter_combo.setEnabled(False)
            return

        conn = sqlite3.connect("quiz.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT DISTINCT subchapter FROM questions WHERE chapter = ? ORDER BY subchapter", (selected_chapter,)
        )
        subchapters = cursor.fetchall()
        conn.close()

        self.subchapter_combo.setEnabled(True)
        self.subchapter_combo.addItem("Choose subchapter", None) 
        for subchapter in subchapters:
            self.subchapter_combo.addItem(f" {subchapter[0]}", subchapter[0])

    def load_questions(self):
        selected_chapter = self.chapter_combo.currentData()
        selected_subchapter = self.subchapter_combo.currentData()

        if selected_chapter is None or selected_subchapter is None:
            return  

        conn = sqlite3.connect("quiz.db")
        cursor = conn.cursor()
        cursor.execute(
            "SELECT * FROM questions WHERE chapter = ? AND subchapter = ?",
            (selected_chapter, selected_subchapter),
        )
        self.questions = cursor.fetchall()
        conn.close()

        self.current_question_index = 0
        self.score = 0
        self.answers = []  
        self.show_question()

    def show_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]

            self.question_label.setText(question[1])  

            options = [question[2], question[3], question[4], question[5]]
            correct_option = question[6]
            correct_answer_text = options[correct_option - 1]  

            random.shuffle(options)

            for i in range(4):
                self.option_buttons[i].setText(options[i])
                self.option_buttons[i].setChecked(False)

            self.correct_index = options.index(correct_answer_text) + 1  
        else:
            self.show_result()

    def check_answer(self):
        selected_index = None
        for i, btn in enumerate(self.option_buttons):
            if btn.isChecked():
                selected_index = i + 1  

        if selected_index is None:
            return
            
        correct = selected_index == self.correct_index
        self.answers.append({
            'question': self.questions[self.current_question_index][1], 
            'user_answer': self.option_buttons[selected_index - 1].text() if selected_index else "No answer", 
            'correct_answer': self.option_buttons[self.correct_index - 1].text(),
            'correct': correct
        })

        if correct:
            self.score += 1

        self.current_question_index += 1
        self.show_question()

    def show_result(self):
        self.ui.show_end_screen(self.score, len(self.questions), self.answers)
        
    def create_button(self, text, function):
        button = QPushButton(text)
        button.clicked.connect(function)
        return button
    
    def make_quiz_elements_visible(self):
        self.question_label.show()
        for btn in self.option_buttons:
            btn.show()
        self.next_button.show()
        
    def restart_quiz(self):
        import sys
        import os
        
        python = sys.executable
        script = sys.argv[0]
        args = sys.argv[1:]
        
        self.ui.close()
        
        os.execl(python, python, script, *args)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QuizApp()
    window.ui.show()  
    sys.exit(app.exec())