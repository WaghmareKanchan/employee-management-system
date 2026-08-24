from controller.employee_list_controller import EmployeeListController
from controller.register_controller import RegisterController
from controller.dashboard_controller import DashboardController

class MainController:

    def __init__(self, view, login_view,dashboard_view):

        # Stores the MainView object.
        self.view = view
        self.login_view = login_view
        
        # Stores DashboardView.
        self.dashboard_view = dashboard_view


        # ---------------- Button Connections ----------------

        # Register button opens Register page.
        self.view.register_button.clicked.connect(
            self.open_register_view
        )


        # Employee List button opens Employee List page.
        self.view.employee_list_button.clicked.connect(
            self.open_employee_list
        )
        
        self.view.logout_button.clicked.connect(
            self.logout
        )

        #shared employee dictionary 
        self.main_dict = {}

        # ---------------- Controllers ----------------

        # Dashboard Controller.
        self.dashboard_controller = DashboardController(
            self.dashboard_view,
            self.main_dict,
            self.view
           
        )

        # Creates EmployeeListController.
        self.employee_list_controller = EmployeeListController(
            self.view.employee_list_view,
            self.view,
            self.main_dict,
            self.dashboard_controller
        )
        

        # Creates RegisterController.
        self.register_controller = RegisterController(
            self.view.register_view,
            self.view.employee_list_view,
            self.view,
            self.main_dict,
            self.dashboard_controller
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
        
        
         # ---------------- Logout ----------------

    def logout(self):

        self.view.hide()

        self.login_view.username.clear()

        self.login_view.password.clear()

        self.login_view.show()