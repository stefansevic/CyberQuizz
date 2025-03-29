from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QFrame, QPushButton, QScrollArea
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import Qt

class QuizUI(QMainWindow):
    def __init__(self, quiz_app):
        super().__init__()
        self.quiz_app = quiz_app
        
        self.bg_color = "#333333"  
        self.accent_color = "#531253"  
        self.combobox_color = "#525252"
                
        self.setWindowTitle("CyberQuizz")
        self.setGeometry(200, 200, 800, 600)  
        
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        main_layout = QVBoxLayout(self.central_widget)
        main_layout.setContentsMargins(15, 15, 15, 15)
        main_layout.setSpacing(15)

        title_label = QLabel("Sigurnost računarskih sistema i mreža")
        title_label.setFont(QFont("Arial", 36, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setObjectName("title")
        
        main_layout.addWidget(title_label)

        main_layout.addWidget(quiz_app.chapter_combo)
        main_layout.addWidget(quiz_app.subchapter_combo)
        main_layout.addWidget(quiz_app.question_label)

        for btn in quiz_app.option_buttons:
            main_layout.addWidget(btn)

        main_layout.addWidget(quiz_app.next_button)
        
        self.setStyleSheet(self.get_stylesheet())

    def get_stylesheet(self):
        return f"""
        QMainWindow, QWidget {{
            background-color: {self.bg_color};
        }}
        
        QLabel {{
            color: white;
            font-size: 16px;
            padding: 5px;
        }}
        
        QLabel#title {{
            font-size: 36px;
            font-weight: bold;
            padding: 5px;
            background-color: {self.accent_color};
            border-radius: 10px;
        }}
        
        QComboBox {{
            background-color: {self.combobox_color};
            color: white;
            border: 2px solid {self.accent_color};
            border-radius: 8px;
            padding: 8px;
            min-height: 35px;
            font-size: 14px;
            selection-background-color: {self.accent_color};
        }}
        
        QComboBox::drop-down {{
            subcontrol-origin: padding;
            subcontrol-position: top right;
            width: 30px;
            background-color: {self.accent_color};
            border-top-right-radius: 6px;
            border-bottom-right-radius: 6px;
        }}
        
        QComboBox QAbstractItemView {{
            background-color: #444444;
            color: white;
            selection-background-color: {self.accent_color};
            border: 2px solid {self.accent_color};
        }}
        
        QPushButton {{
            background-color: {self.accent_color};
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px;
            font-size: 14px;
            font-weight: bold;
        }}
        
        QPushButton:hover {{
            background-color: #722372;
        }}
        
        QPushButton:pressed {{
            background-color: #3F0E3F;
        }}
        
        /* End screen styles */
        QFrame#endScreen {{
            background-color: {self.bg_color};
            border: 2px solid {self.accent_color};
            border-radius: 12px;
            padding: 20px;
        }}
        
        QLabel#scoreLabel {{
            font-size: 24px;
            color: white;
            margin-bottom: 15px;
        }}
        
        QLabel#resultDetail {{
            font-size: 14px;
            color: white;
            background-color: #444444;
            border-radius: 6px;
            padding: 10px;
            margin: 5px 0;
        }}
        
        QScrollArea {{
            border: none;
            background-color: transparent;
        }}
        
        QScrollArea > QWidget > QWidget {{
            background-color: transparent;
        }}
        
        QScrollBar:vertical {{
            border: none;
            background: #444444;
            width: 14px;
            margin: 0px;
        }}
        
        QScrollBar::handle:vertical {{
            background: {self.accent_color};
            min-height: 30px;
            border-radius: 7px;
        }}
        
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
            height: 0px;
        }}
        """
        
    def show_end_screen(self, score, total, answers):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(20, 20, 20, 20)
        
        end_frame = QFrame()
        end_frame.setObjectName("endScreen")
        end_layout = QVBoxLayout(end_frame)
        
        score_label = QLabel(f"Quiz Complete!\nYour Score: {score}/{total}")
        score_label.setObjectName("scoreLabel")
        score_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        end_layout.addWidget(score_label)
        
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_content = QWidget()
        scroll_layout = QVBoxLayout(scroll_content)
        
        results_title = QLabel("Detailed Results:")
        results_title.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        scroll_layout.addWidget(results_title)
        
        for i, answer in enumerate(answers, 1):
            question_result = QLabel(
                f"Question {i}:\n\n"
                f"{answer['question']}\n\n"
                f"Your answer:\n{answer['user_answer']}\n\n"
                f"Correct answer:\n{answer['correct_answer']}\n\n"
                f"{'✅ Correct!' if answer['correct'] else '❌ Incorrect!'}"
            )
            question_result.setObjectName("resultDetail")
            question_result.setWordWrap(True)
            scroll_layout.addWidget(question_result)
            
            if i < len(answers):
                spacer = QWidget()
                spacer.setFixedHeight(10)
                scroll_layout.addWidget(spacer)
        
        scroll_area.setWidget(scroll_content)
        end_layout.addWidget(scroll_area)
        
        restart_button = self.quiz_app.create_button("Start New Quiz", self.quiz_app.restart_quiz)
        end_layout.addWidget(restart_button)
        
        layout.addWidget(end_frame)  

    