from controller.employee_list_controller import EmployeeListController
from controller.register_controller import RegisterController

class MainController:
    
    def __init__(self, view):
        
        # Stores the MainView object.
        # This gives the controller access to all pages
        # and sidebar buttons.
        self.view = view 
        
        
        # Connects the Register button to open_register_view().
        # When the user clicks Register, the Register page
        # will be displayed on the right side.
        self.view.register_button.clicked.connect(
            self.open_register_view
        )
        
        
        # Connects the Employee List button to open_employee_list().
        # When the user clicks Employee List, the Employee List page
        # will be displayed on the right side.
        self.view.employee_list_button.clicked.connect(
            self.open_employee_list
        )
        
        
        # Creates EmployeeListController.
        #
        # self.view.employee_list_view:
        #   Employee List GUI
        #
        # self.view:
        #   MainView, required for page navigation.
        self.employee_list_controller = EmployeeListController(
            self.view.employee_list_view,
            self.view
        )
        
        
        # Creates RegisterController.
        #
        # self.view.register_view:
        #   Register GUI
        #
        # self.view.employee_list_view:
        #   Employee List GUI, where the newly registered
        #   employee will be displayed.
        #
        # self.view:
        #   MainView, used to navigate to Employee List page
        #   after successful registration.
        self.register_controller = RegisterController(
            self.view.register_view,
            self.view.employee_list_view,
            self.view
        )
        
    def open_register_view(self):
        
        # Changes the currently visible page
        # to the Register page.
        self.view.stack.setCurrentWidget(
            self.view.register_view)
        
    
    def open_employee_list(self):
        
        # Changes the currently visible page
        # to the Employee List page.
        self.view.stack.setCurrentWidget(
            self.view.employee_list_view
        )
        
        
        