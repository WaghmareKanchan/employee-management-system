import json

from PyQt5.QtWidgets import QTableWidgetItem


class EmployeeListController:

    def __init__(self, view, main_view, main_dict):

        # EmployeeListView reference
        self.view = view

        # MainView reference
        self.main_view = main_view

        # Shared employee dictionary
        self.main_dict = main_dict

        # View button signal
        self.view.view_employee_signal.connect(
            self.view_employee
        )

        # Edit button signal
        self.view.edit_employee_signal.connect(
            self.edit_employee
        )

        # Delete signal from EmployeeDetailView
        self.main_view.employee_detail_view.delete_employee_signal.connect(
            self.delete_employee
        )

        # Update signal from EditEmployeeView
        self.main_view.edit_employee_view.update_employee_signal.connect(
            self.update_employee
        )

    # ==================================================
    # VIEW EMPLOYEE
    # ==================================================

    def view_employee(self, employee):

        self.main_view.employee_detail_view.set_employee_data(
            employee
        )

        self.main_view.stack.setCurrentWidget(
            self.main_view.employee_detail_view
        )

    # ==================================================
    # DELETE EMPLOYEE
    # ==================================================

    def delete_employee(self, employee):

        # Employee ID is always at index 0
        employee_id = str(employee[0])

        # JSON key
        key = "Employee " + employee_id

        # ---------------- JSON UPDATE ----------------

        if key in self.main_dict:

            # Keep Employee ID unchanged.
            self.main_dict[key]["Name"] = ""
            self.main_dict[key]["Email"] = ""
            self.main_dict[key]["Phone"] = ""
            self.main_dict[key]["Department"] = ""
            self.main_dict[key]["Salary"] = ""

       

        # Search employee row using Employee ID.
        # ---------------- TABLE ----------------

        for row in range(self.view.table.rowCount()):

            table_item = self.view.table.item(row, 0)

            if table_item is not None:

                table_id = table_item.text()

                if table_id == employee_id:

                    # Keep Employee ID.
                    # Clear Name, Email, Phone,
                    # Department and Salary.

                    for column in range(1, 6):

                        self.view.table.setItem(
                            row,
                            column,
                            QTableWidgetItem("")
                        )

                    # ---------------- ACTION BUTTONS ----------------

                    button_widget = self.view.table.cellWidget(
                        row,
                        6
                    )

                    if button_widget is not None:

                        self.view.table.removeCellWidget(
                            row,
                            6
                        )

                    # Return to Employee List.
                    self.main_view.stack.setCurrentWidget(
                        self.main_view.employee_list_view
                    )

                    break

        # ---------------- CHECK JSON ----------------

        print("AFTER DELETE")
        print(
            json.dumps(
                self.main_dict,
                indent=2
            )
        )

        # ---------------- BACK TO LIST ----------------

        self.main_view.stack.setCurrentWidget(
            self.main_view.employee_list_view
        )

    # ==================================================
    # EDIT EMPLOYEE
    # ==================================================

    def edit_employee(self, employee):

        self.main_view.edit_employee_view.set_employee_data(
            employee
        )

        self.main_view.stack.setCurrentWidget(
            self.main_view.edit_employee_view
        )

    # ==================================================
    # UPDATE EMPLOYEE
    # ==================================================

    def update_employee(self, employee):

        # Employee ID identifies the employee.
        employee_id = str(employee[0])

        # JSON key
        key = "Employee " + employee_id

        # ---------------- JSON UPDATE ----------------

        if key in self.main_dict:

            self.main_dict[key]["Name"] = employee[1]
            self.main_dict[key]["Email"] = employee[2]
            self.main_dict[key]["Phone"] = employee[3]
            self.main_dict[key]["Department"] = employee[4]
            self.main_dict[key]["Salary"] = employee[5]

        # ---------------- TABLE UPDATE ----------------

        for row in range(self.view.table.rowCount()):

            table_item = self.view.table.item(
                row,
                0
            )

            if table_item is not None:

                table_id = table_item.text()

                if table_id == employee_id:

                    self.view.table.setItem(
                        row,
                        1,
                        QTableWidgetItem(employee[1])
                    )

                    self.view.table.setItem(
                        row,
                        2,
                        QTableWidgetItem(employee[2])
                    )

                    self.view.table.setItem(
                        row,
                        3,
                        QTableWidgetItem(employee[3])
                    )

                    self.view.table.setItem(
                        row,
                        4,
                        QTableWidgetItem(employee[4])
                    )

                    self.view.table.setItem(
                        row,
                        5,
                        QTableWidgetItem(employee[5])
                    )

                    break

        # ---------------- CHECK JSON ----------------

        print("AFTER UPDATE")
        print(
            json.dumps(
                self.main_dict,
                indent=2
            )
        )

        # Back to Employee List
        self.main_view.stack.setCurrentWidget(
            self.main_view.employee_list_view
        )