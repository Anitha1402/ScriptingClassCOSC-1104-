"""
Author: Anita Mohan
Date: December 6, 2024
Description: Flask API server for managing expenses and calculating user balances.
"""

from flask import Flask, request, jsonify
from expense_logic import add_expense, calculate_balances

app = Flask(__name__)

# API endpoint to add a new expense.
# Expects JSON input with 'expense_id', 'payer', 'amount', and 'split_with'.

@app.route('/add_expense', methods=['POST'])
def add_expense_endpoint():
    
    data = request.json
    expense_id = data['expense_id']
    payer = data['payer']
    amount = data['amount']
    split_with = data['split_with']

    result = add_expense(expense_id, payer, amount, split_with)
    return jsonify({'message': result})

#API endpoint to get user balances.
# Returns a dictionary of balances for all users.
@app.route('/get_balances', methods=['GET'])
def get_balances_endpoint():
    
    balances = calculate_balances()
    return jsonify({'balances': balances})

if __name__ == "__main__":
    app.run(debug=True)
