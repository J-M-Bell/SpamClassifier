from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from Models.spam_classifier_model import SpamClassifierModel
import resources

class SpamClassifierController(QWidget):
    """
    A class that acts as the Controller for
    the spam_classifier_view
    """
    def __init__(self):
        """
        constructor for SpamClassifierController
        
        :param self: SpamClassifierController - The SpamClassifierController object
        """

        # Start up window
        super().__init__()
        uic.loadUi("./Desktop/Views/spam_classifier_view.ui", self)
        self.setWindowTitle("Spam Classifier")

        #Instantiate spam model
        self.model = SpamClassifierModel()

        #Assign functionalities to UI elements
        self.submitButton.clicked.connect(self.makePrediction)
        self.resetButton.clicked.connect(self.resetScreen)

    def makePrediction(self):
        """
        ui function to change the text for the 
        resultLabel between spam or ham
        
        :param self: SpamClassifierController - The SpamClassifierController object
        """
        
        # Change label to ham or spam depending on prediction
        message = self.messageTextBox.toPlainText()
        prediction = self.model.predict(message)
        if prediction == 'ham':
            self.resultLabel.setText("Ham")
        elif prediction == "spam":
            self.resultLabel.setText("Spam")
        else:
            print("error")
    
    def resetScreen(self):
        """
        ui function to reset the screen after the
        Reset button has been pressed
        
        :param self: SpamClassifierController - The SpamClassifierController object
        """

        # Reset text box and label
        self.messageTextBox.setText("")
        self.resultLabel.setText("")