import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


# prime number logic
def prime_number(number):
    try:
        flag = False
        if number == 2:
            print(number, " is prime number")
            return

        if number > 2:
            # for loop start from 2 till number / 2
            for i in range(2, int(number / 2)):
                if number % 2 == 0:
                    flag = True
                    break
            if flag:
                print(number, " is not a prime number")
            else:
                print(number, " is a prime number")
        else:
            print("Entered number is less than 2")
    except Exception as err:
        print(err)


if __name__ == "__main__":
    try:
        integer = int(input("Enter integer to check whether it is prime or not : "))
        prime_number(integer)
    except Exception as e:
        print(e)
        logging.exception(e)
