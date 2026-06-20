# Human Resource Management System (HRMS)
**INFORMATION MAIN
ITS ALREADY LOGIN FIRST, YOU HAVE TO CREATE EMPLOYEE AND THROUGH EMPLOYEE YOU CAN LOGIN OR LOGOUT !!!
## Project Overview

The Human Resource Management System (HRMS) is a web-based application developed using Django and MySQL to automate and manage various HR operations within an organization.

The system provides centralized management for departments, roles, employees, task assignments, performance reviews, and leave management. It helps HR teams, managers, and administrators efficiently manage employee information and organizational workflows.

---

## Technology Stack

### Frontend

* HTML5
* CSS3
* Bootstrap 5

### Backend

* Python
* Django Framework

### Database

* MySQL

### Deployment

* Render

### Version Control

* Git
* GitHub

---

# Implemented Modules

## Module 1 - Department Management

### Features

* Add Department
* Update Department
* Delete Department
* Search Department
* Department Dashboard

### Fields

* Department Name
* Description
* Status
* Created Date
* Updated Date

---

## Module 2 - Role Management

### Features

* Add Role
* Update Role
* Delete Role
* Search Role
* Role Dashboard

### Fields

* Role Name
* Description
* Status

---

## Module 3 - Employee Management

### Features

* Add Employee
* Update Employee
* Delete Employee
* Search Employee
* Assign Department
* Assign Role
* Reporting Manager Mapping

### Fields

* First Name
* Last Name
* Username
* Password
* Email
* Mobile
* Department
* Role
* Reporting Manager
* Date Of Joining

---

## Module 4 - Authentication & Password Recovery

### Features

* Employee Login
* Logout
* Forgot Password
* OTP Generation
* OTP Verification
* Password Reset
* Email Integration

### Security Features

* Session Management
* OTP Verification
* Secure Password Reset Flow

---

## Module 5 - Task Management System

### Features

* Create Task
* Update Task
* Delete Task
* Assign Task
* Task Dashboard
* Assignment Dashboard
* Task Status Tracking

### Task Status

* Pending
* In Progress
* Completed

### Task Details

* Task Title
* Description
* Priority
* Start Date
* End Date
* Task Type

---

## Module 6 - Performance Review Management

### Features

* Add Performance Review
* Update Review
* Delete Review
* Search Reviews
* Filter Reviews
* Review Dashboard
* Employee Performance Tracking

### Review Details

* Review Title
* Review Date
* Employee
* Reviewed By
* Review Period
* Rating
* Comments

### Review Periods

* Monthly
* Quarterly
* Annual

---

## Module 7 - Leave Management System

### Features

* Apply Leave
* Update Leave Request
* Leave Dashboard
* Leave Approval/Rejection
* Manager Dashboard
* Leave Quota Management
* Employee Leave Balance Tracking

### Leave Types

* PL (Privilege Leave)
* CL (Casual Leave)
* SL (Sick Leave)

### Leave Status

* Pending
* Approved
* Rejected

### Leave Quota Features

* Add Leave Quota
* Update Leave Quota
* Employee-wise Quota Tracking
* Remaining Leave Calculation

---

# Project Flow

### Step 1

Admin creates Departments.

### Step 2

Admin creates Roles.

### Step 3

Admin creates Employees and assigns Departments and Roles.

### Step 4

Employees login to the system.

### Step 5

Managers/Admin create and assign tasks.

### Step 6

Employee performs assigned tasks.

### Step 7

Managers conduct Performance Reviews.

### Step 8

Employees apply for leaves.

### Step 9

Managers approve or reject leave requests.

### Step 10

Leave balances are automatically managed through Leave Quota Management.

---

# Database Tables

### Department

### Role

### Employee

### OTP

### Task

### TaskAssignment

### PerformanceReview

### Leave

### LeaveQuota

---

# Key Features

* Department Management
* Role Management
* Employee Management
* Login Authentication
* OTP Verification
* Password Reset
* Task Assignment
* Performance Reviews
* Leave Management
* Leave Quota Tracking
* Search Functionality
* Dashboard Analytics
* Responsive Bootstrap UI

---

# Future Enhancements

* Attendance Management
* Payroll Management
* Employee Documents
* Email Notifications
* Reports & Analytics
* REST API Integration
* Role-Based Access Control (RBAC)

---

# Developer

**Parth Shirke**

Bachelor of Commerce (B.Com)

Master of Computer Applications (MCA)

Full Stack Python Developer

Mumbai, Maharashtra

---

# Internship Project

This project was developed as part of a Full Stack Python Development Internship Program and demonstrates end-to-end HR Management functionality using Django Framework.
