import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)


# merge sort logic
def merge_sort(a):
    """
    Sort array elements using merge sort
    :param a: Array
    :return: Sorted Array
    """
    try:
        # if length of array is greater than 1 then only proceed
        if len(a) > 1:

            # finding middle element index
            mid = len(a) // 2

            # left subarray is from index 0 to middle element - 1
            left_subarray = a[:mid]

            # right subarray is from middle element till last
            right_subarray = a[mid:]

            # merge sort left and right subarrays
            merge_sort(left_subarray)
            merge_sort(right_subarray)

            # declaring variables i, j and k for indexing purpose
            i = j = k = 0

            # comparing each element in both sub arrays and placing them at their correct position
            while i < len(left_subarray) and j < len(right_subarray):
                if left_subarray[i] < right_subarray[j]:
                    a[k] = left_subarray[i]
                    i += 1
                else:
                    a[k] = right_subarray[j]
                    j += 1
                k += 1

            # copying the remaining elements in the array
            while i < len(left_subarray):
                a[k] = left_subarray[i]
                i += 1
                k += 1
            while j < len(right_subarray):
                a[k] = right_subarray[j]
                j += 1
                k += 1
    except Exception as err:
        print(err)


if __name__ == "__main__":
    try:
        array = list(map(int, input("Enter integer separated by spaces : ").strip().split()))
        logging.info("Integer list accepted successfully")
        print("Array is : ", array)
        merge_sort(array)
        print("Merge sorted array is : ", array)
    except Exception as e:
        print(e)
        logging.exception(e)
