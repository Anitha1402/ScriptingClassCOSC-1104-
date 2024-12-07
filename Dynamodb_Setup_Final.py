"""
Author: Anita Mohan
Date: December 6, 2024
Description: This script sets up a DynamoDB table named 'Expenses' to store expense data.
"""

import boto3

# Creates the Expenses table in DynamoDB with a primary key 'ExpenseID'.
def create_expense_table():

    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table_name = 'Expenses'

    existing_tables = boto3.client('dynamodb', region_name='us-east-1').list_tables()['TableNames']

    if table_name in existing_tables:
        print(f"Table {table_name} already exists.")
        return

    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {'AttributeName': 'ExpenseID', 'KeyType': 'HASH'},
        ],
        AttributeDefinitions=[
            {'AttributeName': 'ExpenseID', 'AttributeType': 'S'},
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    print(f"Creating table {table_name}...")
    table.wait_until_exists()
    print(f"Table {table_name} created successfully.")

if __name__ == "__main__":
    create_expense_table()
