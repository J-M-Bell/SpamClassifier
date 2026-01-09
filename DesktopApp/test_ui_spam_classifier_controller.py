from PyQt6.QtCore import Qt
from Controllers.spam_classifier_controller import SpamClassifierController

def test_ui_spam_message(qtbot):
    """
    A ui test to test if the right classification prediction appears
    depending on the message provided
    
    :param qtbot: qtbot - automates the test process
    """
    
    # Instantiate and show main window
    window = SpamClassifierController()
    qtbot.addWidget(window)
    window.show()
    qtbot.waitExposed(window)

    # simulate user interactions using qtbot methods
    qtbot.keyClicks(window.messageTextBox, "Lol your always so convincing.")
    qtbot.mouseClick(window.submitButton, Qt.MouseButton.LeftButton)

    # verify the application's state
    assert window.resultLabel.text() == "Ham"
