import json
from datetime import datetime
from utils import sorted_operations


def main():
    print("Вывести 5 последних выполненных операций, нажать 'Enter'")
    user_input = input()
    last_transactions = get_sorted_operations()
    x = transaction
    for x in last_transactions:
        print(print_date(x.get('date')), x.get('description'))
        print(f"{get_sent(x.get('from'))} -> {get_sent(x.get('to'))}")
        print(x.get('operationAmount').get('amount'), x.get('operationAmount').get('currency').get('name'))
        print()


if __name__ == '__main__':
    main()
