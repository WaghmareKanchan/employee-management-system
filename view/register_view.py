import re

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame
)

from PyQt5.QtCore import pyqtSignal, Qt


class RegisterView(QWidget):

    # Sends employee data from View to Controller.
    register_employee_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        # ---------------- Window ----------------

        self.setWindowTitle(
            "Register Employee"
        )

        # ---------------- Main Layout ----------------

        main_layout = QVBoxLayout()

        main_layout.setContentsMargins(
            0,
            20,
            0,
            20
        )

        # ---------------- Card ----------------

        card = QFrame()

        card.setObjectName(
            "registerCard"
        )

        card.setFixedWidth(
            500
        )

        # ---------------- Card Layout ----------------

        form_layout = QVBoxLayout()

        form_layout.setContentsMargins(
            35,
            30,
            35,
            30
        )

        form_layout.setSpacing(
            12
        )

        # ---------------- Title ----------------

        title_label = QLabel(
            "Register Employee"
        )

        title_label.setObjectName(
            "titleLabel"
        )

        title_label.setAlignment(
            Qt.AlignCenter
        )

        form_layout.addWidget(
            title_label
        )

        form_layout.addSpacing(
            15
        )

        # ==================================================
        # EMPLOYEE ID
        # ==================================================

        id_label = QLabel(
            "Employee ID"
        )

        self.id_input = QLineEdit()

        self.id_input.setPlaceholderText(
            "Enter employee ID"
        )

        self.add_field(
            form_layout,
            id_label,
            self.id_input
        )

        # ==================================================
        # NAME
        # ==================================================

        name_label = QLabel(
            "Name"
        )

        self.name_input = QLineEdit()

        self.name_input.setPlaceholderText(
            "Enter employee name"
        )

        self.add_field(
            form_layout,
            name_label,
            self.name_input
        )

        # ==================================================
        # EMAIL
        # ==================================================

        email_label = QLabel(
            "Email"
        )

        self.email_input = QLineEdit()

        self.email_input.setPlaceholderText(
            "Enter email address"
        )

        self.add_field(
            form_layout,
            email_label,
            self.email_input
        )

        # ==================================================
        # PHONE
        # ==================================================

        phone_label = QLabel(
            "Phone"
        )

        self.phone_input = QLineEdit()

        self.phone_input.setPlaceholderText(
            "Enter 10 digit phone number"
        )

        self.add_field(
            form_layout,
            phone_label,
            self.phone_input
        )

        # ==================================================
        # DEPARTMENT
        # ==================================================

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

        self.add_field(
            form_layout,
            department_label,
            self.department_combo
        )

        # ==================================================
        # SALARY
        # ==================================================

        salary_label = QLabel(
            "Salary"
        )

        self.salary_input = QLineEdit()

        self.salary_input.setPlaceholderText(
            "Enter salary"
        )

        self.add_field(
            form_layout,
            salary_label,
            self.salary_input
        )

        # ==================================================
        # ERROR MESSAGE
        # ==================================================

        self.error_label = QLabel(
            ""
        )

        self.error_label.setObjectName(
            "errorLabel"
        )

        form_layout.addWidget(
            self.error_label
        )

        # ==================================================
        # BUTTONS
        # ==================================================

        button_layout = QHBoxLayout()

        button_layout.setSpacing(
            10
        )

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

        button_layout.addWidget(
            self.register_button
        )

        button_layout.addWidget(
            self.clear_button
        )

        form_layout.addLayout(
            button_layout
        )

        # ---------------- Card Layout ----------------

        card.setLayout(
            form_layout
        )

        # ---------------- Center Card ----------------

        main_layout.addStretch()

        card_layout = QHBoxLayout()

        card_layout.addStretch()

        card_layout.addWidget(
            card
        )

        card_layout.addStretch()

        main_layout.addLayout(
            card_layout
        )

        main_layout.addStretch()

        self.setLayout(
            main_layout
        )

        # ==================================================
        # SIGNALS
        # ==================================================

        self.register_button.clicked.connect(
            self.register_employee
        )

        self.clear_button.clicked.connect(
            self.clear_form
        )

        # ==================================================
        # QSS
        # ==================================================

        self.setStyleSheet("""

        QWidget {
            background-color: #f5f7fa;
            font-family: Arial;
            font-size: 14px;
        }

        /* ---------------- Card ---------------- */

        #registerCard {
            background-color: white;
            border: 1px solid #e5e7eb;
            border-radius: 12px;
        }

        /* ---------------- Labels ---------------- */

        QLabel {
            color: #374151;
            font-weight: bold;
        }

        /* ---------------- Title ---------------- */

        #titleLabel {
            font-size: 24px;
            font-weight: bold;
            color: #1f2937;
        }

        /* ---------------- Inputs ---------------- */

        QLineEdit,
        QComboBox {
            background-color: white;
            border: 1px solid #d1d5db;
            border-radius: 6px;
            padding: 7px 8px;
            min-height: 16px;
        }

        QLineEdit:focus,
        QComboBox:focus {
            border: 2px solid #2563eb;
        }

        /* ---------------- Register Button ---------------- */

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

        /* ---------------- Clear Button ---------------- */

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

        /* ---------------- Error ---------------- */

        #errorLabel {
            color: #dc2626;
            font-weight: bold;
        }

        """)

    # ==================================================
    # ADD FIELD
    # ==================================================

    def add_field(
        self,
        layout,
        label,
        field
    ):

        row_layout = QHBoxLayout()

        row_layout.setSpacing(
            15
        )

        # Fixed label width
        label.setFixedWidth(
            100
        )

        # Input width
        field.setFixedWidth(
            280
        )

        # Label
        row_layout.addWidget(
            label
        )

        # Input
        row_layout.addWidget(
            field
        )

        # Add row
        layout.addLayout(
            row_layout
        )

    # ==================================================
    # REGISTER EMPLOYEE
    # ==================================================

    def register_employee(self):

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

        for field_name, value in required_fields:

            if not value:

                self.show_error(
                    f"{field_name} is required."
                )

                return

        # ---------------- Employee ID ----------------

        if not employee[0].isdigit():

            self.show_error(
                "Employee ID should contain only numbers."
            )

            return

        # ---------------- Name ----------------

        if not re.fullmatch(
            r"[A-Za-z ]+",
            employee[1]
        ):

            self.show_error(
                "Name should contain only letters."
            )

            return

        # ---------------- Email ----------------

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

        # ---------------- Phone ----------------

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

        # ---------------- Salary ----------------

        if not employee[5].isdigit():

            self.show_error(
                "Salary should contain only numbers."
            )

            return

        # ---------------- Send Data ----------------

        self.register_employee_signal.emit(
            employee
        )

        # Clear form
        self.clear_form()

    # ==================================================
    # CLEAR FORM
    # ==================================================

    def clear_form(self):

        fields = [
            self.id_input,
            self.name_input,
            self.email_input,
            self.phone_input,
            self.salary_input
        ]

        for field in fields:

            field.clear()

        self.department_combo.setCurrentIndex(
            0
        )

        self.clear_error()

    # ==================================================
    # ERROR
    # ==================================================

    def show_error(self, message):

        self.error_label.setText(
            message
        )

    def clear_error(self):

        self.error_label.setText(
            ""
        )