import sys

from PyQt5.QtWidgets import QApplication 

from view.main_view import MainView 
from controller.main_controller import MainController 

# Creates the PyQt application object.
# sys.argv contains the command-line arguments passed to the application.
app = QApplication(sys.argv)


# Creates the main GUI window.
# MainView contains the complete UI and different pages.
window = MainView() 


# Creates the MainController.
# Controller connects the GUI buttons and views with the required logic.
controller = MainController(window)


# Displays the main window on the screen.
window.show() 


# Starts the PyQt event loop.
# It keeps the application running and listens for user actions
# such as button clicks.
sys.exit(app.exec_())

