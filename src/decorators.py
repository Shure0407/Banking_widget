from datetime import datetime
from typing import Callable, Optional, Any


def log(filename: Optional[str]) -> Callable:
    """Декоратор log, который будет автоматически сохранять в лог начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки. Декоратор должен принимать необязательный аргумент filename,
    который определяет, куда будут записываться логи (в файл или в консоль): Если filename задан,
    логи записываются в указанный файл. Если filename не задан, логи выводятся в консоль."""

    def my_log_decorator(function: Callable) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                time_start = datetime.now().isoformat
                result = function(*args, **kwargs)
                time_end = datetime.now().isoformat
                name_function = function.__name__
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(
                            f"Начало: {time_start}\nФункция {name_function} ок. "
                            f"Результат: {result}\nКонец: {time_end}\n\n"
                        )
                    file.close()
                else:
                    print(f"Функция {name_function} ok. Результат: {result}")
                return result
            except Exception as err:
                name_function = function.__name__
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{name_function} error: {err}. Inputs: {args}, {kwargs}")
                    file.close()
                    return f"{name_function} error: {err}. Inputs: {args}, {kwargs}"
                else:
                    print(f"{name_function} error: {err}. Inputs: {args}, {kwargs}")
                # raise

        return wrapper

    return my_log_decorator
