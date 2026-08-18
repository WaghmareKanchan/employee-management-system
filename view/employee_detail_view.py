from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QFrame
)

from PyQt5.QtCore import pyqtSignal


class EmployeeDetailView(QWidget):

    # Signal used to send selected employee data
    # to EmployeeListController when Delete is clicked.
    delete_employee_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        # Stores the currently selected employee.
        self.employee = None

        # Creates the Employee Detail UI.
        self.setup_ui()

    def setup_ui(self):

        # ---------------- Title ----------------

        self.title_label = QLabel("Employee Details")

        # Gives the title a unique object name.
        # QSS will use this name for styling.
        self.title_label.setObjectName(
            "titleLabel"
        )


        # ---------------- Employee Detail Labels ----------------

        self.id_label = QLabel("ID:")
        self.name_label = QLabel("Name:")
        self.email_label = QLabel("Email:")
        self.phone_label = QLabel("Phone:")
        self.department_label = QLabel("Department:")
        self.salary_label = QLabel("Salary:")


        # Stores all detail labels in a list.
        #
        # All these labels need the same styling,
        # so we can use a for loop.
        detail_labels = [
            self.id_label,
            self.name_label,
            self.email_label,
            self.phone_label,
            self.department_label,
            self.salary_label
        ]


        # Applies the same object name
        # to all detail labels.
        for label in detail_labels:

            label.setObjectName(
                "detailLabel"
            )


        # ---------------- Detail Card ----------------

        # Creates a frame that works like
        # a card around employee information.
        detail_card = QFrame()

        detail_card.setObjectName(
            "detailCard"
        )


        # Creates layout inside the detail card.
        detail_layout = QVBoxLayout()

        # Space between employee details.
        detail_layout.setSpacing(15)


        # Adds all employee detail labels.
        #
        # Instead of writing addWidget()
        # six times, we use a for loop.
        for label in detail_labels:

            detail_layout.addWidget(
                label
            )


        # Applies the layout to the card.
        detail_card.setLayout(
            detail_layout
        )


        # ---------------- Delete Button ----------------

        self.delete_button = QPushButton(
            "Delete"
        )

        # Unique name used by QSS.
        self.delete_button.setObjectName(
            "deleteButton"
        )


        # Connects Delete button to delete_employee().
        self.delete_button.clicked.connect(
            self.delete_employee
        )


        # ---------------- Main Layout ----------------

        layout = QVBoxLayout()


        # Adds space around the complete form.
        layout.setContentsMargins(
            80,
            40,
            80,
            40
        )


        # Space between widgets.
        layout.setSpacing(20)


        # Adds title.
        layout.addWidget(
            self.title_label
        )


        # Adds employee detail card.
        layout.addWidget(
            detail_card
        )


        # Adds Delete button.
        layout.addWidget(
            self.delete_button
        )


        # Pushes content towards the top.
        layout.addStretch()


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


        #detailCard {
            background-color: white;
            border: 1px solid #d1d5db;
            border-radius: 10px;
        }


        #detailLabel {
            color: #374151;
            font-size: 15px;
            padding: 8px;
        }


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


    def set_employee_data(self, employee):

        # Stores the selected employee.
        #
        # This employee will later be used
        # when Delete button is clicked.
        self.employee = employee


        # Employee labels and their display names.
        labels = [
            self.id_label,
            self.name_label,
            self.email_label,
            self.phone_label,
            self.department_label,
            self.salary_label
        ]

        names = [
            "ID",
            "Name",
            "Email",
            "Phone",
            "Department",
            "Salary"
        ]


        # Adds employee data to the labels.
        #
        # zip() combines:
        # labels + names + employee data
        #
        # Example:
        # id_label + ID + employee[0]
        # name_label + Name + employee[1]
        # etc.
        for label, name, value in zip(
            labels,
            names,
            employee
        ):

            label.setText(
                name + ": " + value
            )


    def delete_employee(self):

        # Checks whether an employee
        # is currently selected.
        if self.employee:

            # Sends selected employee data
            # to EmployeeListController.
            self.delete_employee_signal.emit(
                self.employee
            )