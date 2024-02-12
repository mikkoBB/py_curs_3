import json
import os
import re
from config import ROOT_DIR
from datetime import datetime

DATA_DIR = os.path.join(ROOT_DIR, "src", "operations.json")


def get_operations():
    """
    Загружает список операций из файла
    """
    with open(DATA_DIR, "r", encoding='utf-8-sig') as f:
        operations = json.load(f)
    return operations


def get_sorted_operations():
    """
    Сортирует операции по дате и результату и оставляет последние 5
    """
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
    """
    Проверяет отправителя и счета или карты по операциям
    """
    if sender:
        data = sender.split()
        if data[0] == "Счет":
            return encode_account(data)
        else:
            return encode_card(data)
    return ""


def encode_account(data):
    """
    Скрывает номер счет операции
    """
    account_num = '**' + data[-1][-4:]
    return data[0] + ' ' + account_num


def encode_card(data):
    """
    Скрывает номер карты
    """
    payment_system = ' '.join(data[:-1]) + ' '
    card_name = data[-1]
    card_number = card_name[0:4] + ' ' + card_name[4:6] + '** ****' + ' ' + card_name[12:]
    return payment_system + card_number


def print_date(source_date):
    """
    Переводит дату операции в другой формат
    """
    try:
        data_time = datetime.fromisoformat(source_date)
        return data_time.strftime('%d.%m.%Y')
    except ValueError:
        return '<invalid date format>'










