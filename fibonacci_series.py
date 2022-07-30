import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


# fibonacci series logic
def fibonacci_series(nth_term):
    """
    Function implements fibonacci series
    :param nth_term: how many terms we want
    :return: fibonacci series till the n th tern
    """
    try:
        first = 0
        second = 1
        next_number = first + second
        if nth_term > 2:
            print(first, second, end=" ")
            for i in range(3, term + 1):
                if i == term:
                    print(next_number)
                else:
                    print(next_number, end=" ")
                    first = second
                    second = next_number
                    next_number = first + second
        else:
            print("Entered integer is either negative or too small")
    except Exception as err:
        print(err)


if __name__ == "__main__":
    try:
        term = int(input("Enter how many fibonacci terms do you want : "))
        fibonacci_series(term)
    except Exception as e:
        print(e)
        logging.exception(e)
