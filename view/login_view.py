from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QFrame
)

from PyQt5.QtCore import Qt


class LoginView(QWidget):

    def __init__(self):
        super().__init__()

        self.setup_ui()


    def setup_ui(self):

        # ---------------- Main Window ----------------

        self.setWindowTitle(
            "Employee Management System - Login"
        )

        self.resize(
            1000,
            600
        )


        # ---------------- Login Card ----------------

        self.login_card = QFrame()

        self.login_card.setObjectName(
            "loginCard"
        )

        self.login_card.setFixedWidth(
            400
        )


        # ---------------- Title ----------------

        self.title_label = QLabel(
            "Employee Management System"
        )

        self.title_label.setObjectName(
            "titleLabel"
        )

        self.title_label.setAlignment(
            Qt.AlignCenter
        )


        # ---------------- Subtitle ----------------

        self.subtitle_label = QLabel(
            "Login to continue"
        )

        self.subtitle_label.setObjectName(
            "subtitleLabel"
        )

        self.subtitle_label.setAlignment(
            Qt.AlignCenter
        )


        # ---------------- Username ----------------

        self.username_label = QLabel(
            "Username"
        )

        self.username = QLineEdit()

        self.username.setPlaceholderText(
            "Enter username"
        )

        self.username.setFixedHeight(
            42
        )


        # ---------------- Password ----------------

        self.password_label = QLabel(
            "Password"
        )

        self.password = QLineEdit()

        self.password.setPlaceholderText(
            "Enter password"
        )

        self.password.setEchoMode(
            QLineEdit.Password
        )

        self.password.setFixedHeight(
            42
        )


        # ---------------- Login Button ----------------

        self.login_button = QPushButton(
            "Login"
        )

        self.login_button.setFixedHeight(
            45
        )


        # ---------------- Card Layout ----------------

        card_layout = QVBoxLayout()

        card_layout.setContentsMargins(
            40,
            35,
            40,
            35
        )

        card_layout.setSpacing(
            10
        )


        card_layout.addWidget(
            self.title_label
        )

        card_layout.addWidget(
            self.subtitle_label
        )


        card_layout.addSpacing(
            20
        )


        card_layout.addWidget(
            self.username_label
        )

        card_layout.addWidget(
            self.username
        )


        card_layout.addSpacing(
            8
        )


        card_layout.addWidget(
            self.password_label
        )

        card_layout.addWidget(
            self.password
        )


        card_layout.addSpacing(
            20
        )


        card_layout.addWidget(
            self.login_button
        )


        self.login_card.setLayout(
            card_layout
        )


        # ---------------- Main Layout ----------------

        main_layout = QVBoxLayout()

        main_layout.setContentsMargins(
            20,
            20,
            20,
            20
        )


        main_layout.addStretch()


        main_layout.addWidget(
            self.login_card,
            alignment=Qt.AlignCenter
        )


        main_layout.addStretch()


        self.setLayout(
            main_layout
        )


        # ---------------- Styling ----------------

        self.setStyleSheet("""

        /* Main Window */

        QWidget {
            background-color: #f3f4f6;
            font-family: Arial;
            font-size: 14px;
        }


        /* Login Card */

        #loginCard {
            background-color: white;

            border: 1px solid #e5e7eb;

            border-radius: 12px;
        }


        /* Title */

        #titleLabel {
            color: #111827;

            font-size: 20px;

            font-weight: bold;

            padding-bottom: 4px;
        }


        /* Subtitle */

        #subtitleLabel {
            color: #6b7280;

            font-size: 14px;
        }


        /* Labels */

        QLabel {
            background-color: transparent;

            color: #374151;

            font-size: 14px;

            font-weight: bold;
        }


        /* Input Fields */

        QLineEdit {
            background-color: #f9fafb;

            color: #111827;

            border: 1px solid #d1d5db;

            border-radius: 6px;

            padding: 0 12px;

            font-size: 14px;
        }


        QLineEdit:focus {
            border: 1px solid #2563eb;

            background-color: white;
        }


        /* Login Button */

        QPushButton {
            background-color: #2563eb;

            color: white;

            border: none;

            border-radius: 6px;

            font-size: 15px;

            font-weight: bold;
        }


        QPushButton:hover {
            background-color: #1d4ed8;
        }


        QPushButton:pressed {
            background-color: #1e40af;
        }

        """)