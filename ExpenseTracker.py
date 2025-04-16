import csv
import matplotlib.pyplot as plt

# Function to add an expense
def add_expense(filename, date, category, amount):
    with open(filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    print("Expense added successfully!")

# Function to view all expenses
def view_expenses(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        print("Date       | Category     | Amount")
        print("-----------------------------------")
        for row in reader:
            print(f"{row[0]}   | {row[1]:<12} | {row[2]}")

# Function to visualize expenses by category
def visualize_expenses(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        categories = {}
        for row in reader:
            category = row[1]
            amount = float(row[2])
            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount
        
        plt.bar(categories.keys(), categories.values())
        plt.title("Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount")
        plt.show()

# Main program
if __name__ == "__main__":
    filename = 'expenses.csv'
    
    while True:
        print("\nExpense Tracker")
        print("1. Add an Expense")
        print("2. View All Expenses")
        print("3. Visualize Expenses")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            add_expense(filename, date, category, amount)
        elif choice == '2':
            view_expenses(filename)
        elif choice == '3':
            visualize_expenses(filename)
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")