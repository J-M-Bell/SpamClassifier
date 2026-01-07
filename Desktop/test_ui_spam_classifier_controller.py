from PyQt6.QtCore import Qt
from Controllers.spam_classifier_controller import SpamClassifierController

def test_ui_spam_message(qtbot):
    # 1. Instantiate and show your application's main window
    window = SpamClassifierController()
    qtbot.addWidget(window)
    window.show()
    qtbot.waitExposed(window)

    # 2. Simulate user interactions using qtbot methods
    qtbot.keyClicks(window.messageTextBox, "Lol your always so convincing.")

    # Example: Click a button named 'submit_button'
    qtbot.mouseClick(window.submitButton, Qt.MouseButton.LeftButton)

    # 3. Add assertions to verify the application's state
    assert window.resultLabel.text() == "Ham"

# if __name__ == '__main__':
#     test_my_app_flow()   