from PyQt5.QtWidgets import QTableWidgetItem

class EmployeeListController: 
    
    def __init__(self,view, main_view):
        
        # Stores the EmployeeListView object.
        # This gives the controller access to the employee table
        # and View/Edit signals.
        self.view = view 
        
        
        # Stores the MainView object.
        # This is required to switch between different pages.
        self.main_view = main_view
        
        
        # Connects the View button signal to view_employee().
        #
        # When the user clicks View for an employee,
        # the selected employee data is passed to view_employee().
        self.view.view_employee_signal.connect(
            self.view_employee
        )
        
        
        # Connects the Edit button signal to edit_employee().
        #
        # When the user clicks Edit,
        # the selected employee data is passed to edit_employee().
        self.view.edit_employee_signal.connect(
            self.edit_employee
        )
        
        
        # Connects the Delete signal from EmployeeDetailView
        # to delete_employee().
        #
        # This allows the controller to delete the selected
        # employee from the table.
        self.main_view.employee_detail_view.delete_employee_signal.connect(
            self.delete_employee
        )
        
        
        # Connects the Update signal from EditEmployeeView
        # to update_employee().
        #
        # When the user clicks Update,
        # the updated employee data is received here.
        self.main_view.edit_employee_view.update_employee_signal.connect(
            self.update_employee
        )
        
    def view_employee(self,employee):
        
        # Sends the selected employee data to EmployeeDetailView.
        #
        # set_employee_data() displays the employee details
        # using labels.
        self.main_view.employee_detail_view.set_employee_data(employee)
        
        
        # Changes the current page to Employee Detail page.
        self.main_view.stack.setCurrentWidget(
            self.main_view.employee_detail_view
        )
        
    def delete_employee(self, employee):

        # Gets the Employee ID of the employee to be deleted.
        employee_id = employee[0]

        # Loops through every row in the employee table.
        for row in range(self.view.table.rowCount()):

            # Gets the Employee ID item from column 0.
            table_item = self.view.table.item(row, 0)

            # Checks whether the table cell contains data.
            if table_item is not None:

                # Gets the Employee ID from the table.
                table_id = table_item.text()

                # Checks whether the table employee ID
                # matches the employee being deleted.
                if table_id == employee_id:

                    # Removes the matching employee row.
                    self.view.table.removeRow(row)

                    # After deletion, returns to Employee List page.
                    self.main_view.stack.setCurrentWidget(
                        self.main_view.employee_list_view
                    )

                    # Stops the loop because the employee
                    # has already been found and deleted.
                    break
            
    def edit_employee(self,employee):
        
        # Sends the selected employee data to EditEmployeeView.
        #
        # The existing employee values are displayed
        # in the edit form.
        self.main_view.edit_employee_view.set_employee_data(employee)
        
        
        # Changes the current page to Edit Employee page.
        self.main_view.stack.setCurrentWidget(
            self.main_view.edit_employee_view
        )
        
    def update_employee(self, employee):

         # Gets the Employee ID.
        #
        # Employee ID is used to identify which row
        # should be updated.
        employee_id = employee[0]


        # Loops through all employee table rows.
        for row in range(self.view.table.rowCount()):

            # Gets the Employee ID from the current table row.
            table_item = self.view.table.item(row, 0)


            # Checks whether the table cell contains data.
            if table_item is not None:


                # Gets the Employee ID from the table.
                table_id = table_item.text()


                # Checks whether this is the employee
                # that needs to be updated.
                if table_id == employee_id:


                    # Updates the employee name.
                    self.view.table.setItem(
                        row, 1, QTableWidgetItem(employee[1])
                    )


                    # Updates the email.
                    self.view.table.setItem(
                        row, 2, QTableWidgetItem(employee[2])
                    )


                    # Updates the phone number.
                    self.view.table.setItem(
                        row, 3, QTableWidgetItem(employee[3])
                    )


                    # Updates the department.
                    self.view.table.setItem(
                        row, 4, QTableWidgetItem(employee[4])
                    )

                    # Updates the salary.
                    self.view.table.setItem(
                        row, 5, QTableWidgetItem(employee[5])
                    )


                    # Returns to the Employee List page
                    # after successful update.
                    self.main_view.stack.setCurrentWidget(
                        self.main_view.employee_list_view
                    )


                    # Stops searching because the employee
                    # has already been updated.
                    break
        

    