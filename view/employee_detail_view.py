from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame
)

from PyQt5.QtCore import pyqtSignal, Qt


class EmployeeDetailView(QWidget):

    # Signal used to send selected employee data
    # to EmployeeListController when Delete is clicked.
    delete_employee_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        # Stores currently selected employee.
        self.employee = None

        # Creates Employee Detail UI.
        self.setup_ui()

    def setup_ui(self):

        # ==================================================
        # TITLE
        # ==================================================

        self.title_label = QLabel(
            "Employee Details"
        )

        self.title_label.setObjectName(
            "titleLabel"
        )

        self.title_label.setAlignment(
            Qt.AlignCenter
        )

        # ==================================================
        # EMPLOYEE DETAIL LABELS
        # ==================================================

        self.id_label = QLabel(
            "ID:"
        )

        self.name_label = QLabel(
            "Name:"
        )

        self.email_label = QLabel(
            "Email:"
        )

        self.phone_label = QLabel(
            "Phone:"
        )

        self.department_label = QLabel(
            "Department:"
        )

        self.salary_label = QLabel(
            "Salary:"
        )

        # Store all labels.
        detail_labels = [
            self.id_label,
            self.name_label,
            self.email_label,
            self.phone_label,
            self.department_label,
            self.salary_label
        ]

        # Same styling for all detail labels.
        for label in detail_labels:

            label.setObjectName(
                "detailLabel"
            )

        # ==================================================
        # DETAIL CARD
        # ==================================================

        detail_card = QFrame()

        detail_card.setObjectName(
            "detailCard"
        )

        # Fixed width keeps card small
        # even when GUI is maximized.
        detail_card.setFixedWidth(
            450
        )

        # Card layout.
        detail_layout = QVBoxLayout()

        detail_layout.setContentsMargins(
            25,
            25,
            25,
            25
        )

        detail_layout.setSpacing(
            12
        )

        # Add employee details.
        for label in detail_labels:

            detail_layout.addWidget(
                label
            )

        detail_card.setLayout(
            detail_layout
        )

        # ==================================================
        # DELETE BUTTON
        # ==================================================

        self.delete_button = QPushButton(
            "Delete"
        )

        self.delete_button.setObjectName(
            "deleteButton"
        )

        self.delete_button.clicked.connect(
            self.delete_employee
        )

        # ==================================================
        # FORM CONTAINER
        # ==================================================

        # This layout contains:
        #
        # Title
        # Card
        # Delete button
        #
        # Everything will remain together.

        form_layout = QVBoxLayout()

        form_layout.setContentsMargins(
            30,
            30,
            30,
            30
        )

        form_layout.setSpacing(
            15
        )

        form_layout.addWidget(
            self.title_label
        )

        form_layout.addWidget(
            detail_card
        )

        form_layout.addWidget(
            self.delete_button
        )

        # ==================================================
        # CENTER DELETE BUTTON
        # ==================================================

        self.delete_button.setFixedWidth(
            450
        )

        # ==================================================
        # CENTER COMPLETE FORM
        # ==================================================

        main_layout = QVBoxLayout()

        main_layout.setContentsMargins(
            0,
            20,
            0,
            20
        )

        # Vertical center.
        main_layout.addStretch()

        # Horizontal center.
        center_layout = QHBoxLayout()

        center_layout.addStretch()

        center_layout.addLayout(
            form_layout
        )

        center_layout.addStretch()

        main_layout.addLayout(
            center_layout
        )

        # Vertical center.
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

        /* ---------------- Title ---------------- */

        #titleLabel {
            font-size: 24px;
            font-weight: bold;
            color: #1f2937;
            padding-bottom: 5px;
        }

        /* ---------------- Detail Card ---------------- */

        #detailCard {
            background-color: white;
            border: 1px solid #d1d5db;
            border-radius: 10px;
        }

        /* ---------------- Employee Details ---------------- */

        #detailLabel {
            color: #374151;
            font-size: 15px;
            font-weight: bold;
            padding: 6px;
        }

        /* ---------------- Delete Button ---------------- */

        #deleteButton {
            background-color: #dc2626;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 10px;
            font-weight: bold;
        }

        #deleteButton:hover {
            background-color: #b91c1c;
        }

        """)

    # ==================================================
    # SET EMPLOYEE DATA
    # ==================================================

    def set_employee_data(self, employee):

        # Stores selected employee.
        self.employee = employee

        # Employee labels.
        labels = [
            self.id_label,
            self.name_label,
            self.email_label,
            self.phone_label,
            self.department_label,
            self.salary_label
        ]

        # Display names.
        names = [
            "ID",
            "Name",
            "Email",
            "Phone",
            "Department",
            "Salary"
        ]

        # Adds employee data to labels.
        for label, name, value in zip(
            labels,
            names,
            employee
        ):

            label.setText(
                name + ": " + value
            )

    # ==================================================
    # DELETE EMPLOYEE
    # ==================================================

    def delete_employee(self):

        # Checks whether employee is selected.
        if self.employee:

            # Sends selected employee data
            # to EmployeeListController.
            self.delete_employee_signal.emit(
                self.employee
            )