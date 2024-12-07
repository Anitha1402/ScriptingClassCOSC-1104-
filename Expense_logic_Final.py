"""
Author: Anita Mohan
Date: December 6, 2024
Description: Contains the logic to add expenses to DynamoDB and calculate user balances.
"""

import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('Expenses')

# Adds an expense record to the Expenses DynamoDB table.
def add_expense(expense_id, payer, amount, split_with):
   
    table.put_item(
        Item={
            'ExpenseID': expense_id,
            'Payer': payer,
            'Amount': amount,
            'SplitWith': split_with
        }
    )
    return f"Expense {expense_id} added successfully."

# Calculates and returns balances for all users based on the stored expenses.
def calculate_balances():
    
    response = table.scan()
    items = response['Items']

    balances = {}
    for item in items:
        payer = item['Payer']
        amount = item['Amount']
        split_with = item['SplitWith']

        if payer not in balances:
            balances[payer] = 0
        balances[payer] += amount

        share = amount / len(split_with)
        for person in split_with:
            if person not in balances:
                balances[person] = 0
            balances[person] -= share

    return balances
