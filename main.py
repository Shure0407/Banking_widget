# from src import masks

# from src import widget

# from src import processing

# from src import generators

# from src import decorators

# from src import utils

# from src import external_api

from src import tables

# import os

# import requests


# account_or_card = input('''Введите номер карты или счета: ''')

# if len(account_or_card) == 16 and account_or_card.isdigit():
#     card_num = masks.get_mask_card_number(account_or_card)
#     print(card_num)
# elif len(account_or_card) == 20 and account_or_card.isdigit():
#     card_acc = masks.get_mask_account(account_or_card)
#     print(card_acc)
# else:
#     masks.get_mask_card_number(account_or_card)
#     masks.get_mask_account(account_or_card)
#
# data_json = utils.load_transactions('C:/Users/Aleksandr/PycharmProjects/PythonProject/data/operation.json') # полный файл
# data_json = utils.load_transactions('C:/Users/Aleksandr/PycharmProjects/PythonProject/data/operations_three_trans.json') # файл с тремя транзакциями
# data_json = utils.load_transactions('C:/Users/Aleksandr/PycharmProjects/PythonProject/data/operations_not_list.json') # файл не содержит список
# data_json = utils.load_transactions("C:/Users/Aleksandr/PycharmProjects/PythonProject/data/operations_empty.json") # пустой файл
# print(data_json)

# for data in data_json:
#      result_conv = external_api.conversion(data)
#      print(result_conv)

# data_csv = tables.tables_csv('C:/Users/Aleksandr/PycharmProjects/PythonProject/data/transactions.csv')
# data_csv = tables.tables_csv('C:/Users/Aleksandr/PycharmProjects/PythonProject/data/transactions_three_str.csv')
# data_csv = tables.tables_csv('C:/Users/Aleksandr/PycharmProjects/PythonProject/data/transactions_not_list.csv')
# data_csv = tables.tables_csv('C:/Users/Aleksandr/PycharmProjects/PythonProject/data/transactions_empty.csv') # пустой файл
# print(data_csv)

# data_excel = tables.tables_excel('C:/Users/Aleksandr/PycharmProjects/PythonProject/data/transactions_excel.xlsx')
data_excel = tables.tables_excel('C:/Users/Aleksandr/PycharmProjects/PythonProject/data/transactions_excel_three_str.xlsx')
# data_excel = tables.tables_excel('C:/Users/Aleksandr/PycharmProjects/PythonProject/data/transactions_not_list.xlsx')
# data_excel = tables.tables_excel('C:/Users/Aleksandr/PycharmProjects/PythonProject/data/transactions_excel_empty.xlsx') # пустой файл
print(data_excel)
account_details = str()
time_event = str()

widget.mask_account_card(account_details)
widget.get_date(time_event)

transactions: list[dict] = []
state = ()
sort = ()

processing.filter_by_state(transactions, state)
processing.sort_by_date(transactions, sort)

