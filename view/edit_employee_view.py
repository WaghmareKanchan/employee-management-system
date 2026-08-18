from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QVBoxLayout
)

from PyQt5.QtCore import pyqtSignal


class EditEmployeeView(QWidget):

    # Signal used to send the updated employee data
    # from View to Controller.
    update_employee_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        # Creates the Edit Employee form.
        self.setup_ui()


    def setup_ui(self):

        # Sets the title of the Edit Employee page.
        self.setWindowTitle("Edit Employee")


        # ---------------- Employee ID ----------------

        # Label for Employee ID.
        id_label = QLabel("Employee ID")

        # Employee ID input field.
        self.id_input = QLineEdit()

        # Employee ID should not normally be changed,
        # so it can be made read-only.
        self.id_input.setReadOnly(True)


        # ---------------- Name ----------------

        # Label for employee name.
        name_label = QLabel("Name")

        # Input field for employee name.
        self.name_input = QLineEdit()


        # ---------------- Email ----------------

        # Label for employee email.
        email_label = QLabel("Email")

        # Input field for employee email.
        self.email_input = QLineEdit()


        # ---------------- Phone ----------------

        # Label for employee phone.
        phone_label = QLabel("Phone")

        # Input field for employee phone.
        self.phone_input = QLineEdit()


        # ---------------- Department ----------------

        # Label for employee department.
        department_label = QLabel("Department")

        # Dropdown for selecting department.
        self.department_combo = QComboBox()

        # Adds available department options.
        self.department_combo.addItems([
            "IT",
            "HR",
            "Finance",
            "Marketing"
        ])


        # ---------------- Salary ----------------

        # Label for employee salary.
        salary_label = QLabel("Salary")

        # Input field for employee salary.
        self.salary_input = QLineEdit()


        # ---------------- Update Button ----------------

        # Creates the Update button.
        self.update_button = QPushButton("Update")

        # Calls update_employee() when the button is clicked.
        self.update_button.clicked.connect(
            self.update_employee
        )


        # ---------------- Layout ----------------

        # Creates a vertical layout for the edit form.
        layout = QVBoxLayout()

        # Adds Employee ID field.
        layout.addWidget(id_label)
        layout.addWidget(self.id_input)

        # Adds Name field.
        layout.addWidget(name_label)
        layout.addWidget(self.name_input)

        # Adds Email field.
        layout.addWidget(email_label)
        layout.addWidget(self.email_input)

        # Adds Phone field.
        layout.addWidget(phone_label)
        layout.addWidget(self.phone_input)

        # Adds Department field.
        layout.addWidget(department_label)
        layout.addWidget(self.department_combo)

        # Adds Salary field.
        layout.addWidget(salary_label)
        layout.addWidget(self.salary_input)

        # Adds Update button.
        layout.addWidget(self.update_button)

        # Applies the layout to the EditEmployeeView.
        self.setLayout(layout)


    def set_employee_data(self, employee):

        # Stores the employee that is being edited.
        self.employee = employee


        # Displays the existing Employee ID.
        self.id_input.setText(employee[0])

        # Displays the existing name.
        self.name_input.setText(employee[1])

        # Displays the existing email.
        self.email_input.setText(employee[2])

        # Displays the existing phone number.
        self.phone_input.setText(employee[3])

        # Selects the existing department in the dropdown.
        index = self.department_combo.findText(employee[4])

        if index >= 0:
            self.department_combo.setCurrentIndex(index)

        # Displays the existing salary.
        self.salary_input.setText(employee[5])


    def update_employee(self):

        # Collects the updated values entered by the user.
        employee = [
            self.id_input.text(),
            self.name_input.text(),
            self.email_input.text(),
            self.phone_input.text(),
            self.department_combo.currentText(),
            self.salary_input.text()
        ]

        # Sends the updated employee data
        # to EmployeeListController.
        self.update_employee_signal.emit(employee)