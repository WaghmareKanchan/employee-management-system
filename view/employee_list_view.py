from PyQt5.QtWidgets import (
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QPushButton,
    QHBoxLayout
)
from PyQt5.QtCore import pyqtSignal 


class EmployeeListView(QWidget):
    
    # Signal used to send selected employee data
    # from View to EmployeeListController when View button is clicked.
    view_employee_signal = pyqtSignal(object)
    
    
    # Signal used to send selected employee data
    # from View to EmployeeListController when Edit button is clicked.
    edit_employee_signal = pyqtSignal(object)
    
    
    def __init__(self):
        super().__init__()
        
        # Creates and arranges the employee list UI.
        self.setup_ui()

    def setup_ui(self):

        # Creates a table widget to display employee records.
        self.table = QTableWidget()


        # We have 7 columns:
        # 6 employee data columns + 1 Action column.
        self.table.setColumnCount(7)


        # Sets the column names displayed in the table.
        self.table.setHorizontalHeaderLabels([
            "ID",
            "Name",
            "Email",
            "Phone",
            "Department",
            "Salary",
            "Action"
        ])
        
        # Column widths
        self.table.setColumnWidth(0, 70)
        self.table.setColumnWidth(1, 130)
        self.table.setColumnWidth(2, 200)
        self.table.setColumnWidth(3, 120)
        self.table.setColumnWidth(4, 120)
        self.table.setColumnWidth(5, 100)
        self.table.setColumnWidth(6, 180)


        # Creates a vertical layout.
        layout = QVBoxLayout()


        # Adds the employee table to the layout.
        layout.addWidget(self.table)


        # Applies the layout to EmployeeListView.
        self.setLayout(layout)
    
    def add_employee(self,employee):
        
        # Gets the current number of rows.
        # The new employee will be added after the existing rows.
        row = self.table.rowCount()
        
        
        # Creates a new empty row.
        self.table.insertRow(row)
        
        # Adds Employee ID to column 0.
        self.table.setItem(
            row, 0, QTableWidgetItem(employee[0])
        )

        # Adds Name to column 1.
        self.table.setItem(
            row, 1, QTableWidgetItem(employee[1])
        )

        # Adds Email to column 2.
        self.table.setItem(
            row, 2, QTableWidgetItem(employee[2])
        )
            
        # Adds Phone to column 3.
        self.table.setItem(
            row, 3, QTableWidgetItem(employee[3])
        )

        # Adds Department to column 4.
        self.table.setItem(
            row, 4, QTableWidgetItem(employee[4])
        )

        # Adds Salary to column 5.
        self.table.setItem(
            row, 5, QTableWidgetItem(employee[5])
        )
            
        # Creates View and Edit buttons for each employee.
        view_button = QPushButton("View")
        edit_button = QPushButton("Edit")
            
        # Sets fixed size so the button text is completely visible.
        view_button.setFixedSize(70,30)
        edit_button.setFixedSize(70,30)
            
        
        # When View is clicked, the selected employee data
        # is sent through view_employee_signal.
        view_button.clicked.connect(
            lambda checked=False, emp=employee:
                self.view_employee_signal.emit(emp)
        )
            
            
        # When Edit is clicked, the selected employee data
        # is sent through edit_employee_signal.
        edit_button.clicked.connect(
            lambda checked=False, emp=employee:
                self.edit_employee_signal.emit(emp)
        )
            
        # Creates a horizontal layout for View and Edit buttons.
        button_layout = QHBoxLayout()
            
        # Adds View button to the button layout.
        button_layout.addWidget(view_button)
        
        # Adds Edit button to the button layout.
        button_layout.addWidget(edit_button)
            
        # Creates a QWidget to hold both buttons.
        button_widget = QWidget()
        
        # Applies the horizontal button layout to the widget.
        button_widget.setLayout(button_layout)
            
            
        # Places the button widget inside the Action column.
        # Column 6 is the Action column
        self.table.setCellWidget(row,6,button_widget)
            
            
            