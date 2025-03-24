from PyQt5.QtWidgets import *

class Widgets(QWidget):
    def __init__(self, **kwargs):
        super(Widgets, self) .__init__()

        self.vlayout = QVBoxLayout()

        self.hlayout_1 = QHBoxLayout()

        self.L1 = QLabel()
        self.L1.setText("Enter your name")
        self.hlayout_1.addWidget(self.L1)

        self.t1 = QLineEdit()
        self.hlayout_1.addWidget(self.t1)
        self.vlayout.addLayout(self.hlayout_1)

        self.hlayout_2 = QHBoxLayout()

        self.L2 = QLabel()
        self.L2.setText("Enter your school name")
        self.hlayout_2.addWidget(self.L2)

        self.t2 = QLineEdit()
        self.hlayout_2.addWidget(self.t2)
        self.vlayout.addLayout(self.hlayout_2)

        self.btn = QPushButton("Click")
        self.btn.clicked.connect(self.On_click)
        self.vlayout.addWidget(self.btn)

        self.setLayout(self.vlayout)

    def On_click(self):
        print(f"My name is {self.t1.text()} and I have attended {self.t2.text()}")

def window():
    app = QApplication([])

    wig = Widgets()
    wig.show()

    app.exec_()

if __name__=="__main__":
    window()