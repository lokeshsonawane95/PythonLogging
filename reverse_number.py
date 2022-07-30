import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


# number reversal logic
def reverse_number(number):
    """
    Function implements reversal of an integer
    :param number: integer
    :return: reversed integer
    """
    try:
        reverse = 0
        while number != 0:
            reverse *= 10
            reverse += number % 10
            number = int(number / 10)
        print("Reversed number is : ", reverse)
    except Exception as err:
        print(err)


if __name__ == "__main__":
    try:
        integer = int(input("Enter an integer to reverse : "))
        reverse_number(integer)
    except Exception as e:
        print(e)
        logging.exception(e)
