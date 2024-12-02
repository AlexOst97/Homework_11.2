from src.decorators import log


def test_log_1(capsys):
    @log()
    def my_function(x, y):
        return x / y

    my_function(4, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"

    my_function(4, 0)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: division by zero. Inputs: (4, 0), {}\n"


def test_log_2(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(5, 6)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"

    my_function(4, "x")
    captured = capsys.readouterr()
    assert (
        captured.out
        == "my_function error: unsupported operand type(s) for +: 'int' and 'str'. Inputs: (4, 'x'), {}\n"
    )
