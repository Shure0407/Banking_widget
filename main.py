from src import masks

# from src import widget

# from src import processing

# from src import generators

# from src import decorators

from src import utils

# from src import external_api

# import os

# import requests


account_or_card = input('''Введите номер карты или счета: ''')

if len(account_or_card) == 16 and account_or_card.isdigit():
    card_num = masks.get_mask_card_number(account_or_card)
    print(card_num)
elif len(account_or_card) == 20 and account_or_card.isdigit():
    card_acc = masks.get_mask_account(account_or_card)
    print(card_acc)
else:
    masks.get_mask_card_number(account_or_card)
    masks.get_mask_account(account_or_card)

data_tr = utils.load_transactions('C:/Users/Aleksandr/PycharmProjects/PythonProject/data/operation.json') # полный файл
# data_tr = utils.load_transactions('C:/Users/Aleksandr/PycharmProjects/PythonProject/data/123.json') # файл с тремя транзакциями
# data_tr = utils.load_transactions('C:/Users/Aleksandr/PycharmProjects/PythonProject/data/11.json') # файл не содержит список
# data_tr = utils.load_transactions("C:/Users/Aleksandr/PycharmProjects/PythonProject/data/1.json") # пустой файл
# print(data_tr)

# for data in data_tr:
#      result_conv = external_api.conversion(data)
#      print(result_conv)
account_details = str()
time_event = str()

widget.mask_account_card(account_details)
widget.get_date(time_event)

transactions: list[dict] = []
state = ()
sort = ()

processing.filter_by_state(transactions, state)
processing.sort_by_date(transactions, sort)

