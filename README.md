# Personal Expense & Budget Tracker 
A simple Python-based Personal Expense & Budget Tracker that helps users record daily expenses, organize them by category, set monthly budgets, and generate spending summaries.

# 📌 Project Description
The Personal Expense & Budget Tracker is a beginner-friendly Python application developed using Python's built-in modules.

Users can:
● Add daily expenses
● View all recorded expenses
● Organize expenses by category
● Set monthly budgets
● View monthly budgets
● Generate category-wise summaries
● Generate monthly spending summaries
● Check remaining budget
● Track total spending

The project stores expense information in a CSV file and monthly budget information in a JSON file.

# 🎯 Objectives
The main objectives of this project are:
● Improve Python programming skills
● Practice functions and conditional statements
● Understand file handling
● Work with CSV files
● Work with JSON files
● Practice date and time operations
● Implement exception handling
● Perform basic data processing

# 🛠️ Technologies Used:
● Python
● CSV
● JSON
● datetime
● File Handling
● VS Code
● Git
● GitHub
✨ Features
1. Add Expense
Users can enter:
Category
Description
Amount
The application automatically records the current date.

2. View All Expenses
Displays all recorded expenses with:
Date
Category
Description
Amount

3. Set Monthly Budget
Users can set a budget for a particular month.
Example:
Month: 2026-10
Budget: ₹15000

4. Category-wise Summary
The application calculates total spending for each category.
Example:
Food: ₹2500.00
Travel: ₹1800.00
Shopping: ₹3200.00

5. Monthly Spending Summary
Users can select a month and see:
Total spending
Monthly budget
Remaining budget
Budget exceeded amount

6. Overall Spending Summary
Displays the total expenses and category-wise spending.

# 📂 Project Structure
PersonalExpenseTracker/
│
├── main.py
├── expenses.csv
├── budget.json
└── README.md

expenses.csv and budget.json are automatically created when the application runs for the first time.

🚀 How to Run
Step 1: Install Python
● Make sure Python is installed on your computer.
Check using:
python --version

Step 2: Create Project Folder
Create a folder:
● PersonalExpenseTracker

Step 3: Create Python File
Inside the folder, create:
● main.py

Step 4: Add the Code
● Copy the complete project code into main.py.

Step 5: Run the Project
● Open the terminal inside the project folder and run:

python main.py
🖥️ Application Menu
====================================
 PERSONAL EXPENSE & BUDGET TRACKER
====================================
1. Add Expense
2. View All Expenses
3. Set Monthly Budget
4. View Monthly Budgets
5. Category-wise Summary
6. Monthly Spending Summary
7. Overall Spending Summary
8. Exit
====================================
Enter your choice (1-8):
📊 Example
Add Expense
--- Add Expense ---

Enter category: Food
Enter description: Lunch
Enter amount: ₹150

Expense added successfully!

The expense will be stored in expenses.csv.

Example:

Date,Category,Description,Amount
2026-10-03,Food,Lunch,150
💾 Data Storage
CSV

Expense information is stored in:

expenses.csv
JSON

Monthly budget information is stored in:

budget.json

Example:

{
    "2026-10": 15000
}
# 📚 Python Concepts Practiced
This project provides practice with:
● Variables
● Functions
● if-elif-else
● while loops
● Lists and dictionaries
● CSV file handling
● JSON file handling
● Exception handling
● datetime
● File and directory operations
● User input
● Basic data processing

# 🔮 Future Improvements
The project can be extended with:
● User login system
● SQLite database
● Graphical User Interface
● Web application
● Expense editing and deletion
● Expense search
● Export reports to PDF
● Charts and graphs
● Monthly expense comparison
● Income tracking

# ⭐ Conclusion
● This project is a practical example of using Python to build a real-world expense and budget management application while practicing file handling, functions, data processing, and exception handling.
● If you find this project useful, consider giving the repository a ⭐ on GitHub.
