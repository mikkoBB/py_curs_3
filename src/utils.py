import json
import re
from datetime import datetime


def get_operations():
    with open("operations.json", "r", encoding='utf-8-sig') as f:
        operations = json.load(f)
    return operations


def get_sorted_operations():
    operate_ = []
    i = get_operations()
    for operation in i:
        if operation.get("state") == 'EXECUTED' and operation.get('date'):
            operate_.append(operation)
        sorted_operations = sorted(
            operate_,
            key=lambda i: i.get('date'), reverse=True)
    return sorted_operations[:5]


def get_sent(sender):
    if sender:
        data = sender.split()
        if data[0] == "Счет":
            return encode_account(data)
        else:
            return encode_card(data)
    return ""


def encode_account(data):
    account_num = '**' + data[-1][-4:]
    return data[0] + ' ' + account_num


def encode_card(data):
    payment_system = ' '.join(data[:-1]) + ' '
    card_name = data[-1]
    card_number = card_name[0:4] + ' ' + card_name[5:7] + '** ****' + card_name[12:]
    return payment_system + card_number


def print_date(source_date):
    try:
        datatime = datetime.fromisoformat(source_date)
        return datatime.strftime('%d.%m.%Y')
    except ValueError:
        return '<invalid date format>'
    return datatime







