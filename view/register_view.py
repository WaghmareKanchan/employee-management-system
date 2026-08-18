from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QVBoxLayout
)

from PyQt5.QtCore import pyqtSignal


class RegisterView(QWidget):

    # Signal is used to send employee data from View to Controller.
    # object allows us to send the complete employee data together.
    register_employee_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        # Calls the method that creates and arranges
        # all the registration form widgets.
        self.setup_ui()

    def setup_ui(self):

        # Sets the title of the Register page.
        self.setWindowTitle("Register Employee")


        # ---------------- Employee ID ----------------

        # Creates a label for Employee ID.
        id_label = QLabel("Employee ID")

        # Creates an input box where the user enters Employee ID.
        self.id_input = QLineEdit()


        # ---------------- Name ----------------

        # Creates a label for employee name.
        name_label = QLabel("Name")

        # Creates an input box for employee name.
        self.name_input = QLineEdit()


        # ---------------- Email ----------------

        # Creates a label for employee email.
        email_label = QLabel("Email")

        # Creates an input box for employee email.
        self.email_input = QLineEdit()


        # ---------------- Phone ----------------

        # Creates a label for employee phone number.
        phone_label = QLabel("Phone")

        # Creates an input box for employee phone number.
        self.phone_input = QLineEdit()


        # ---------------- Department ----------------

        # Creates a label for department.
        department_label = QLabel("Department")

        # QComboBox provides a dropdown list for selecting
        # the employee's department.
        self.department_combo = QComboBox()

        # Adds department options to the dropdown.
        self.department_combo.addItems([
            "IT",
            "HR",
            "Finance"
        ])


        # ---------------- Salary ----------------

        # Creates a label for salary.
        salary_label = QLabel("Salary")

        # Creates an input box for employee salary.
        self.salary_input = QLineEdit()


        # ---------------- Register Button ----------------

        # Creates the Register button.
        self.register_button = QPushButton("Register")

        # Connects the button click to register_employee().
        # When the user clicks Register, the entered form data
        # will be collected.
        self.register_button.clicked.connect(
            self.register_employee
        )


        # ---------------- Layout ----------------

        # Creates a vertical layout for the registration form.
        layout = QVBoxLayout()

        # Adds Employee ID label and input field.
        layout.addWidget(id_label)
        layout.addWidget(self.id_input)

        # Adds Name label and input field.
        layout.addWidget(name_label)
        layout.addWidget(self.name_input)

        # Adds Email label and input field.
        layout.addWidget(email_label)
        layout.addWidget(self.email_input)

        # Adds Phone label and input field.
        layout.addWidget(phone_label)
        layout.addWidget(self.phone_input)

        # Adds Department label and dropdown.
        layout.addWidget(department_label)
        layout.addWidget(self.department_combo)

        # Adds Salary label and input field.
        layout.addWidget(salary_label)
        layout.addWidget(self.salary_input)

        # Adds Register button at the bottom of the form.
        layout.addWidget(self.register_button)

        # Applies the layout to the RegisterView.
        self.setLayout(layout)


    def register_employee(self):

        # Collects the data entered by the user in the GUI.
        employee = [
            self.id_input.text(),
            self.name_input.text(),
            self.email_input.text(),
            self.phone_input.text(),
            self.department_combo.currentText(),
            self.salary_input.text()
        ]

        # Sends the employee data to RegisterController.
        # The View does not decide what to do with the data;
        # it only collects and emits it.
        self.register_employee_signal.emit(employee)