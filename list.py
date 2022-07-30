import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


def list_operations():
    """
    Function implements normal list
    :return: operations performed on list data structure
    """
    try:
        # declaration of fruits list
        fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

        print("fruits list is : ", fruits)

        # counting apples in fruits list
        print("count of 'apple' in fruits list : ", fruits.count('apple'))

        # getting index of element 'banana'
        print("index of 'banana' in fruits list : ", fruits.index('banana'))

        # reverse fruits list
        fruits.reverse()
        print("Reversed fruits list is : ", fruits)

    except Exception as err:
        print(err)


def list_as_stack():
    """
    Function implements stack using list
    :return: operations performed on stack
    """
    try:
        # declaration of stack list
        stack = [3, 4, 5]
        print("Stack is : ", stack)

        # push operation
        stack.append(6)
        stack.append(7)
        logging.info("Append operation in list performed successfully")
        print("Stack after pushing 6 ans 7 onto is : ", stack)

        # pop operation
        stack.pop()
        stack.pop()
        logging.info("Pop operation from list performed successfully")
        print("Stack after popping top 2 elements is : ", stack)

    except Exception as err:
        print(err)


def list_as_queue():
    """
    Function implements queue using list
    :return: operations performed on queue
    """
    try:
        # importing deque class from collection package
        from collections import deque

        # declaring queue
        queue = deque(["Eric", "John", "Michael"])

        print("queue is : ", queue)

        # Enqueue operation
        queue.append("Terry")
        queue.append("Graham")
        logging.info("Append operation in queue performed successfully")
        print(queue)

        # deque operation (popping element from start)
        queue.popleft()
        print(queue)
        queue.popleft()
        logging.info("Popleft i.e. deque operation from queue performed successfully")
        print(queue)

    except Exception as err:
        print(err)
        logging.error(err)


if __name__ == "__main__":
    print("List operation are as follows")
    list_operations()

    print("\nStack operations using list are as follows")
    list_as_stack()

    print("\nQueue operation using list are as follows")
    list_as_queue()
