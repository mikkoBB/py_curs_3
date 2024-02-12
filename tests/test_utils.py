import pytest
import os.path
import json
from config import ROOT_DIR
from src.utils import get_operations, get_sent, get_sorted_operations, print_date
from datetime import datetime

DATA_DIR = os.path.join(ROOT_DIR, "src", "operations.json")


def test_get_operations():
    operations = get_operations()
    assert type(operations) == list


def test_get_sorted_operations():
    sorted_operations = get_sorted_operations()
    assert type(sorted_operations) == list


def test_encode_account():
    assert get_sent("Счет 77613226829885488381") == "Счет **8381"
    assert get_sent("Счет 90424923579946435907") == "Счет **5907"
    assert get_sent("Счет 43241152692663622869") == "Счет **2869"
    assert get_sent("Счет 35158586384610753655") == "Счет **3655"
    assert get_sent("Счет 38611439522855669794") == "Счет **9794"
    assert get_sent("Счет 46765464282437878125") == "Счет **8125"


def test_encode_card():
    assert get_sent("Maestro 7810846596785568") == "Maestro 7810 84** **** 5568"
    assert get_sent("Visa Classic 2842878893689012") == "Visa Classic 2842 87** **** 9012"


def test_get_sent():
    assert get_sent(None) == ""


def test_print_date():
    assert print_date("2019-12-08T22:46:21.935582") == "08.12.2019"
    assert print_date("2019-12-07T06:17:14.634890") == "07.12.2019"
    assert print_date("2019-11-19T09:22:25.899614") == "19.11.2019"
    assert print_date("2019-11-05T12:04:13.781725") == "05.11.2019"
    assert print_date("2019-11-13T17:38:04.800051") == "13.11.2019"
    assert print_date("08.12.2019") == '<invalid date format>'








