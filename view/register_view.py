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


class RegisterView(QWidget):

    # Sends employee data from View to Controller.
    register_employee_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        # Creates the registration form.
        self.setup_ui()


    def setup_ui(self):

        # Sets the window title.
        self.setWindowTitle(
            "Register Employee"
        )


        # ---------------- Title ----------------

        title_label = QLabel(
            "Register Employee"
        )

        title_label.setObjectName(
            "titleLabel"
        )


        # ---------------- Employee ID ----------------

        id_label = QLabel(
            "Employee ID"
        )

        self.id_input = QLineEdit()

        self.id_input.setPlaceholderText(
            "Enter employee ID"
        )


        # ---------------- Name ----------------

        name_label = QLabel(
            "Name"
        )

        self.name_input = QLineEdit()

        self.name_input.setPlaceholderText(
            "Enter employee name"
        )


        # ---------------- Email ----------------

        email_label = QLabel(
            "Email"
        )

        self.email_input = QLineEdit()

        self.email_input.setPlaceholderText(
            "Enter email address"
        )


        # ---------------- Phone ----------------

        phone_label = QLabel(
            "Phone"
        )

        self.phone_input = QLineEdit()

        self.phone_input.setPlaceholderText(
            "Enter 10 digit phone number"
        )


        # ---------------- Department ----------------

        department_label = QLabel(
            "Department"
        )

        self.department_combo = QComboBox()

        self.department_combo.addItems([
            "IT",
            "HR",
            "Finance",
            "Marketing"
        ])


        # ---------------- Salary ----------------

        salary_label = QLabel(
            "Salary"
        )

        self.salary_input = QLineEdit()

        self.salary_input.setPlaceholderText(
            "Enter salary"
        )


        # ---------------- Error Message ----------------

        self.error_label = QLabel("")

        self.error_label.setObjectName(
            "errorLabel"
        )


        # ---------------- Buttons ----------------

        self.register_button = QPushButton(
            "Register"
        )

        self.register_button.setObjectName(
            "registerButton"
        )


        self.clear_button = QPushButton(
            "Clear"
        )

        self.clear_button.setObjectName(
            "clearButton"
        )


        # Connects Register button.
        self.register_button.clicked.connect(
            self.register_employee
        )


        # Connects Clear button.
        self.clear_button.clicked.connect(
            self.clear_form
        )


        # ---------------- Form Fields ----------------

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

        # Outer spacing.
        layout.setContentsMargins(
            80,
            40,
            80,
            40
        )

        # Space between widgets.
        layout.setSpacing(
            10
        )


        # Adds title.
        layout.addWidget(
            title_label
        )

        layout.addSpacing(
            15
        )


        # Adds all form fields.
        #
        # Same operation is repeated,
        # so for loop is suitable here.
        for label, field in fields:

            layout.addWidget(
                label
            )

            layout.addWidget(
                field
            )


        # Adds error message.
        layout.addWidget(
            self.error_label
        )

        layout.addSpacing(
            10
        )


        # ---------------- Button Layout ----------------

        button_layout = QHBoxLayout()

        button_layout.setSpacing(
            10
        )


        button_layout.addWidget(
            self.register_button
        )

        button_layout.addWidget(
            self.clear_button
        )


        layout.addLayout(
            button_layout
        )


        # Applies layout.
        self.setLayout(
            layout
        )


        # ---------------- QSS ----------------

        self.setStyleSheet("""

        QWidget {
            background-color: #f5f7fa;
            font-family: Arial;
            font-size: 14px;
            
        }

        QLabel {
            color: #333333;
            font-weight: bold;
        }


        #titleLabel {
            font-size: 24px;
            font-weight: bold;
            color: #1f2937;
        }


        QLineEdit,
        QComboBox {
            background-color: white;
            border: 1px solid #d1d5db;
            border-radius: 6px;
            padding: 9px;
            min-height: 18px;
        }


        QLineEdit:focus,
        QComboBox:focus {
            border: 2px solid #2563eb;
        }


        #registerButton {
            background-color: #2563eb;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 10px;
            font-weight: bold;
        }


        #registerButton:hover {
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


    def register_employee(self):

        # Collects all form data.
        employee = [
            self.id_input.text().strip(),
            self.name_input.text().strip(),
            self.email_input.text().strip(),
            self.phone_input.text().strip(),
            self.department_combo.currentText(),
            self.salary_input.text().strip()
        ]


        # ---------------- Required Fields ----------------

        required_fields = [
            ("Employee ID", employee[0]),
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


        # ---------------- Employee ID Validation ----------------

        if not employee[0].isdigit():

            self.show_error(
                "Employee ID should contain only numbers."
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


        # ---------------- Successful Registration ----------------

        # Sends valid employee data to Controller.
        self.register_employee_signal.emit(
            employee
        )


        # Immediately clears the form
        # after successful registration.
        self.clear_form()


    def clear_form(self):

        # Stores all QLineEdit fields.
        fields = [
            self.id_input,
            self.name_input,
            self.email_input,
            self.phone_input,
            self.salary_input
        ]


        # Same clear operation for all fields,
        # so for loop is suitable here.
        for field in fields:

            field.clear()


        # Resets department.
        self.department_combo.setCurrentIndex(
            0
        )


        # Clears error message.
        self.clear_error()


    def show_error(self, message):

        # Displays validation error.
        self.error_label.setText(
            message
        )


    def clear_error(self):

        # Clears error message.
        self.error_label.setText("")