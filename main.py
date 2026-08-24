import sys

from PyQt5.QtWidgets import QApplication


# ---------------- Views ----------------

from view.login_view import LoginView

from view.main_view import MainView

from view.dashboard_view import DashboardView


# ---------------- Controllers ----------------

from controller.login_controller import LoginController

from controller.main_controller import MainController


# ---------------- Application ----------------

app = QApplication(
    sys.argv
)


# ---------------- Create Views ----------------

login_view = LoginView()

main_view = MainView()

dashboard_view = DashboardView()


# ---------------- Create Controllers ----------------

login_controller = LoginController(
    login_view,
    main_view,
    dashboard_view
)


main_controller = MainController(
    main_view,
    login_view,
    dashboard_view,
    
)


# ---------------- Start Application ----------------

login_view.show()


# ---------------- Event Loop ----------------

sys.exit(
    app.exec_()
)