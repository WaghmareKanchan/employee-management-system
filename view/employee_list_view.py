from PyQt5.QtWidgets import (
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QPushButton,
    QHBoxLayout,
    QLabel,
    QHeaderView
)

from PyQt5.QtCore import pyqtSignal, Qt


class EmployeeListView(QWidget):

    # Signal used to send selected employee data
    # when View button is clicked.
    view_employee_signal = pyqtSignal(object)

    # Signal used to send selected employee data
    # when Edit button is clicked.
    edit_employee_signal = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        # ---------------- Title ----------------

        title_label = QLabel("Employee List")
        title_label.setObjectName("titleLabel")

        # ---------------- Table ----------------

        self.table = QTableWidget()

        # 6 employee data columns + 1 Action column.
        self.table.setColumnCount(7)

        # Column names.
        self.table.setHorizontalHeaderLabels([
            "ID",
            "Name",
            "Email",
            "Phone",
            "Department",
            "Salary",
            "Action"
        ])

        # Prevent editing table cells directly.
        self.table.setEditTriggers(
            QTableWidget.NoEditTriggers
        )

        # Select complete row instead of individual cell.
        self.table.setSelectionBehavior(
            QTableWidget.SelectRows
        )

        # Allow only one row to be selected.
        self.table.setSelectionMode(
            QTableWidget.SingleSelection
        )

        # Alternating row colors.
        self.table.setAlternatingRowColors(True)

        # Set row height.
        self.table.verticalHeader().setDefaultSectionSize(45)

        # Hide row numbers.
        self.table.verticalHeader().setVisible(False)

        # ---------------- Column Width ----------------

        self.table.setColumnWidth(0, 70)
        self.table.setColumnWidth(1, 140)
        self.table.setColumnWidth(2, 220)
        self.table.setColumnWidth(3, 130)
        self.table.setColumnWidth(4, 130)
        self.table.setColumnWidth(5, 110)
        self.table.setColumnWidth(6, 180)

        # ---------------- Header ----------------

        header = self.table.horizontalHeader()

        # Keep Action column fixed.
        header.setSectionResizeMode(
            6,
            QHeaderView.Fixed
        )

        # Other columns resize according to content/space.
        for column in range(6):
            header.setSectionResizeMode(
                column,
                QHeaderView.Stretch
            )

        # ---------------- Main Layout ----------------

        layout = QVBoxLayout()

        # Proper page margins.
        layout.setContentsMargins(
            30, 25, 30, 30
        )

        # Space between widgets.
        layout.setSpacing(15)

        # Add title.
        layout.addWidget(title_label)

        # Add table.
        layout.addWidget(self.table)

        # Apply layout.
        self.setLayout(layout)

        # ---------------- Styling ----------------

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

        QTableWidget {
            background-color: white;
            border: 1px solid #d1d5db;
            border-radius: 8px;
            gridline-color: #e5e7eb;
            selection-background-color: #dbeafe;
            selection-color: #111827;
        }

        QTableWidget::item {
            padding: 8px;
        }

        QTableWidget::item:selected {
            background-color: #dbeafe;
            color: #111827;
        }

        QHeaderView::section {
            background-color: #2563eb;
            color: white;
            padding: 10px;
            border: none;
            font-weight: bold;
        }

        QScrollBar:vertical {
            width: 10px;
            background-color: #f3f4f6;
        }

        QScrollBar::handle:vertical {
            background-color: #9ca3af;
            border-radius: 5px;
            min-height: 30px;
        }

        QPushButton {
            border-radius: 5px;
            padding: 6px 12px;
            font-weight: bold;
        }

        QPushButton:hover {
            opacity: 0.9;
        }

        """)

    def add_employee(self, employee):

        # Gets the current number of rows.
        row = self.table.rowCount()

        # Creates a new row.
        self.table.insertRow(row)

        # Adds employee data to the first 6 columns.
        for column, value in enumerate(employee):

            self.table.setItem(
                row,
                column,
                QTableWidgetItem(value)
            )


        # Centers selected columns.
        for column in [0, 3, 4, 5]:

            self.table.item(
                row,
                column
            ).setTextAlignment(
                Qt.AlignCenter
            )

        # ---------------- Buttons ----------------

        view_button = QPushButton("View")
        edit_button = QPushButton("Edit")

        # Fixed button size.
        view_button.setFixedSize(70, 30)
        edit_button.setFixedSize(70, 30)

        # Button styling.
        view_button.setStyleSheet("""
            QPushButton {
                background-color: #2563eb;
                color: white;
                border: none;
                border-radius: 5px;
            }

            QPushButton:hover {
                background-color: #1d4ed8;
            }
        """)

        edit_button.setStyleSheet("""
            QPushButton {
                background-color: #6b7280;
                color: white;
                border: none;
                border-radius: 5px;
            }

            QPushButton:hover {
                background-color: #4b5563;
            }
        """)

        # ---------------- Signals ----------------

        view_button.clicked.connect(
            lambda checked=False, emp=employee:
                self.view_employee_signal.emit(emp)
        )

        edit_button.clicked.connect(
            lambda checked=False, emp=employee:
                self.edit_employee_signal.emit(emp)
        )

        # ---------------- Button Layout ----------------

        button_layout = QHBoxLayout()

        # Remove unnecessary spacing around buttons.
        button_layout.setContentsMargins(
            5, 0, 5, 0
        )

        button_layout.setSpacing(8)

        button_layout.addWidget(view_button)
        button_layout.addWidget(edit_button)

        # Create container widget.
        button_widget = QWidget()

        # Apply button layout.
        button_widget.setLayout(button_layout)

        # Add buttons to Action column.
        self.table.setCellWidget(
            row,
            6,
            button_widget
        )