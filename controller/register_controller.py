import re 
import json 

class RegisterController:
    
    def __init__(self,view, employee_list_view, main_view,main_dict):
        
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
        
        self.count = 0
        self.main_dict = main_dict
        
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
        name = employee[0].strip()
        email = employee[1].strip()
        phone = employee[2].strip()
        department = employee[3].strip()
        salary = employee[4].strip()
        
        
        #check user take empty field 
        required_fields = [
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
        
        
        if department == "Select Department":
            self.view.show_error(
                f"{field_name} is required."
            )
            return


        if not salary.isdigit():
            self.view.show_error(
                "Salary should contain only numbers."
            )
            return
        
            
        self.count += 1
        new_employee_id = self.count 
            
            
        #Sub dictionary
        employee_dict = {
                "Employee ID": new_employee_id,
                "Name": name,
                "Email": email, 
                "Phone": phone,
                "Department": department ,
                "Salary": salary
            }
            
        key = "Employee " + str(self.count)
      
        new_main_dict = {}
        
        new_main_dict[key] = employee_dict
        new_main_dict.update(self.main_dict)
            
        self.main_dict.clear()
        self.main_dict.update(new_main_dict)
        
        employee_for_table = [
            str(new_employee_id),
            name,
            email,
            phone,
            department,
            salary
        ]
            
        #print on colsole "dumps - > means print on console , s means string "  and "dump - > python dictionary convert in json "
        print(json.dumps(self.main_dict, indent=2))
                
        
        # Prints the received employee data in the terminal.
        # This was useful while testing the signal connection.
        print("Register clicked")
        print(employee_for_table)
        
        
        # Sends the employee data to EmployeeListView.
        # The data entered by the user through the GUI
        # is added as a new row in the employee table.
        self.employee_list_view.add_employee(employee_for_table)
        
        
        