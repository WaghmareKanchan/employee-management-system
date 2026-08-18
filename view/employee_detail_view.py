from PyQt5.QtWidgets import (
    QWidget, 
    QLabel, 
    QPushButton, 
    QVBoxLayout)

from PyQt5.QtCore import pyqtSignal

class EmployeeDetailView(QWidget):
    
    # Signal used to send the employee ID to the Controller
    # when the Delete button is clicked.
    delete_employee_signal = pyqtSignal(object)
    
    def __init__(self):
        super().__init__()
        
        # Stores the currently selected employee.
        self.employee = None
        
        # Creates the Employee Detail page.
        self.setup_ui()
        
    
    def setup_ui(self):
        self.title_label = QLabel("Employee Details")
        
        # Creates labels to display employee information.
        self.id_label = QLabel("ID:")
        self.name_label = QLabel("Name:")
        self.email_label = QLabel("Email:")
        self.phone_label = QLabel("Phone:")
        self.department_label = QLabel("Department:")
        self.salary_label = QLabel("Salary:")
        
        # Creates the Delete button.
        self.delete_button = QPushButton("Delete")
        
        # Connects the Delete button to delete_employee().
        self.delete_button.clicked.connect(
            self.delete_employee 
        )
        
        # Creates a vertical layout.
        layout = QVBoxLayout()
        
        # Adds all employee detail labels to the layout.
        layout.addWidget(self.title_label)
        layout.addWidget(self.id_label)
        layout.addWidget(self.name_label)
        layout.addWidget(self.email_label)
        layout.addWidget(self.phone_label)
        layout.addWidget(self.department_label)
        layout.addWidget(self.salary_label)
        
        # Adds the Delete button.
        layout.addWidget(self.delete_button)
        
        # Applies the layout to the page.
        self.setLayout(layout)
        
    def set_employee_data(self, employee):

        # Stores the selected employee data.
        # This data comes from EmployeeListController.
        self.employee = employee


        # Displays Employee ID.
        self.id_label.setText(
            "ID: " + employee[0]
        )

        # Displays employee name.
        self.name_label.setText(
            "Name: " + employee[1]
        )

        # Displays employee email.
        self.email_label.setText(
            "Email: " + employee[2]
        )

        # Displays employee phone number.
        self.phone_label.setText(
            "Phone: " + employee[3]
        )

        # Displays employee department.
        self.department_label.setText(
            "Department: " + employee[4]
        )

        # Displays employee salary.
        self.salary_label.setText(
            "Salary: " + employee[5]
        )


    def delete_employee(self):

        if self.employee:
            # Sends the selected employee data
            # to EmployeeListController.
            self.delete_employee_signal.emit(
                self.employee
            )

        
        