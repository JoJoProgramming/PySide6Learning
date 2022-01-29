from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PySide6.QtGui import QCloseEvent

class Example(QWidget):
    def __init__(self):
        #super refers to the parent; in this case, super is initializing QWidget
        super().__init__()
        #setup method is placing widgets within the screen and assigning functionality
        self.setup()
    def setup(self):
        quitButton = QPushButton("Force Quit", self)
        quitButton.clicked.connect(QApplication.instance().quit)
        #sizeHint will allow the defined button to scale with the window
        quitButton.resize(quitButton.sizeHint())
        quitButton.move(90,100)

        self.setGeometry(100, 100, 200, 150)
        self.setWindowTitle("Window Example")

        self.show()
    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, "Message", "Are you sure you want to quit?",
        QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
def run():
    app = QApplication([])
    ex = Example()

    app.exec()

if __name__ == '__main__':
    run()