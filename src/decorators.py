from functools import wraps


def log(filename=None):
    """декоратор, который будет автоматически логировать начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""

    def decoretor(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
                result_try = f"{function.__name__} ok"
                if filename is None:
                    print(f"{result_try}")
                elif filename is not None:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{result_try}\n")
                return result

            except Exception as e:
                result_error = (
                    f"{function.__name__} error: {e}. Inputs: {args}, {kwargs}"
                )
                if filename is None:
                    print(f"{result_error}")
                elif filename is not None:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{result_error}\n")

        return wrapper

    return decoretor


@log()
def my_function(x, y):
    return x / y


my_function(4, 2)
