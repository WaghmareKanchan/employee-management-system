from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QStackedWidget,
    QFrame
)

from PyQt5.QtCore import Qt

from view.register_view import RegisterView
from view.employee_list_view import EmployeeListView
from view.employee_detail_view import EmployeeDetailView
from view.edit_employee_view import EditEmployeeView


class MainView(QWidget):

    def __init__(self):
        super().__init__()

        # Creates the main application window.
        self.setup_ui()


    def setup_ui(self):

        # ---------------- Main Window ----------------

        self.setWindowTitle(
            "Employee Management System"
        )

        self.resize(
            1000,
            600
        )


        # ---------------- Sidebar Buttons ----------------

        self.register_button = QPushButton(
            "Register Employee"
        )

        self.employee_list_button = QPushButton(
            "Employee List"
        )


        # ---------------- Sidebar Layout ----------------

        self.sidebar_layout = QVBoxLayout()

        self.sidebar_layout.setContentsMargins(
            15,
            25,
            15,
            25
        )

        self.sidebar_layout.setSpacing(
            10
        )


        # Adds buttons to sidebar.

        self.sidebar_layout.addWidget(
            self.register_button
        )

        self.sidebar_layout.addWidget(
            self.employee_list_button
        )

        # Empty space below buttons.
        self.sidebar_layout.addStretch()


        # ---------------- Sidebar Widget ----------------

        self.sidebar = QFrame()

        self.sidebar.setObjectName(
            "sidebar"
        )

        self.sidebar.setLayout(
            self.sidebar_layout
        )


        # ---------------- Stacked Widget ----------------

        self.stack = QStackedWidget()


        # Empty page.
        self.empty_page = QWidget()


        # ---------------- Application Views ----------------

        self.register_view = RegisterView()

        self.employee_list_view = EmployeeListView()

        self.employee_detail_view = EmployeeDetailView()

        self.edit_employee_view = EditEmployeeView()


        # ---------------- Add Pages ----------------

        self.stack.addWidget(
            self.empty_page
        )

        self.stack.addWidget(
            self.register_view
        )

        self.stack.addWidget(
            self.employee_list_view
        )

        self.stack.addWidget(
            self.employee_detail_view
        )

        self.stack.addWidget(
            self.edit_employee_view
        )


        # ---------------- Main Content ----------------

        # Container for the stacked widget.
        self.content_frame = QFrame()

        self.content_frame.setObjectName(
            "contentFrame"
        )


        # Content layout.
        content_layout = QVBoxLayout()

        content_layout.setContentsMargins(
            20,
            20,
            20,
            20
        )


        # Adds stack to content area.
        content_layout.addWidget(
            self.stack
        )

        self.content_frame.setLayout(
            content_layout
        )


        # ---------------- Main Layout ----------------

        main_layout = QHBoxLayout()

        main_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        main_layout.setSpacing(
            0
        )


        # Sidebar on left.
        main_layout.addWidget(
            self.sidebar
        )


        # Content on right.
        main_layout.addWidget(
            self.content_frame
        )


        # Sidebar width.
        self.sidebar.setFixedWidth(
            210
        )


        # Applies main layout.
        self.setLayout(
            main_layout
        )


        # ---------------- QSS Styling ----------------

        self.setStyleSheet("""

        /* Main Window */

        QWidget {
            background-color: #f5f7fa;
            font-family: Arial;
            font-size: 14px;
        }


        /* Sidebar */

        #sidebar {
            background-color: #1f2937;
        }


        /* Sidebar Buttons */

        #sidebar QPushButton {
            background-color: #374151;
            color: white;
            border: none;
            border-radius: 6px;

            padding: 12px;

            font-size: 14px;
            font-weight: bold;

            text-align: left;
        }


        #sidebar QPushButton:hover {
            background-color: #4b5563;
        }


        #sidebar QPushButton:pressed {
            background-color: #2563eb;
        }


        /* Main Content */

        #contentFrame {
            background-color: #f5f7fa;
        }

        """)