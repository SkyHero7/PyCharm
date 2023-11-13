import json


def get_last_operations(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    operations = data['operations']
    executed_operations = [op for op in operations if op['state'] == 'EXECUTED']
    last_executed_operations = sorted(executed_operations, key=lambda x: x['date'], reverse=True)[:5]

    result = []
    for op in last_executed_operations:
        date = op['date']
        description = op['description']
        from_account = op.get('from', '')
        to_account = op['to'][-4:]
        amount, currency = op['operationAmount'].split()

        masked_from_account = '**** **** **** ' + from_account[-4:] if from_account else ''

        output = f"{date} {description}\n{masked_from_account} -> **{to_account}\n{amount} {currency}\n"
        result.append(output)

    return '\n'.join(result)


file_path = 'utils/operations.json'
print(get_last_operations(file_path))