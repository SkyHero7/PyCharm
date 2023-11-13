import json
date_iso = '2023-11-12T18:05:44.081292'

from datetime import datetime


def format_card_number(card_number):
    return f'{card_number[:4]} {card_number[4:8]} ** {card_number[-4:]}'

def format_account_number(account_number):
    return f'**{account_number[-4:]}'

def convert_date(date: str):
    date_datetime = datetime.fromisoformat(date)
    date_datetime
    datetime.datetime(2023, 11, 12, 18, 5, 44, 81292)
    executed_operations = [op for op in operations if op.get('state') == 'EXECUTED']
    last_5_operations = sorted(executed_operations, key=lambda x: datetime.strptime(x.get('date'), '%d.%m.%Y'),
                               reverse=True)[:5]
# def display_last_operations(operations):
#     executed_operations = [op for op in operations if op.get('state') == 'EXECUTED']
#     last_5_operations = sorted(executed_operations, key=lambda x: datetime.strptime(x.get('date'), '%d.%m.%Y'), reverse=True)[:5]

    for operation in last_5_operations:
        print(f"{operation.get('date')} {operation.get('description')}")
        print(f"{format_card_number(operation.get('from'))} -> {format_account_number(operation.get('to'))}")
        print(f"{operation.get('amount')} {operation.get('currency')}\n")

#
with open('operations.json', 'r', encoding='utf-8') as file:
    operations = json.load(file)

convert_date(operations)
