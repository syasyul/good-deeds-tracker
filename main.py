import sys
from PyQt5.QtWidgets import QApplication, QStackedWidget, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

from login_screen import LoginScreen
from input_screen import InputScreen
from result_screen import ResultScreen

class MainMenu(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack
        layout = QVBoxLayout()

        title = QLabel("GOOD DEEDS TRACKER")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 36px; font-weight: bold; color: #733c15;")

        subtitle1 = QLabel("Small Kindness, Big Impact✨")
        subtitle1.setAlignment(Qt.AlignCenter)
        subtitle1.setStyleSheet("font-size: 18px; color: #8B4513;")

        subtitle2 = QLabel("Selamat Datang di GOOD DEEDS TRACKER! \nAplikasi ini dibuat untuk membantu kamu mencatat kebaikan kecil \nyang kamu lakukan setiap hari.Walaupun sederhana, kebaikan kecil bisa memberi \ndampak besar untuk diri sendiri, orang lain, dan lingkungan. ")
        subtitle2.setAlignment(Qt.AlignCenter)
        subtitle2.setStyleSheet("font-size: 18px; color: #8B4513;")
        
        start_btn = QPushButton("🚀Start Your Kindness Journey")
        start_btn.setStyleSheet("""
            QPushButton {
                background-color: #ab5b35;
                color: white;
                border: none;
                padding: 15px 30px;
                font-size: 18px;
                font-weight: bold;
                border-radius: 25px;
            }
            QPushButton:hover {
                background-color: #75432b;
            }
            QPushButton:pressed {
                background-color: #4f2815;
            }
        """)
        start_btn.clicked.connect(self.start)
        layout.addStretch(1)
        layout.addWidget(title)
        layout.addSpacing(20)
        layout.addWidget(subtitle1)
        layout.addSpacing(10)
        layout.addWidget(subtitle2)
        layout.addSpacing(40)
        layout.addWidget(start_btn, alignment=Qt.AlignCenter)
        layout.addStretch(1)
        self.setLayout(layout)
    def start(self):
        self.stack.setCurrentWidget(self.stack.login)

class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()
        self.total_inputs = 0
        self.menu = MainMenu(self)
        self.login = LoginScreen(self)
        self.input = InputScreen(self)
        self.result = ResultScreen(self)
        self.addWidget(self.menu)
        self.addWidget(self.login)
        self.addWidget(self.input)
        self.addWidget(self.result)
        self.setFixedSize(900, 600)
        self.setWindowTitle("Good Deeds Tracker")
        self.setStyleSheet("background-color: #FFF8DC;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())