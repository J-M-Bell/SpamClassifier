from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from Models.spam_classifier_model import SpamClassifierModel
import resources

class SpamClassifierController(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("./Desktop/Views/spam_classifier_view.ui", self)
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