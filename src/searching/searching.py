def linear_search(arr, target):
    # Your code here
    for index, element in enumerate(arr):
        if element == target:
            return index

    return -1   # not found


arr1 = [-2, 7, 3, -9, 5, 1, 0, 4, -6]

print(list(enumerate(arr1)))

# Write an iterative implementation of Binary Search


def binary_search(arr, target):
    # let's figure out the total size of the arr
    left = 0
    right = len(arr) - 1

    while left <= right:
        # find the midpoint
        mid = (left + right) // 2

        # check to see if the midpoint element is our target
        if arr[mid] == target:
            return mid

        # check to see if the element should be on the left or right side
        # of our midpoint
        if arr[mid] < target:
            # toss out the left side of the arr
            # update our `left` index
            left = mid + 1

        # otherwise, arr[mid] > target
        else:
            # toss out the right side of the arr because the element has to be
            # on the left side
            right = mid - 1

    # we didn't find the element

    return -1  # not found
