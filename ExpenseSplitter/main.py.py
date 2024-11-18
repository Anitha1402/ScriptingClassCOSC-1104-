# Author: Anita Mohan (100884879)
# Date: November 17, 2024

import yaml
import sys
from tabulate import tabulate

 # Reads the YAML file containing expense details.
def read_expenses(file_path):
   
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Validates the expense data for consistency.
def validate_expenses(data):
    people = set(data['people'])
    for payer, expenses in data['expenses'].items():
        if payer not in people:
            raise ValueError(
                f"Error: When setting the names under 'expenses', the name '{payer}' must match a name under 'people'."
            )
        for expense_name, expense_details in expenses.items():
            split_with = expense_details.get('split_with', people)  # Default to everyone if 'split_with' not provided
            invalid_names = [name for name in split_with if name not in people]
            if invalid_names:
                raise ValueError(
                    f"Error: The following names in 'split_with' are not valid (CASE SENSITIVE):\n - {', '.join(invalid_names)}\n"
                    "Double-check the names in the 'split_with' section and ensure they match names defined under 'people'."
                )

# Calculates how much each person owes or is owed.
def calculate_balances(data):
    
    people = data['people']
    balances = {person: 0 for person in people}

    for payer, expenses in data['expenses'].items():
        for expense_name, details in expenses.items():
            amount = details['amount']
            split_with = details.get('split_with', people)
            split_count = len(split_with)
            share = amount / split_count

            # Update balances
            balances[payer] += amount
            for person in split_with:
                balances[person] -= share

    return balances

# Prints the details of each person's expenses.
def print_expense_details(data):
    
    print("===============\nExpense Details\n===============")
    for person, expenses in data['expenses'].items():
        if expenses:
            print(f"{person} has spent:")
            for expense_name, details in expenses.items():
                split_with = details.get('split_with', data['people'])
                split_with_str = f" (split with: {', '.join(split_with)})" if split_with else ""
                print(f" - ${details['amount']} on {expense_name}{split_with_str}")
        else:
            print(f"{person} has no expenses")

# Prints the balances of each person.
def print_balances(balances):
    
    print("=========================\nGroup Debt/Credit Totals\n=========================")
    for person, balance in balances.items():
        if balance > 0:
            print(f"{person} is receiving ${balance:.2f} from the group.")
        elif balance < 0:
            print(f"{person} owes ${-balance:.2f} to the group.")
        else:
            print(f"{person} is settled with the group.")

#  Suggests who should pay whom to settle balances.
def print_payouts(balances):
    
    print("=========================\nGroup Payout Information\n=========================")
    creditors = [(person, balance) for person, balance in balances.items() if balance > 0]
    debtors = [(person, -balance) for person, balance in balances.items() if balance < 0]

    creditors.sort(key=lambda x: x[1], reverse=True)
    debtors.sort(key=lambda x: x[1], reverse=True)

    for debtor, debt_amount in debtors:
        while debt_amount > 0:
            creditor, credit_amount = creditors.pop(0)
            payment = min(debt_amount, credit_amount)
            print(f" - {debtor.upper()} pays {creditor.upper()} ${payment:.2f}")
            debt_amount -= payment
            credit_amount -= payment
            if credit_amount > 0:
                creditors.insert(0, (creditor, credit_amount))

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_yaml_file>")
        sys.exit(1)

    file_path = sys.argv[1]

    try:
        data = read_expenses(file_path)
        validate_expenses(data)
        balances = calculate_balances(data)

        print("======\nGroup Expense Splitter Script\n========")
        print(f"Reading expenses from {file_path}")
        print("Validating the expense names to match name defined under people...")
        print("Validating the expenses to ensure names are referenced correctly..")
        print("Adding up expenses for each person...")
        print_expense_details(data)
        print(f"The group has spent a total of: ${sum(balances.values()):.2f}")
        print_balances(balances)
        print_payouts(balances)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
