from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt

class InputScreen(QWidget):
    def __init__(self, stack):
        super().__init__()
        self.stack = stack

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(30,10,30,10)
        self.layout.setSpacing(0)

        label_layout = QVBoxLayout()

        self.title = QLabel()
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFixedHeight(50)
        self.title.setStyleSheet("font-size:36px; font-weight:bold; color:#733c15; padding:0; margin:0;")

        self.subtitle1 = QLabel()
        self.subtitle1.setAlignment(Qt.AlignCenter)
        self.subtitle1.setFixedHeight(40)
        self.subtitle1.setStyleSheet("font-size:16px; color:#8B4513; padding:0; margin:0;")

        self.subtitle2 = QLabel()
        self.subtitle2.setAlignment(Qt.AlignCenter)
        self.subtitle2.setFixedHeight(40)
        self.subtitle2.setStyleSheet("font-size:16px; color:#8B4513; padding:0; margin:8;")

        label_layout.addWidget(self.title)
        label_layout.addWidget(self.subtitle1)
        label_layout.addWidget(self.subtitle2)

        self.layout.addLayout(label_layout)

        self.inputs = []

        next_layout = QHBoxLayout()
        next_layout.addStretch()

        self.next = QPushButton("Next")
        self.next.clicked.connect(self.next_screen)
        self.next.setStyleSheet("""
            QPushButton{
                background:#ab5b35;
                color:white;
                border:none;
                padding:15px 30px;
                font-size:18px;
                font-weight:bold;
                border-radius:25px;
            }
            QPushButton:hover{
                background:#75432b;
            }
            QPushButton:pressed{
                background:#4f2815;
            }
        """)
        next_layout.addWidget(self.next)
        self.layout.addLayout(next_layout)
        self.setLayout(self.layout)


    def setup(self, name, level, screen):
        self.name = name
        self.level = level
        self.screen = screen
        if level == 1:
            if screen == 3:
                self.title.setText("💙Kebaikan untuk Diri Sendiri")
                self.subtitle1.setText(f"Halo {name}! Kadang kita terlalu sibuk sampai lupa \nmemperhatikan diri sendiri.")
                self.subtitle2.setText("Tuliskan kebaikan yang kamu lakukan untuk diri sendiri hari ini!")
            elif screen == 4:
                self.title.setText("🤝Kebaikan untuk Orang Lain")
                self.subtitle1.setText(f"Halo {name}! Hal kecil yang kamu lakukan bisa berarti besar untuk orang lain.")
                self.subtitle2.setText("Tuliskan kebaikan yang kamu lakukan untuk orang lain hari ini!")
            elif screen == 5:
                self.title.setText("🌱Kebaikan untuk Lingkungan")
                self.subtitle1.setText(f"Halo {name}! Hal kecil yang kamu lakukan bisa memberi dampak baik untuk lingkungan sekitar.")
                self.subtitle2.setText("Tuliskan kebaikan yang kamu lakukan untuk lingkungan sekitarmu hari ini!")
        elif level == 3:
            if screen == 3:
                self.title.setText("💙Kebaikan untuk Diri Sendiri")
                self.subtitle1.setText(f"Halo {name}! Kadang kita terlalu sibuk sampai lupa \nmemperhatikan diri sendiri.")
                self.subtitle2.setText("Tuliskan kebaikan yang kamu lakukan untuk diri sendiri hari ini!")
            elif screen == 4:
                self.title.setText("🤝Kebaikan untuk Orang Lain")
                self.subtitle1.setText(f"Halo {name}! Hal kecil yang kamu lakukan bisa berarti besar untuk orang lain.")
                self.subtitle2.setText("Tuliskan kebaikan yang kamu lakukan untuk orang lain hari ini!")
            elif screen == 5:
                self.title.setText("🌱Kebaikan untuk Lingkungan")
                self.subtitle1.setText(f"Halo {name}! Hal kecil yang kamu lakukan bisa memberi dampak baik untuk lingkungan sekitar.")
                self.subtitle2.setText("Tuliskan kebaikan yang kamu lakukan untuk lingkungan sekitarmu hari ini!")
        elif level == 5:
            if screen == 3:
                self.title.setText("💙Kebaikan untuk Diri Sendiri")
                self.subtitle1.setText(f"Halo {name}! Kadang kita terlalu sibuk sampai lupa \nmemperhatikan diri sendiri.")
                self.subtitle2.setText("Tuliskan kebaikan yang kamu lakukan untuk diri sendiri hari ini!")
            elif screen == 4:
                self.title.setText("🤝Kebaikan untuk Orang Lain")
                self.subtitle1.setText(f"Halo {name}! Hal kecil yang kamu lakukan bisa berarti besar untuk orang lain.")
                self.subtitle2.setText("Tuliskan kebaikan yang kamu lakukan untuk orang lain hari ini!")
            elif screen == 5:
                self.title.setText("🌱Kebaikan untuk Lingkungan")
                self.subtitle1.setText(f"Halo {name}! Hal kecil yang kamu lakukan bisa memberi dampak baik untuk lingkungan sekitar.")
                self.subtitle2.setText("Tuliskan kebaikan yang kamu lakukan untuk lingkungan sekitarmu hari ini!")
        for i in self.inputs:
            self.layout.removeWidget(i)
            i.deleteLater()
        self.inputs = []
        for i in range(level):
            inp = QLineEdit()
            inp.setPlaceholderText(f"Kebaikan {i+1}")
            inp.setStyleSheet("""
                QLineEdit{
                    padding:12px;
                    font-size:14px;
                    border:2px solid #733c15;
                    border-radius:10px;
                    background:#ecf0f1;
                    margin:2px 0;
                }
                QLineEdit:focus{
                    border-color:#733c15;
                    background:white;
                }
            """)
            self.layout.insertWidget(self.layout.count()-1, inp)
            self.inputs.append(inp)

    def next_screen(self):
        filled = 0
        for i in self.inputs:
            if i.text() != "":
                filled += 1
        self.stack.total_inputs += filled
        if self.screen < 5:
            self.setup(self.name, self.level, self.screen + 1)
        else:
            points = self.stack.total_inputs * 10
            self.stack.result.show_result(self.name, points)
            self.stack.setCurrentWidget(self.stack.result)