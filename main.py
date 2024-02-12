import os
import json
from config import ROOT_DIR
from datetime import datetime
from src.utils import get_sorted_operations, get_sent, print_date

DATA_DIR = os.path.join(ROOT_DIR, "src", "operations.json")


def main():
    """
    Программа выводит 5 последних операций в нужном формате
    """
    print("Вывести 5 последних выполненных операций, нажать 'Enter'")
    user_input = input()

    x = get_sorted_operations()
    for operation in x:
        print(print_date(operation.get('date')), operation.get('description'))
        print(f"{get_sent(operation.get('from'))} -> {get_sent(operation.get('to'))}")
        print(operation.get('operationAmount').get('amount'), operation.get('operationAmount').get('currency').get('name'))
        print()


if __name__ == '__main__':
    main()


