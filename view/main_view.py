from PyQt5.QtWidgets import ( QWidget,
    QPushButton, 
    QVBoxLayout, 
    QHBoxLayout, 
    QStackedWidget)

from view.register_view import RegisterView 
from view.employee_list_view import EmployeeListView
from view.employee_detail_view import EmployeeDetailView
from view.edit_employee_view import EditEmployeeView


class MainView(QWidget):
    
    def __init__(self): 
        super().__init__()
        
        # Calls the method responsible for creating
        # and arranging all GUI components.
        self.setup_ui()
        
    def setup_ui(self):
        
        self.setWindowTitle("Employee Management System")
        self.resize(1000, 600)
        
        # Creates the Register button for the left sidebar.
        self.register_button = QPushButton("Register Employee")
        
         # Creates the Employee List button for the left sidebar.
        self.employee_list_button = QPushButton("Employee List")
        
        # Creates the left sidebar layout.
        self.sidebar_layout = QVBoxLayout()
        
        # Adds Register button to the sidebar.
        self.sidebar_layout.addWidget(self.register_button)
        
        # Adds Employee List button to the sidebar.
        self.sidebar_layout.addWidget(self.employee_list_button)
        
        #sidebar widget
        self.sidebar = QWidget()
        self.sidebar.setLayout(self.sidebar_layout)
        
        
        # QStackedWidget is used to keep multiple pages
        # in the same area and display one page at a time.
        self.stack = QStackedWidget()
        
        self.empty_page = QWidget()
        
        
        # Creates the different pages of the application.
        # Each page is displayed on the right side of the main window.
        self.register_view = RegisterView()
        self.employee_list_view = EmployeeListView()
        self.employee_detail_view = EmployeeDetailView()
        self.edit_employee_view = EditEmployeeView()
        
        self.stack.addWidget(self.empty_page)
        
        # Adds Register page to the stacked widget.
        self.stack.addWidget(self.register_view)
        
        # Adds Employee List page to the stacked widget.
        self.stack.addWidget(self.employee_list_view)
        
        # Adds Employee Detail page to the stacked widget.
        self.stack.addWidget(self.employee_detail_view)
        
        # Adds Edit Employee page to the stacked widget.
        self.stack.addWidget(self.edit_employee_view)
        
        # Creates the main horizontal layout.
        # Sidebar will be on the left and stacked pages on the right.
        main_layout = QHBoxLayout()
        
        main_layout.addWidget(self.sidebar)
        
        # Adds the current page to the right side.
        main_layout.addWidget(self.stack)
        
        # Applies the main layout to the window.
        self.setLayout(main_layout)
        
        
    