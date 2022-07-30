import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


# bubble sort logic
def bubble_sort(a):
    """
    sort elements in array using bubble sort
    :param a: Array
    :return: Sorted Array
    """
    try:
        # loop till less than length of array a - 1
        for i in range(len(a) - 1):
            swapped = False
            for j in range(len(a) - i - 1):

                # comparing if current element is greater than next element or not
                if a[j] > a[j + 1]:
                    # swap logic
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swapped = True

            # if no element in the list is swapped then break the loop
            if not swapped:
                break
        return a
    except Exception as err:
        print(err)


if __name__ == "__main__":
    try:
        array = list(map(int, input("Enter integer separated by spaces : ").strip().split()))
        logging.info("Integer list accepted successfully")
        print("Array is : ", array)
        print("Bubble sorted array is : ", bubble_sort(array))
    except Exception as e:
        logging.exception(e)
