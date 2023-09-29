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


# Allow users to enter both expenses and income and then present a summary.
def displayMenu():
    global totalExpense, totalIncome
    print("========================================")
    print("            FINANCE TRACKER             ")
    print("========================================")
    print("[1] Record Income                       ")
    print("[2] Record Expense                      ")
    print("[3] Summary                             ")
    print("[4] Exit \n                             ")

    choice = int(input("Enter choice: "))

    if choice == 1:
        recordIncome()
    elif choice == 2:
        recordExpense()
    elif choice == 3:
        computeSavings()
    elif choice == 4:
        exitProgram()
        pass
    else:
        print("Invalid input. Please try again!")
        displayMenu()


# Allows the user to enter his entire expenditure.
def recordExpense():
    global totalExpense
    print("========================================")
    print("             RECORD EXPENSE             ")
    print("========================================")
    expense = float(input("Enter expense amount: ₱"))
    totalExpense += expense
    print("Expense recorded successfully.")
    displayMenu()


# Allows the user to compare his monthly earnings to his overall earnings.
def recordIncome():
    global totalIncome
    print("========================================")
    print("             RECORD INCOME              ")
    print("========================================")
    income = float(input("Enter income amount: ₱"))
    totalIncome += income
    print("Income recorded successfully.")
    displayMenu()


# Calculates and displays the user's total income and total expenses.
def computeSavings():
    global totalExpense, totalIncome
    print("========================================")
    print("                SUMMARY                 ")
    print("========================================")

    if totalExpense > totalIncome:
        print('!!! Insufficient Savings !!!\n')

    savings = totalIncome - totalExpense
    print(f"Total Income  : ₱{totalIncome:.2f}")
    print(f"Total Expenses: ₱{totalExpense:.2f}")
    print(f"Total Savings : ₱{savings:.2f}")
    displayMenu()


# Exiting the program with credits
def exitProgram():
    print("========================================")
    print("                 EXIT                   ")
    print("========================================")
    print(
        "Thank you for using the program!   \n\n"
        "Programmers: INACAY, Vassili L.    \n"
        "             MARTIN, Katryna Lei V.\n"
        "Course     : CS0053                \n"
        "Section    : AN31                    "
    )
    print("========================================")


if __name__ == '__main__':
    print("Welcome to VILM Inc.")
    displayMenu()
