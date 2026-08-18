import re

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)

from PyQt5.QtCore import pyqtSignal


class EditEmployeeView(QWidget):

    # Signal used to send updated employee data
    # from View to EmployeeListController.
    update_employee_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        # Creates the Edit Employee UI.
        self.setup_ui()

    def setup_ui(self):

        # Sets the page title.
        self.setWindowTitle("Edit Employee")


        # ---------------- Title ----------------

        title_label = QLabel("Edit Employee")

        # Used by QSS for title styling.
        title_label.setObjectName(
            "titleLabel"
        )


        # ---------------- Employee ID ----------------

        id_label = QLabel("Employee ID")

        self.id_input = QLineEdit()

        # Employee ID should not be changed.
        self.id_input.setReadOnly(True)

        self.id_input.setPlaceholderText(
            "Employee ID"
        )


        # ---------------- Name ----------------

        name_label = QLabel("Name")

        self.name_input = QLineEdit()

        self.name_input.setPlaceholderText(
            "Enter employee name"
        )


        # ---------------- Email ----------------

        email_label = QLabel("Email")

        self.email_input = QLineEdit()

        self.email_input.setPlaceholderText(
            "Enter email address"
        )


        # ---------------- Phone ----------------

        phone_label = QLabel("Phone")

        self.phone_input = QLineEdit()

        self.phone_input.setPlaceholderText(
            "Enter 10 digit phone number"
        )


        # ---------------- Department ----------------

        department_label = QLabel("Department")

        self.department_combo = QComboBox()

        self.department_combo.addItems([
            "IT",
            "HR",
            "Finance",
            "Marketing"
        ])


        # ---------------- Salary ----------------

        salary_label = QLabel("Salary")

        self.salary_input = QLineEdit()

        self.salary_input.setPlaceholderText(
            "Enter salary"
        )


        # ---------------- Error Label ----------------

        self.error_label = QLabel("")

        self.error_label.setObjectName(
            "errorLabel"
        )


        # ---------------- Buttons ----------------

        self.update_button = QPushButton(
            "Update"
        )

        self.update_button.setObjectName(
            "updateButton"
        )


        self.clear_button = QPushButton(
            "Clear"
        )

        self.clear_button.setObjectName(
            "clearButton"
        )


        # Connect Update button.
        self.update_button.clicked.connect(
            self.update_employee
        )


        # Connect Clear button.
        self.clear_button.clicked.connect(
            self.clear_form
        )


        # ---------------- Field List ----------------

        # Stores label + input pairs.
        #
        # All fields have the same layout:
        #
        # Label
        # Input
        #
        # So we can use a for loop.
        fields = [
            (id_label, self.id_input),
            (name_label, self.name_input),
            (email_label, self.email_input),
            (phone_label, self.phone_input),
            (department_label, self.department_combo),
            (salary_label, self.salary_input)
        ]


        # ---------------- Main Layout ----------------

        layout = QVBoxLayout()


        # Adds space around the form.
        layout.setContentsMargins(
            80,
            40,
            80,
            40
        )


        # Space between widgets.
        layout.setSpacing(10)


        # Adds title.
        layout.addWidget(
            title_label
        )

        layout.addSpacing(15)


        # Adds all label + input pairs.
        for label, field in fields:

            layout.addWidget(label)
            layout.addWidget(field)


        # Adds small space before error.
        layout.addSpacing(5)


        # Adds error message label.
        layout.addWidget(
            self.error_label
        )


        # Adds space before buttons.
        layout.addSpacing(10)


        # ---------------- Button Layout ----------------

        button_layout = QHBoxLayout()

        button_layout.setSpacing(10)

        button_layout.addWidget(
            self.update_button
        )

        button_layout.addWidget(
            self.clear_button
        )


        # Adds button layout to main layout.
        layout.addLayout(
            button_layout
        )


        # Applies main layout.
        self.setLayout(
            layout
        )


        # ---------------- QSS Styling ----------------

        self.setStyleSheet("""

        QWidget {
            background-color: #f5f7fa;
            font-size: 14px;
        }


        #titleLabel {
            font-size: 24px;
            font-weight: bold;
            color: #1f2937;
            padding-bottom: 5px;
        }


        QLineEdit,
        QComboBox {

            background-color: white;

            border: 1px solid #d1d5db;

            border-radius: 6px;

            padding: 9px;
        }


        QLineEdit:focus,
        QComboBox:focus {

            border: 2px solid #2563eb;
        }


        QLineEdit:read-only {

            background-color: #e5e7eb;

            color: #6b7280;
        }


        #updateButton {

            background-color: #2563eb;

            color: white;

            border: none;

            border-radius: 6px;

            padding: 10px;

            font-weight: bold;
        }


        #updateButton:hover {

            background-color: #1d4ed8;
        }


        #clearButton {

            background-color: #e5e7eb;

            color: #374151;

            border: none;

            border-radius: 6px;

            padding: 10px;

            font-weight: bold;
        }


        #clearButton:hover {

            background-color: #d1d5db;
        }


        #errorLabel {

            color: #dc2626;

            font-weight: bold;
        }

        """)


    def set_employee_data(self, employee):

        # Stores employee currently being edited.
        self.employee = employee


        # Employee ID.
        self.id_input.setText(
            employee[0]
        )


        # Employee name.
        self.name_input.setText(
            employee[1]
        )


        # Employee email.
        self.email_input.setText(
            employee[2]
        )


        # Employee phone.
        self.phone_input.setText(
            employee[3]
        )


        # Finds existing department.
        index = self.department_combo.findText(
            employee[4]
        )


        # Selects department if found.
        if index >= 0:

            self.department_combo.setCurrentIndex(
                index
            )


        # Employee salary.
        self.salary_input.setText(
            employee[5]
        )


        # Removes any previous error.
        self.clear_error()


    def update_employee(self):

        # Collects updated employee data.
        employee = [
            self.id_input.text().strip(),
            self.name_input.text().strip(),
            self.email_input.text().strip(),
            self.phone_input.text().strip(),
            self.department_combo.currentText(),
            self.salary_input.text().strip()
        ]


        # ---------------- Required Field Validation ----------------

        required_fields = [
            ("Name", employee[1]),
            ("Email", employee[2]),
            ("Phone", employee[3]),
            ("Salary", employee[5])
        ]


        # Checks all required fields.
        for field_name, value in required_fields:

            if not value:

                self.show_error(
                    f"{field_name} is required."
                )

                return


        # ---------------- Name Validation ----------------

        if not re.fullmatch(
            r"[A-Za-z ]+",
            employee[1]
        ):

            self.show_error(
                "Name should contain only letters."
            )

            return


        # ---------------- Email Validation ----------------

        email_pattern = (
            r"^[\w\.-]+@[\w\.-]+\.\w+$"
        )


        if not re.fullmatch(
            email_pattern,
            employee[2]
        ):

            self.show_error(
                "Please enter a valid email address."
            )

            return


        # ---------------- Phone Validation ----------------

        if not employee[3].isdigit():

            self.show_error(
                "Phone number should contain only digits."
            )

            return


        if len(employee[3]) != 10:

            self.show_error(
                "Phone number must contain exactly 10 digits."
            )

            return


        # ---------------- Salary Validation ----------------

        if not employee[5].isdigit():

            self.show_error(
                "Salary should contain only numbers."
            )

            return


        # ---------------- Send Updated Data ----------------

        self.update_employee_signal.emit(
            employee
        )


    def clear_form(self):

        # Employee ID is not cleared
        # because it is read-only.

        self.name_input.clear()

        self.email_input.clear()

        self.phone_input.clear()

        self.salary_input.clear()


        # Resets department.
        self.department_combo.setCurrentIndex(
            0
        )


        # Removes error message.
        self.clear_error()


    def show_error(self, message):

        # Displays validation error.
        self.error_label.setText(
            message
        )


    def clear_error(self):

        # Removes validation error.
        self.error_label.setText("")