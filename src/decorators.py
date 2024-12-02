from functools import wraps


def log(filename=None):
    """декоратор, который будет автоматически логировать начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""

    def decoretor(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                function(*args, **kwargs)
                result = f"{function.__name__} ok"
                if filename is None:
                    print(f"{result}")
                elif filename is not None:
                    with open("record_result.txt", "a", encoding="utf-8") as file:
                        file.write(f"{result}\n")
                return result

            except Exception as e:
                result_e = f"{function.__name__} error: {e}. Inputs: {args}, {kwargs}"
                if filename is None:
                    print(f"{result_e}")
                elif filename is not None:
                    with open("record_result.txt", "a", encoding="utf-8") as file:
                        file.write(f"{result_e}\n")
                return result_e

        return wrapper

    return decoretor


@log(filename="mylog.txt")
def my_function(x, y):
    return x / y


my_function(1, 0)
