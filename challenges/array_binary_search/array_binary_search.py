def binary_search(lst, target):

    lst.sort()
    left = 0
    right = len(lst) - 1

    while (left < right):
        mid = (left + right) // 2
        # if left == right:
        #     return -1
        if (lst[mid] == target):
            return mid
        elif (lst[mid] < target):
            left = mid + 1
        elif (lst[mid] > target):
            right = mid - 1
    return -1
