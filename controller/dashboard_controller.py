class DashboardController:

    def __init__(
        self,
        view,
        main_dict,
        main_view
    ):

        # Dashboard View reference

        self.view = view


        # Shared employee dictionary

        self.main_dict = main_dict
        
        self.main_view = main_view


        # Initial count update

        self.update_counts()
        
        self.view.employee_button.clicked.connect(
            self.open_employee_list
        )


    def update_counts(self):

        # ---------------- Total Employees ----------------

        total_employees = len(
            self.main_dict
        )


        # ---------------- IT Employees ----------------

        it_count = 0


        for employee in self.main_dict.values():

            if employee["Department"] == "IT":

                it_count += 1


        # ---------------- Other Departments ----------------

        other_count = (
            total_employees - it_count
        )


        # ---------------- Update UI ----------------

        self.view.total_count.setText(
            str(total_employees)
        )

        self.view.it_count.setText(
            str(it_count)
        )

        self.view.other_count.setText(
            str(other_count)
        )
        
        
        # ---------------- Employee List ----------------

    def open_employee_list(self):

        # Hide Dashboard

        self.view.hide()


        # Open Employee List page

        self.main_view.stack.setCurrentWidget(
            self.main_view.employee_list_view
        )


        # Show MainView

        self.main_view.show()