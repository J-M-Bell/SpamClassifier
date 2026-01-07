import sys
from PyQt6 import QtWidgets
from Controllers.spam_classifier_controller import SpamClassifierController

def main():
    app = QtWidgets.QApplication(sys.argv)

    window = SpamClassifierController()
    window.show()

    app.exec()

if __name__ == "__main__":
    main()