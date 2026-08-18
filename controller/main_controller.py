from controller.employee_list_controller import EmployeeListController
from controller.register_controller import RegisterController


class MainController:

    def __init__(self, view):

        # Stores the MainView object.
        self.view = view


        # ---------------- Button Connections ----------------

        # Register button opens Register page.
        self.view.register_button.clicked.connect(
            self.open_register_view
        )


        # Employee List button opens Employee List page.
        self.view.employee_list_button.clicked.connect(
            self.open_employee_list
        )


        # ---------------- Controllers ----------------

        # Creates EmployeeListController.
        self.employee_list_controller = EmployeeListController(
            self.view.employee_list_view,
            self.view
        )


        # Creates RegisterController.
        self.register_controller = RegisterController(
            self.view.register_view,
            self.view.employee_list_view,
            self.view
        )


    # ---------------- Register Page ----------------

    def open_register_view(self):

        # Makes Register button active.
        self.view.register_button.setChecked(
            True
        )

        # Makes Employee List button inactive.
        self.view.employee_list_button.setChecked(
            False
        )


        # Opens Register page.
        self.view.stack.setCurrentWidget(
            self.view.register_view
        )


    # ---------------- Employee List Page ----------------

    def open_employee_list(self):

        # Makes Employee List button active.
        self.view.employee_list_button.setChecked(
            True
        )

        # Makes Register button inactive.
        self.view.register_button.setChecked(
            False
        )


        # Opens Employee List page.
        self.view.stack.setCurrentWidget(
            self.view.employee_list_view
        )