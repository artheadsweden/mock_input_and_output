import unittest.mock


def my_func():
    return "something else"


def main():
    mock = unittest.mock.MagicMock()
    mock.return_value = '54'

    print(mock())
    mock.side_effect = my_func
    print(mock())


if __name__ == '__main__':
    main()
