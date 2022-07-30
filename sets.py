import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


def sets():
    """
    Function implements set
    :return: operation performed on set
    """
    try:
        a = {2, 3, 5, 7}
        b = {1, 3, 5}
        print("Set a is : ", a)
        print("Set b is : ", b)
        print("a | b : ", a | b)
        print("a & b : ", a & b)
        print("a - b : ", a - b)
        print("b - a : ", b - a)
        print("a ^ b : ", a ^ b)
    except Exception as err:
        print(err)
        logging.exception(err)


if __name__ == "__main__":
    print("Set operations are")
    sets()
