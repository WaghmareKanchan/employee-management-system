import re 
import json 

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
        
        
        self.main_dict = {}
        self.count = 0
        
        
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
        
        #Gets employee data from the list 
        employee_id = employee[0].strip()
        name = employee[1].strip()
        email = employee[2].strip()
        phone = employee[3].strip()
        department = employee[4].strip()
        salary = employee[5].strip()
        
        
        #check user take empty field 
        required_fields = [
            ("Employee ID", employee_id),
            ("Name", name),
            ("Email", email),
            ("Phone", phone),
            ("Salary", salary)
        ]

        for field_name, value in required_fields:

            if not value:
                self.view.show_error(
                    f"{field_name} is required."
                )
                return


        if not re.fullmatch(r"[A-Za-z ]+", name):
            self.view.show_error(
                "Name should contain only letters."
            )
            return


        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.fullmatch(email_pattern, email):
            self.view.show_error(
                "Please enter a valid email address."
            )
            return


        if not phone.isdigit():
            self.view.show_error(
                "Phone number should contain only digits."
            )
            return


        if len(phone) != 10:
            self.view.show_error(
                "Phone number must contain exactly 10 digits."
            )
            return
        
        
        if not department or department == "Select Department":
            self.view.show_error(
                f"{field_name} is required."
            )
            return


        if not salary.isdigit():
            self.view.show_error(
                "Salary should contain only numbers."
            )
            return
        
        
        #Duplicate ID check
        for key in self.main_dict:
            if self.main_dict[key]["Employee ID"] == employee_id:
                self.view.show_error("Employee ID already exists.")
                return 
            
        self.count += 1
            
            
        #Sub dictionary
        employee_dict = {
                "Employee ID": employee_id,
                "Name": name,
                "Email": email, 
                "Phone": phone,
                "Department": department ,
                "Salary": salary
            }
            
        self.main_dict["Employee " + str(self.count)] = employee_dict 
            
            
        #print on colsole "dumps - > means print on console , s means string "  and "dump - > python dictionary convert in json "
        print(json.dumps(self.main_dict, indent=2))
                
        
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
        # self.main_view.stack.setCurrentWidget(
        #     self.employee_list_view
        # ) 