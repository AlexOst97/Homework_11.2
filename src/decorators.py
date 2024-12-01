from functools import wraps


def log(filename="mylog.txt"):
    """декоратор, который будет автоматически логировать начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""

    def decoretor(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
                print(f"{function.__name__} ok")
                with open("record_result.txt", "a") as file:
                    file.write(f"{function.__name__} ok - result: {result}\n")
            except Exception as e:
                print(f"{function.__name__} error: {e}. Inputs: {args}, {kwargs}")
                with open("record_result.txt", "a") as file:
                    file.write(
                        f"{function.__name__} error: {e}. Inputs: {args}, {kwargs}\n"
                    )

        return wrapper

    return decoretor


@log(filename="mylog.txt")
def my_function(x, y):
    return x / y


my_function(4, 0)
