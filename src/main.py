import json
from datetime import datetime
from src import utils
from utils import get_sorted_operations
from utils import print_date
from utils import get_sent

def main():
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


