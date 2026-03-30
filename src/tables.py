# import os.path

import pandas as pd

import csv

import logging


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    filename="logs/tables.log",
    encoding="utf-8",
    filemode="w",
)  # Перезапись файла при каждом запуске

tables_logger = logging.getLogger(__name__)


def tables_csv(path_csv: str) -> list:
    """Функция, которая принимает на вход путь к csv файлу и
    выдает список словарей с транзакциями"""

    try:
        with open(path_csv, mode="r", encoding="utf-8") as file:
            reader_csv = csv.DictReader(file, delimiter=";")
            if not reader_csv:
                tables_logger.error("csv файл не имеет строк, пустой")
                return []
            data_csv = [row for row in reader_csv]
            return data_csv
    except FileNotFoundError:
        tables_logger.error("файл в формате csv не найден")
        print("Файл csv не найден:")
        return []


def tables_excel(path_excel: str) -> list[dict]:
    """Функция, которая принимает на вход путь к excel файлу и
    выдает список словарей с транзакциями"""

    try:
        reader_excel = pd.read_excel(path_excel, engine="openpyxl")
        if reader_excel.empty:
            tables_logger.error("excel файл не имеет строк, пустой")
            return []
        data_ex = reader_excel.to_dict(orient="records")
        return data_ex
    except FileNotFoundError:
        tables_logger.error("файл в формате excel не найден")
        print("Файл excel не найден:")
        return []
