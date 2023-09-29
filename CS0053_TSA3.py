"""
CS0053 - Technical 3 Source Code for 1T AY 2023-2024

   Program:        Functions - Recursion
   Programmer(s):
                   Vassili L. Inacay (L)
                   Katryna Lei V. Martin
   Section:        AN31
   Start Date:     September 28, 2023
   End Date:       October 2, 2023
"""

totalExpense = 0
totalIncome = 0

# This function displays the main menu and prompts the user for a choice.
# It uses the global variables totalExpense and totalIncome.
# If the user selects an option other than 1, 2, 3, or 4, the function displays an error message and calls itself recursively.
def displayMenu():
    global totalExpense, totalIncome
    print("\n===== FINANCE TRACKER =====")
    print("[1] Add Expense")
    print("[2] Add Income")
    print("[3] Display Summary")
    print("[4] Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        addExpense()
    elif choice == 2:
        addIncome()
    elif choice == 3:
        computeSavings()
    elif choice == 4:
        pass
    else:
        print("\nInvalid input. Please try again!")
        displayMenu()

# This function prompts the user for an expense amount and adds it to the totalExpense variable.
# It then displays a success message and calls recursively displayMenu function.
def addExpense():
    global totalExpense
    expense = float(input("Enter expense amount: "))
    totalExpense += expense
    print("Expense added successfully.")
    displayMenu()

# This function prompts the user for an income amount and adds it to the totalIncome variable.
# It then displays a success message and calls recursively displayMenu function.
def addIncome():
    global totalIncome
    income = float(input("Enter income amount: "))
    totalIncome += income
    print("Income added successfully.")
    displayMenu()

# This function computes the savings by subtracting totalExpense from totalIncome.
# It then displays the total income, total expenses, and total savings.
# The function then calls recursively displayMenu function.
def computeSavings():
    global totalExpense, totalIncome
    savings = totalIncome - totalExpense
    print("\nTotal Income: " + str(totalIncome))
    print("Total Expenses: " + str(totalExpense))
    print("Total Savings: " + str(savings))
    displayMenu()

# This line of code displays a welcome message and calls the displayMenu function.
print("Welcome to VILM Inc.")
displayMenu()

# These lines of code display a closing message and the names of members of the group, including the course and section.
print("\n\nThank you for using the program!")
print("Created by: Inacay, Vassili & Martin, Katryna Lei")
print("Course: CS0053")
print("Section: AN31")
