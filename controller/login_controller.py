from PyQt5.QtWidgets import QMessageBox


class LoginController:

    def __init__(
        self,
        login_view,
        main_view,
        dashboard_view
    ):

        # ---------------- View References ----------------

        self.view = login_view

        self.main_view = main_view

        self.dashboard_view = dashboard_view


        # ---------------- Hardcoded Users ----------------

        self.users = {

            "admin1": {
                "password": "admin123",
                "user_type": "Admin"
            },

            "user1": {
                "password": "user123",
                "user_type": "User"
            }
        }


        # ---------------- Signals ----------------

        self.view.login_button.clicked.connect(
            self.login
        )


        self.dashboard_view.logout_button.clicked.connect(
            self.logout_admin
        )


    # ---------------- Login ----------------

    def login(self):

        # Get username

        username = self.view.username.text()


        # Get password

        password = self.view.password.text()


        # ---------------- Username Validation ----------------

        if username not in self.users:

            QMessageBox.warning(
                self.view,
                "Login Failed",
                "Invalid username"
            )

            return


        # ---------------- Password Validation ----------------

        if password != self.users[username]["password"]:

            QMessageBox.warning(
                self.view,
                "Login Failed",
                "Invalid password"
            )

            return


        # ---------------- Get User Type ----------------

        user_type = self.users[username]["user_type"]


        # ---------------- Admin ----------------

        if user_type == "Admin":

            self.dashboard_view.show()

            self.view.hide()


        # ---------------- User ----------------

        elif user_type == "User":

            # Open Register page directly

            self.main_view.stack.setCurrentWidget(
                self.main_view.register_view
            )

            self.main_view.register_button.setChecked(
                True
            )

            self.main_view.employee_list_button.setChecked(
                False
            )

            self.main_view.show()

            self.view.hide()


    # ---------------- Admin Logout ----------------

    def logout_admin(self):

        self.dashboard_view.hide()

        self.view.username.clear()

        self.view.password.clear()

        self.view.show()