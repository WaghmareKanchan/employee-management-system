from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QComboBox,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox
)

from PyQt5.QtCore import pyqtSignal


class RegisterView(QWidget):

    # Signal used to send employee data
    # from View to Controller.
    register_employee_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        self.setWindowTitle("Register Employee")

        # ---------------- Title ----------------

        title_label = QLabel("Register Employee")
        title_label.setObjectName("titleLabel")

        # ---------------- Employee ID ----------------

        id_label = QLabel("Employee ID")
        self.id_input = QLineEdit()
        self.id_input.setPlaceholderText("Enter employee ID")

        # ---------------- Name ----------------

        name_label = QLabel("Name")
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter employee name")

        # ---------------- Email ----------------

        email_label = QLabel("Email")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter email address")

        # ---------------- Phone ----------------

        phone_label = QLabel("Phone")
        self.phone_input = QLineEdit()
        self.phone_input.setPlaceholderText("Enter 10 digit phone number")

        # ---------------- Department ----------------

        department_label = QLabel("Department")

        self.department_combo = QComboBox()

        self.department_combo.addItems([
            "IT",
            "HR",
            "Finance"
        ])

        # ---------------- Salary ----------------

        salary_label = QLabel("Salary")
        self.salary_input = QLineEdit()
        self.salary_input.setPlaceholderText("Enter salary")

        # ---------------- Error Label ----------------

        self.error_label = QLabel("")
        self.error_label.setObjectName("errorLabel")

        # ---------------- Buttons ----------------

        self.register_button = QPushButton("Register")
        self.register_button.setObjectName("registerButton")

        self.clear_button = QPushButton("Clear")
        self.clear_button.setObjectName("clearButton")

        # Register button
        self.register_button.clicked.connect(
            self.register_employee
        )

        # Clear button
        self.clear_button.clicked.connect(
            self.clear_form
        )

        # ---------------- Button Layout ----------------

        button_layout = QHBoxLayout()

        button_layout.addWidget(
            self.register_button
        )

        button_layout.addWidget(
            self.clear_button
        )

        # ---------------- Main Layout ----------------

        layout = QVBoxLayout()

        layout.setContentsMargins(
            80, 40, 80, 40
        )

        layout.setSpacing(10)

        layout.addWidget(title_label)

        layout.addSpacing(15)

        layout.addWidget(id_label)
        layout.addWidget(self.id_input)

        layout.addWidget(name_label)
        layout.addWidget(self.name_input)

        layout.addWidget(email_label)
        layout.addWidget(self.email_input)

        layout.addWidget(phone_label)
        layout.addWidget(self.phone_input)

        layout.addWidget(department_label)
        layout.addWidget(self.department_combo)

        layout.addWidget(salary_label)
        layout.addWidget(self.salary_input)

        layout.addSpacing(5)

        layout.addWidget(self.error_label)

        layout.addSpacing(10)

        layout.addLayout(button_layout)

        self.setLayout(layout)

        # ---------------- Styling ----------------

        self.setStyleSheet("""
        
        QWidget {
            background-color: #f5f7fa;
            font-size: 14px;
        }

        QLabel {
            color: #333333;
            font-weight: 500;
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
            color: #333333;
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

        # Collect employee data.
        employee = [
            self.id_input.text(),
            self.name_input.text(),
            self.email_input.text(),
            self.phone_input.text(),
            self.department_combo.currentText(),
            self.salary_input.text()
        ]

        # Send data to controller.
        self.register_employee_signal.emit(
            employee
        )

    def clear_form(self):

        # Clear all input fields.
        self.id_input.clear()
        self.name_input.clear()
        self.email_input.clear()
        self.phone_input.clear()
        self.salary_input.clear()

        # Reset department dropdown.
        self.department_combo.setCurrentIndex(0)

        # Clear error message.
        self.clear_error()

    def show_error(self, message):

        # Display validation error.
        self.error_label.setText(message)

    def clear_error(self):

        # Remove validation error.
        self.error_label.setText("")