import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


# function to return output
def power_of_two(power):
    """
    Function implements power of 2
    :param power: till which power we want output
    :return: power of 2
    """
    try:
        # for loop starting from 0 till a - 1
        for i in range(0, power + 1):
            # to calculate power
            print("2 ^ ", i, " : ", 2 ** i)
    except Exception as err:
        print(err)


if __name__ == "__main__":
    try:
        number = int(input("Enter he power of two till you want the output : "))
        print("Power of two are")
        power_of_two(number)
    except Exception as e:
        print(e)
        logging.warning(e)
