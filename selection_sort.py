import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


# selection sort logic
def selection_sort(a):
    """
    Sort array using selection sort
    :param a: Array
    :return: Sorted Array
    """
    try:
        for i in range(len(a) - 1):

            # declaring variable min to store index of minimum valued element
            minimum = i

            for j in range(i + 1, len(a)):

                # comparing if current element is less than the element at index min or not
                if a[j] < a[minimum]:
                    minimum = j

            # swap logic
            a[i], a[minimum] = a[minimum], a[i]
        return a
    except Exception as err:
        print(err)


if __name__ == "__main__":
    try:
        array = list(map(int, input("Enter integer separated by spaces : ").strip().split()))
        logging.info("Integer list accepted successfully")
        print("Array is : ", array)
        print("Selection sorted array is : ", selection_sort(array))
    except Exception as e:
        print(e)
        logging.exception(e)
