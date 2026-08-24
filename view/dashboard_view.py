from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout,
    QFrame
)

from PyQt5.QtCore import Qt


class DashboardView(QWidget):

    def __init__(self):
        super().__init__()

        self.setup_ui()


    def setup_ui(self):

        # ---------------- Main Window ----------------

        self.setWindowTitle(
            "Employee Management System - Dashboard"
        )

        self.resize(
            1000,
            600
        )


        # ==================================================
        # SIDEBAR
        # ==================================================

        self.sidebar = QFrame()

        self.sidebar.setObjectName(
            "sidebar"
        )

        self.sidebar.setFixedWidth(
            210
        )


        # ---------------- Sidebar Title ----------------

        self.sidebar_title = QLabel(
            "EMS"
        )

        self.sidebar_title.setObjectName(
            "sidebarTitle"
        )

        self.sidebar_title.setAlignment(
            Qt.AlignCenter
        )


        # ---------------- Dashboard Button ----------------

        self.dashboard_button = QPushButton(
            "Dashboard"
        )

        self.dashboard_button.setObjectName(
            "activeButton"
        )


        # ---------------- Employee Button ----------------

        self.employee_button = QPushButton(
            "Employees"
        )


        # ---------------- Logout ----------------

        self.logout_button = QPushButton(
            "Logout"
        )


        # ---------------- Sidebar Layout ----------------

        sidebar_layout = QVBoxLayout()

        sidebar_layout.setContentsMargins(
            15,
            25,
            15,
            25
        )

        sidebar_layout.setSpacing(
            10
        )


        sidebar_layout.addWidget(
            self.sidebar_title
        )

        sidebar_layout.addSpacing(
            20
        )

        sidebar_layout.addWidget(
            self.dashboard_button
        )

        sidebar_layout.addWidget(
            self.employee_button
        )


        # Empty space

        sidebar_layout.addStretch()


        # Logout at bottom

        sidebar_layout.addWidget(
            self.logout_button
        )


        self.sidebar.setLayout(
            sidebar_layout
        )


        # ==================================================
        # MAIN CONTENT
        # ==================================================

        self.content_frame = QFrame()

        self.content_frame.setObjectName(
            "contentFrame"
        )


        content_layout = QVBoxLayout()

        content_layout.setContentsMargins(
            30,
            30,
            30,
            30
        )

        content_layout.setSpacing(
            20
        )


        # ---------------- Header ----------------

        self.dashboard_title = QLabel(
            "Admin Dashboard"
        )

        self.dashboard_title.setObjectName(
            "dashboardTitle"
        )


        self.welcome_label = QLabel(
            "Welcome, Admin"
        )

        self.welcome_label.setObjectName(
            "welcomeLabel"
        )


        content_layout.addWidget(
            self.dashboard_title
        )

        content_layout.addWidget(
            self.welcome_label
        )


        # ==================================================
        # DASHBOARD CARDS
        # ==================================================

        cards_layout = QHBoxLayout()

        cards_layout.setSpacing(
            20
        )


        # ---------------- Total Employees ----------------

        self.total_card = QFrame()

        self.total_card.setObjectName(
            "dashboardCard"
        )


        total_layout = QVBoxLayout()


        self.total_title = QLabel(
            "Total Employees"
        )

        self.total_title.setObjectName(
            "cardTitle"
        )


        self.total_count = QLabel(
            "0"
        )

        self.total_count.setObjectName(
            "cardCount"
        )

        self.total_count.setAlignment(
            Qt.AlignCenter
        )


        total_layout.addWidget(
            self.total_title
        )

        total_layout.addWidget(
            self.total_count
        )


        self.total_card.setLayout(
            total_layout
        )


        # ---------------- IT Department ----------------

        self.it_card = QFrame()

        self.it_card.setObjectName(
            "dashboardCard"
        )


        it_layout = QVBoxLayout()


        self.it_title = QLabel(
            "IT Department"
        )

        self.it_title.setObjectName(
            "cardTitle"
        )


        self.it_count = QLabel(
            "0"
        )

        self.it_count.setObjectName(
            "cardCount"
        )

        self.it_count.setAlignment(
            Qt.AlignCenter
        )


        it_layout.addWidget(
            self.it_title
        )

        it_layout.addWidget(
            self.it_count
        )


        self.it_card.setLayout(
            it_layout
        )


        # ---------------- Other Departments ----------------

        self.other_card = QFrame()

        self.other_card.setObjectName(
            "dashboardCard"
        )


        other_layout = QVBoxLayout()


        self.other_title = QLabel(
            "Other Departments"
        )

        self.other_title.setObjectName(
            "cardTitle"
        )


        self.other_count = QLabel(
            "0"
        )

        self.other_count.setObjectName(
            "cardCount"
        )

        self.other_count.setAlignment(
            Qt.AlignCenter
        )


        other_layout.addWidget(
            self.other_title
        )

        other_layout.addWidget(
            self.other_count
        )


        self.other_card.setLayout(
            other_layout
        )


        # ---------------- Add Cards ----------------

        cards_layout.addWidget(
            self.total_card
        )

        cards_layout.addWidget(
            self.it_card
        )

        cards_layout.addWidget(
            self.other_card
        )


        content_layout.addLayout(
            cards_layout
        )


        content_layout.addStretch()


        self.content_frame.setLayout(
            content_layout
        )


        # ==================================================
        # MAIN LAYOUT
        # ==================================================

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


        main_layout.addWidget(
            self.sidebar
        )

        main_layout.addWidget(
            self.content_frame
        )


        self.setLayout(
            main_layout
        )


        # ==================================================
        # QSS
        # ==================================================

        self.setStyleSheet("""

        QWidget {
            background-color: #f3f4f6;
            font-family: Arial;
            font-size: 14px;
        }


        /* Sidebar */

        #sidebar {
            background-color: #1f2937;
        }


        #sidebarTitle {
            color: white;
            font-size: 28px;
            font-weight: bold;
        }


        /* Sidebar Buttons */

        #sidebar QPushButton {
            background-color: #374151;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 12px;
            text-align: left;
            font-size: 14px;
            font-weight: bold;
        }


        #sidebar QPushButton:hover {
            background-color: #4b5563;
        }


        #sidebar #activeButton {
            background-color: #2563eb;
        }


        #sidebar #activeButton:hover {
            background-color: #1d4ed8;
        }


        /* Content */

        #contentFrame {
            background-color: #f3f4f6;
        }


        /* Title */

        #dashboardTitle {
            color: #111827;
            font-size: 28px;
            font-weight: bold;
        }


        #welcomeLabel {
            color: #6b7280;
            font-size: 15px;
        }


        /* Cards */

        #dashboardCard {
            background-color: white;
            border: 1px solid #e5e7eb;
            border-radius: 10px;
            min-height: 140px;
        }


        #dashboardCard:hover {
            border: 1px solid #2563eb;
        }


        #cardTitle {
            color: #6b7280;
            font-size: 15px;
            font-weight: bold;
            background-color: transparent;
        }


        #cardCount {
            color: #111827;
            font-size: 32px;
            font-weight: bold;
            background-color: transparent;
        }

        """)