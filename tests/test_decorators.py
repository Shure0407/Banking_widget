import pytest

from typing import Any

import os

from src.decorators import log


@log(None)
def function_ok(a: int, b: int) -> float:
    """Функция, которая успешно складывает два числа."""
    return a + b


@log(filename="test_log_tmp.log")
def function_ok_filename(a: int, b: int) -> float:
    """Функция, которая успешно умножает два числа."""
    return a * b


@log(filename="test_log_tmp.log")
def function_fail(a: int, b: int) -> float | None:
    """Функция, которая вызывается с ошибкой деления на ноль."""
    return a / b


@log(None)
def function_str_ok(a: str, b: str) -> str:
    """Функция, которая успешно соединяет две строки."""
    return a + b


def test_log_to_console_str(capsys: Any) -> Any:
    """Функция проверки вывода в консоль"""
    function_str_ok("hello", "world")
    captured = capsys.readouterr()
    assert "Функция: function_str_ok ok. Результат: helloworld\n" in captured.out


def test_log_to_console(capsys: Any) -> Any:
    """Проверяем, что без filename логи выводятся в консоль"""
    function_ok(2, 3)
    captured = capsys.readouterr()
    assert "Функция: function_ok ok. Результат: 5" in captured.out


def test_log_to_file() -> Any:
    """Функция проверки записи в файл"""
    # Проверяем, что если есть filename - логи записываются в файл
    log_file_path = "test_log_tmp.log"

    # Удаляем файл, если он уже есть
    if os.path.exists(log_file_path):
        os.remove(log_file_path)

    with pytest.raises(ZeroDivisionError):
        function_fail(5, 0)

    assert os.path.exists(log_file_path)

    with open(log_file_path, "r", encoding="utf-8") as f:  # Проверяем содержимое файла
        data = f.read()
    assert "function_fail error: division by zero. Inputs: (5, 0), {}" in data

    # По окончании теста можно удалить временный файл
    if os.path.exists(log_file_path):
        os.remove(log_file_path)

    """Функция проверки записи в файл"""
    function_ok_filename(4, 5)
    with open(log_file_path, "r", encoding="utf-8") as f:  # Проверяем содержимое файла
        data_1 = f.read()
    assert "Функция: function_ok_filename ok. Результат: 20" in data_1