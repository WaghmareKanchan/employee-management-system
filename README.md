# employee-management-system
A Python PyQt5 desktop application for managing employee records with CRUD operations using MVC architecture.

# Employee Management System

A desktop-based Employee Management System developed using Python and PyQt5.

The application follows an MVC-oriented architecture and provides a graphical interface for managing employee records through CRUD operations.

---

## 📌 Project Overview

The Employee Management System is a Python desktop application that allows users to:

- Register employees
- View employee records
- View complete employee details
- Edit employee information
- Update employee records
- Delete employees
- Navigate between different application pages

The project is developed using PyQt5 and follows the Model-View-Controller (MVC) design approach to keep the GUI and application logic separated.

---

## 🎯 Objectives

The main objectives of this project are:

- Learn desktop GUI development using PyQt5
- Implement CRUD operations
- Understand MVC architecture
- Understand PyQt Signals and Slots
- Implement page navigation using QStackedWidget
- Practice clean project structure
- Use Git and GitHub for version control
- Create a foundation that can later be connected to an API and database

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| PyQt5 | Desktop GUI Framework |
| Qt Widgets | GUI Components |
| QStackedWidget | Page Navigation |
| Signals & Slots | Communication between View and Controller |
| Git | Version Control |
| GitHub | Source Code Management |

---

##  Architecture

The project follows an MVC-oriented architecture.


                    Employee Management System
                              |
                              ↓
                         Main Window
                              |
                         MainController
                              |
                ┌─────────────┴─────────────┐
                ↓                           ↓
        RegisterController       EmployeeListController
                ↓                           ↓
         RegisterView             EmployeeListView
                                            |
                              ┌─────────────┼─────────────┐
                              ↓             ↓             ↓
                           View          Edit          Delete
                              ↓             ↓
                    EmployeeDetailView  EditEmployeeView