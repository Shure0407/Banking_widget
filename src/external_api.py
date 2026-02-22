import os

from dotenv import load_dotenv

import requests


load_dotenv(".env")

api_key: str | None = os.getenv("API_KEYN")

headers = {"apikey": api_key}


def conversion(data_fin: dict) -> float | None:
    """Функция, которая принимает на вход транзакцию и возвращает сумму транзакции в рублях"""

    if data_fin["operationAmount"]["currency"]["code"] == "RUB":
        sum_ru = float(data_fin["operationAmount"]["amount"])
        return sum_ru

    elif data_fin["operationAmount"]["currency"]["code"] == "USD":
        sum_us = str(data_fin["operationAmount"]["amount"])
        to = "RUB"
        from_us = "USD"
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_us}&amount={sum_us}"
        resp_us = requests.get(url, headers=headers)
        response_us = resp_us.json()
        result_us = float(response_us["result"])
        return result_us

    elif data_fin["operationAmount"]["currency"]["code"] == "EUR":
        sum_eur = str(data_fin["operationAmount"]["amount"])
        to = "RUB"
        from_eur = "EUR"
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_eur}&amount={sum_eur}"
        resp_eur = requests.get(url, headers=headers)
        response_eur = resp_eur.json()
        result_eur = float(response_eur["result"])
        return result_eur

    else:
        return None
