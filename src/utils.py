import json
import logging
from typing import Any

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    filename="logs/utils.log",
    encoding="utf-8",
    filemode="w",
)  # Перезапись файла при каждом запуске

utils_logger = logging.getLogger(__name__)


def load_transactions(path: str) -> Any:
    """Функция, которая принимает на вход путь к json файлу и
    возвращает список словарей с данными о финансовых транзакциях"""

    try:
        with open(path, "r", encoding="utf-8") as tr:
            content = tr.read()
            if not content.strip():
                utils_logger.error("json файл не имеет строк, пустой")
                return []
            data = json.loads(content)
            if not isinstance(data, list):
                utils_logger.error("файл не содержит список")
                return []
            utils_logger.info("преобразование json файла в формат python")
            return data

    except FileNotFoundError:
        utils_logger.error("файл в формате json не найден")
        print("Файл не найден:")
        return []


# data_tr = utils.load_transactions('C:/Users/Aleksandr/PycharmProjects/PythonProject/data/operations.json')
