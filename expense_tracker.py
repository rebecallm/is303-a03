'''
Rebeca Llontop 
IS 303 - A03

Expense Tracker 
This program tracks expenses by category and produces a spending summary

Inputs:
- Enter number of expenses (int)
- Expense limit (float)
- For each expense: category (string), amount (float)

Processes:
- create dictionary with category and expenses
- Accumulate totals per category
- Find the biggest expense
- Filter expenses above a limit

Outputs:
- Print each expense category and amount
- Print total expenses, average expense, biggest expense, and filtered list
'''

#Inputs
name = input("What is your name? ").capitalize()
num_expenses = int(input("What is the number of your monthly expenses? "))
expenses = {}
#Create the loop for the categories and amount 
for i in range(num_expenses): 
    category = input("Enter category: ").capitalize()
    amount = float(input("Enter the amount: ")) 
    expenses[category]= amount 

expense_limit = float(input("What is your monthly expense limit? "))
print(f"{name}, your expenses are: ")

for category, amount in expenses.items():
    print(f"{category} ${amount:.2f}")

#Use the accumulator and add up the values 
total_expenses = 0 
for amount in expenses.values(): 
    total_expenses += amount
print (f"The total value of your expenses are: ${total_expenses:.2f}.")

#Find the average 
total_average = total_expenses / (len(expenses))
print(f"The total of your monthly average expense is ${total_average:.2f}.")

#Find the biggest expense 
top_expense = 0 
top_category = ""
for category, amount in expenses.items():
    if amount > top_expense:
        top_expense = amount
        top_category = category
print(f"Your biggest expense is {top_category}: ${top_expense:.2f}.")

#Filtered list of expenses above limmit 
above_limit = []
for category, amount in expenses.items():
    if amount > expense_limit:
        above_limit.append(category)
if not above_limit:
    print("No individual expenses are above your limit.")
else:
    print(f"The expenses above your limit are: {','.join(above_limit)}")

#Check if total exceeds limit 
if total_expenses > expense_limit:
    print("Your total expenses exceed your limit. Consider reducing your spending.")
else: 
    print("Your total expenses are within your limit. Good job!")
