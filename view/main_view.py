from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QStackedWidget,
    QLabel,
    QFrame
)

from view.register_view import RegisterView
from view.employee_list_view import EmployeeListView
from view.employee_detail_view import EmployeeDetailView
from view.edit_employee_view import EditEmployeeView


class MainView(QWidget):

    def __init__(self):
        super().__init__()

        # Creates and arranges the complete GUI.
        self.setup_ui()


    def setup_ui(self):

        # ---------------- Main Window ----------------

        self.setWindowTitle(
            "Employee Management System"
        )

        self.resize(
            1100,
            650
        )


        # ---------------- Sidebar ----------------

        self.sidebar = QFrame()

        # Object name is used by QSS.
        self.sidebar.setObjectName(
            "sidebar"
        )

        # Fixed width for sidebar.
        self.sidebar.setFixedWidth(
            230
        )


        # ---------------- Application Title ----------------

        self.app_title = QLabel(
            "Employee\nManagement System"
        )

        self.app_title.setObjectName(
            "appTitle"
        )


        # ---------------- Register Button ----------------

        self.register_button = QPushButton(
            "Register Employee"
        )

        self.register_button.setObjectName(
            "sidebarButton"
        )

        # Allows active button styling.
        self.register_button.setCheckable(
            True
        )


        # ---------------- Employee List Button ----------------

        self.employee_list_button = QPushButton(
            "Employee List"
        )

        self.employee_list_button.setObjectName(
            "sidebarButton"
        )

        # Allows active button styling.
        self.employee_list_button.setCheckable(
            True
        )


        # ---------------- Sidebar Layout ----------------

        self.sidebar_layout = QVBoxLayout()

        # Space around sidebar content.
        self.sidebar_layout.setContentsMargins(
            20,
            30,
            20,
            30
        )

        # Space between widgets.
        self.sidebar_layout.setSpacing(
            12
        )


        # Adds application title.
        self.sidebar_layout.addWidget(
            self.app_title
        )

        # Space after title.
        self.sidebar_layout.addSpacing(
            25
        )


        # Stores sidebar buttons in a list.
        sidebar_buttons = [
            self.register_button,
            self.employee_list_button
        ]


        # Adds all sidebar buttons using for loop.
        for button in sidebar_buttons:

            self.sidebar_layout.addWidget(
                button
            )


        # Pushes buttons towards the top.
        self.sidebar_layout.addStretch()


        # Applies layout to sidebar.
        self.sidebar.setLayout(
            self.sidebar_layout
        )


        # ---------------- Stacked Widget ----------------

        self.stack = QStackedWidget()

        self.stack.setObjectName(
            "contentArea"
        )


        # ---------------- Pages ----------------

        self.empty_page = QWidget()

        self.register_view = RegisterView()

        self.employee_list_view = EmployeeListView()

        self.employee_detail_view = EmployeeDetailView()

        self.edit_employee_view = EditEmployeeView()


        # ---------------- Add Pages ----------------

        pages = [
            self.empty_page,
            self.register_view,
            self.employee_list_view,
            self.employee_detail_view,
            self.edit_employee_view
        ]


        # Adds all pages using for loop.
        for page in pages:

            self.stack.addWidget(
                page
            )


        # ---------------- Main Layout ----------------

        main_layout = QHBoxLayout()

        # Removes extra outer spacing.
        main_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )

        # Removes gap between sidebar and content.
        main_layout.setSpacing(
            0
        )


        # Sidebar on left.
        main_layout.addWidget(
            self.sidebar
        )


        # Content area on right.
        main_layout.addWidget(
            self.stack
        )


        # Applies main layout.
        self.setLayout(
            main_layout
        )


        # ---------------- QSS Styling ----------------

        self.setStyleSheet("""

        QWidget {

            font-family: Arial;

            font-size: 14px;
        }


        /* Sidebar */

        #sidebar {

            background-color: #1e293b;

            border: none;
        }


        /* Application Title */

        #appTitle {

            color: white;

            font-size: 20px;

            font-weight: bold;
        }


        /* Sidebar Buttons */

        #sidebarButton {

            background-color: transparent;

            color: #cbd5e1;

            border: none;

            border-radius: 7px;

            padding: 13px;

            text-align: left;

            font-size: 15px;

            font-weight: 500;
        }


        /* Hover */

        #sidebarButton:hover {

            background-color: #334155;

            color: white;
        }


        /* Active Button */

        #sidebarButton:checked {

            background-color: #2563eb;

            color: white;

            font-weight: bold;
        }


        /* Content Area */

        #contentArea {

            background-color: #f5f7fa;

            border: none;
        }

        """)