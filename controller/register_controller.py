class RegisterController:
    
    def __init__(self,view, employee_list_view, main_view):
        
        # Stores the RegisterView object.
        # This gives the controller access to the Register GUI
        # and its signals.
        self.view = view 
        
        
        # Stores the EmployeeListView object.
        # This is used to add the newly registered employee
        # to the employee table.
        self.employee_list_view = employee_list_view
        
        
        # Stores the MainView object.
        # This is used to navigate from Register page
        # to Employee List page.
        self.main_view = main_view
        
        
        # Connects the RegisterView signal to the controller method.
        #
        # When the user clicks the Register button,
        # RegisterView emits employee data.
        #
        # That data is received by register_employee().
        self.view.register_employee_signal.connect(
            self.register_employee
        )
        
    def register_employee(self,employee):
        
        # Prints the received employee data in the terminal.
        # This was useful while testing the signal connection.
        print("Register clicked")
        print(employee)
        
        
        # Sends the employee data to EmployeeListView.
        # The data entered by the user through the GUI
        # is added as a new row in the employee table.
        self.employee_list_view.add_employee(employee)
        
        
        # After registration, switches the right-side page
        # from RegisterView to EmployeeListView.
        self.main_view.stack.setCurrentWidget(
            self.employee_list_view
        )