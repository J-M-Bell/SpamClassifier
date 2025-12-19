from PyQt6 import QtWidgets

from widget_ui import Ui_Widget

class Widget(QtWidgets.QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Spam Classifier")
        self.submitButton.clicked.connect(self.onClick)

    def onClick(self):
        print("Hello World")