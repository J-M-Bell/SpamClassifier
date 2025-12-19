from PyQt6 import QtWidgets, uic
from widget_ui import Ui_Widget
from spam_model import SpamClassifierModel

class Widget(QtWidgets.QWidget, Ui_Widget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # uic.loadUi("widget.ui", self)
        self.setWindowTitle("Spam Classifier")
        self.submitButton.clicked.connect(self.makePrediction)
        self.resetButton.clicked.connect(self.resetScreen)
        self.model = SpamClassifierModel()

    def makePrediction(self):
        message = self.messageTextBox.toPlainText()
        prediction = self.model.predict(message)
        if prediction == 'ham':
            self.resultLabel.setText("Ham")
        elif prediction == "spam":
            self.resultLabel.setText("Spam")
        else:
            print("error")
    
    def resetScreen(self):
        self.messageTextBox.setText("")
        self.resultLabel.setText("")