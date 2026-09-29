#Store money or income information
import sys
money = {
    "salary" : 0,
    "extra_income" : 0
}

expenses = []

def Income():
    salary = float(input("Enter your Salary: ₹"))
    extra_income = float(input("enter the Extra income Amount: ₹"))
    money["salary"] = salary
    money["extra_income"] = extra_income
    
    total = salary + extra_income
    
    print(f"\nAmount ₹{total:.2f} Added Successfully!")

#Function to Add Expenses  
def Expense():
    category = input("Enter the category of Expense: ")
    amount = float(input("Enter amount spent: ₹"))
    
    expense = {
        "category": category,
        "amount": amount
    }
    
    expenses.append(expense)
    
    print("Expense Added Successfully!")
    
#Function to View total Expenses list
def View_Expense():
    if not expenses:
        print("\nNO EXPENSE!!")
        return

    print("\n----- EXPENSES -----")

    total_expense = 0

    for i, expense in enumerate(expenses, start=1):
        print(f"Expense {i}")
        print("Category:", expense["category"])
        print("Amount: ₹", expense["amount"])
        print("--------------------------------")

        total_expense += expense["amount"]

    print(f"Total Expense: ₹{total_expense:.2f}")

#Function to View Balance
def Balance():
    total_income = money["salary"] + money["extra_income"]
    total_expense = sum(expense["amount"] for expense in expenses)
    
    balance = total_income - total_expense
    
    print("\n----- BALANCE -----")
    print(f"Total Income: ₹{total_income:.2f}")
    print(f"Total Expense: ₹{total_expense:.2f}")
    print(f"Remaining Balance: ₹{balance:.2f}")
    
    # Exit Function
def Exit_App():
    print("\nFinancial Tracker Project. Thank you!")
    sys.exit()
    

def Mine_Menu():
    print("\n===== PERSONAL FINANCIAL TRACKER =====")
    print("1. Income")
    print("2. Expense")
    print("3. View Expense")
    print("4. Balance")
    print("5. Exit")

    choice = int(input("Enter your Choice: "))

    if choice == 1:
        Income()

    elif choice == 2:
        Expense()

    elif choice == 3:
        View_Expense()

    elif choice == 4:
        Balance()
        
    elif choice == 5:
            Exit_App()

    else:
        print("Invalid Choice! \n Try Again!")

    Mine_Menu()

Mine_Menu()
