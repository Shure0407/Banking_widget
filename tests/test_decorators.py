import pytest

from typing import Any

import os

from src.decorators import log


@log(None)
def test_function_ok(a: int, b: int) -> float:
    """Функция, которая успешно складывает два числа."""
    return a + b


@log(filename="test_log_tmp.log")
def test_function_fail(a: int, b: int) -> float:
    """Функция, которая вызывается с ошибкой деления на ноль."""
    return a / b


@log(None)
def test_function_str_ok(a: str, b: str) -> str:
    """Функция, которая успешно соединяет две строки."""
    return a + b


def test_log_to_console_str(capsys: Any) -> Any:
    """Функция проверки вывода в консоль"""
    test_function_str_ok("hello", "world")
    captured = capsys.readouterr()
    assert "Функция test_function_str_ok ok. Результат: helloworld\n" in captured.out


def test_log_to_console(capsys: Any) -> Any:
    """Проверяем, что без filename логи выводятся в консоль"""
    test_function_ok(2, 3)

    captured = capsys.readouterr()
    assert "Функция test_function_ok ok. Результат: 5" in captured.out


def test_log_to_file() -> None:
    """Функция проверки записи в файл"""
    # Проверяем, что если есть filename - логи записываются в файл
    log_file_path = "test_log_tmp.log"

    # Удаляем файл, если он уже есть
    if os.path.exists(log_file_path):
        os.remove(log_file_path)

    with pytest.raises(ZeroDivisionError):
        test_function_fail(5, 0)

    assert os.path.exists(log_file_path)

    with open(log_file_path, "r", encoding="utf-8") as f:  # Проверяем содержимое файла
        data = f.read()
    assert "test_function_fail error: division by zero. Inputs: (5, 0), {}" in data

    # По окончании теста можно удалить временный файл
    if os.path.exists(log_file_path):
        os.remove(log_file_path)
