import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


def division_by_zero_exception():
    """
    Function implements divide by zero exception handling
    :return: exception
    """
    try:
        print(5/0)
    except ZeroDivisionError as err:
        print(err)
        logging.error(err)


def invalid_literal_exception():
    """
    Function implements type exception handling
    :return: exception
    """

    try:
        number = int(input("Enter an integer : "))
        print("Entered integer is : ", number)
    except Exception as err:
        print(err)
        logging.warning(err)


if __name__ == "__main__":
    division_by_zero_exception()
    invalid_literal_exception()
