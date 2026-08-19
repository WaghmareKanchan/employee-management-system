import re

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QFrame
)

from PyQt5.QtCore import pyqtSignal, Qt


class EditEmployeeView(QWidget):

    # Sends updated employee data
    # from View to Controller.
    update_employee_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        # Creates the Edit Employee UI.
        self.setup_ui()


    def setup_ui(self):

        # ---------------- Window Title ----------------

        self.setWindowTitle(
            "Edit Employee"
        )


        # ---------------- Title ----------------

        title_label = QLabel(
            "Edit Employee"
        )

        title_label.setObjectName(
            "titleLabel"
        )

        title_label.setAlignment(
            Qt.AlignCenter
        )


        # ---------------- Employee ID ----------------

        id_label = QLabel(
            "Employee ID"
        )

        self.id_input = QLineEdit()

        # Employee ID cannot be changed.
        self.id_input.setReadOnly(
            True
        )

        self.id_input.setPlaceholderText(
            "Employee ID"
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


        # ---------------- Signals ----------------

        self.update_button.clicked.connect(
            self.update_employee
        )

        self.clear_button.clicked.connect(
            self.clear_form
        )


        # ==================================================
        # FORM LAYOUT
        # ==================================================

        form_layout = QFormLayout()

        form_layout.setHorizontalSpacing(
            20
        )

        form_layout.setVerticalSpacing(
            12
        )


        # Label alignment
        form_layout.setLabelAlignment(
            Qt.AlignRight
        )


        # Input alignment
        form_layout.setFormAlignment(
            Qt.AlignCenter
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


        # Adds label + input pairs.
        #
        # Same operation is repeated,
        # therefore for loop is suitable.
        for label, field in fields:

            form_layout.addRow(
                label,
                field
            )


        # ==================================================
        # BUTTON LAYOUT
        # ==================================================

        button_layout = QHBoxLayout()

        button_layout.setSpacing(
            10
        )

        button_layout.setAlignment(
            Qt.AlignCenter
        )


        button_layout.addWidget(
            self.update_button
        )

        button_layout.addWidget(
            self.clear_button
        )


        # ==================================================
        # FORM CONTAINER
        # ==================================================

        form_container = QFrame()

        form_container.setObjectName(
            "formContainer"
        )


        container_layout = QVBoxLayout()

        container_layout.setContentsMargins(
            35,
            30,
            35,
            30
        )

        container_layout.setSpacing(
            15
        )


        # Title
        container_layout.addWidget(
            title_label
        )


        # Form
        container_layout.addLayout(
            form_layout
        )


        # Error message
        container_layout.addWidget(
            self.error_label
        )


        # Buttons
        container_layout.addLayout(
            button_layout
        )


        form_container.setLayout(
            container_layout
        )


        # ==================================================
        # MAIN LAYOUT
        # ==================================================

        main_layout = QVBoxLayout()

        main_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )


        # Centers the form vertically.
        main_layout.addStretch()


        # Centers the form horizontally.
        main_layout.addWidget(
            form_container,
            alignment=Qt.AlignCenter
        )


        # Centers the form vertically.
        main_layout.addStretch()


        self.setLayout(
            main_layout
        )


        # ==================================================
        # QSS STYLING
        # ==================================================

        self.setStyleSheet("""

        QWidget {
            background-color: #f5f7fa;
            font-family: Arial;
            font-size: 14px;
        }


        /* ---------------- Form Container ---------------- */

        #formContainer {

            background-color: white;

            border: 1px solid #e5e7eb;

            border-radius: 10px;
        }


        /* ---------------- Labels ---------------- */

        QLabel {

            color: #333333;

            font-weight: bold;
        }


        /* ---------------- Title ---------------- */

        #titleLabel {

            font-size: 24px;

            font-weight: bold;

            color: #1f2937;

            padding-bottom: 5px;
        }


        /* ---------------- Input Fields ---------------- */

        QLineEdit,
        QComboBox {

            background-color: white;

            border: 1px solid #d1d5db;

            border-radius: 6px;

            padding: 8px;

            min-width: 240px;

            min-height: 18px;
        }


        /* ---------------- Focus ---------------- */

        QLineEdit:focus,
        QComboBox:focus {

            border: 2px solid #2563eb;
        }


        /* ---------------- Read Only Employee ID ---------------- */

        QLineEdit:read-only {

            background-color: #e5e7eb;

            color: #6b7280;
        }


        /* ---------------- Update Button ---------------- */

        #updateButton {

            background-color: #2563eb;

            color: white;

            border: none;

            border-radius: 6px;

            padding: 10px 25px;

            font-weight: bold;
        }


        #updateButton:hover {

            background-color: #1d4ed8;
        }


        /* ---------------- Clear Button ---------------- */

        #clearButton {

            background-color: #e5e7eb;

            color: #374151;

            border: none;

            border-radius: 6px;

            padding: 10px 25px;

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
    # SET EMPLOYEE DATA
    # ==================================================

    def set_employee_data(self, employee):

        # Stores employee currently being edited.
        self.employee = employee


        # Employee ID
        self.id_input.setText(
            employee[0]
        )


        # Name
        self.name_input.setText(
            employee[1]
        )


        # Email
        self.email_input.setText(
            employee[2]
        )


        # Phone
        self.phone_input.setText(
            employee[3]
        )


        # Department
        index = self.department_combo.findText(
            employee[4]
        )


        if index >= 0:

            self.department_combo.setCurrentIndex(
                index
            )


        # Salary
        self.salary_input.setText(
            employee[5]
        )


        # Clear previous error.
        self.clear_error()


    # ==================================================
    # UPDATE EMPLOYEE
    # ==================================================

    def update_employee(self):

        # Collect updated employee data.
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

            ("Name", employee[1]),

            ("Email", employee[2]),

            ("Phone", employee[3]),

            ("Salary", employee[5])
        ]


        # Checks required fields.
        for field_name, value in required_fields:

            if not value:

                self.show_error(
                    f"{field_name} is required."
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


        # ---------------- Send Updated Data ----------------

        self.update_employee_signal.emit(
            employee
        )


    # ==================================================
    # CLEAR FORM
    # ==================================================

    def clear_form(self):

        # Employee ID remains unchanged.
        self.name_input.clear()

        self.email_input.clear()

        self.phone_input.clear()

        self.salary_input.clear()


        # Reset department.
        self.department_combo.setCurrentIndex(
            0
        )


        # Clear error.
        self.clear_error()


    # ==================================================
    # ERROR
    # ==================================================

    def show_error(self, message):

        self.error_label.setText(
            message
        )


    def clear_error(self):

        self.error_label.setText("")