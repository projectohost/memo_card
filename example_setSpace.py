from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        layout.setSpacing(5)



if __name__ == "__main__":
    app = QApplication([])
    app.setStyleSheet("QWidget{font-size: 55px}")
    widget = MyWidget()
    widget.show()
    app.exec_()
