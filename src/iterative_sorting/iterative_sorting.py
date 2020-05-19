# TO-DO: Complete the selection_sort() function below
# def selection_sort(arr):
#     # * track the current index
#     current = 0
#     # ? while current index is less than the length of the array - 1
#     while current < len(arr) - 1:
#         smallest = current
#         # * for i in range starting at current (adding 1), up to the length of the array
#         for i in range(current + 1, len(arr)):
#             # * keep track of smallest by going through the array
#             # * if smallest is greater than i, smallest now equals i
#             if arr[smallest] > arr[i]:
#                 smallest = i
#         # ! the loop has finished, smallest now represents the lowest value from current until the end of the array
#         # * swap the values of current with smallest
#         arr[current], arr[smallest] = arr[smallest], arr[current]
#         # * we have completed all steps for that index, now do it again until we reach the end of the array
#         current += 1
#     # * we have reached the end of the array, return array
#     return arr


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for x in range(cur_index + 1, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x
            # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    for i in range(0, len(arr) - 1):
        print(i, "[i TOP LEVEL]")
        for j in range(0, len(arr) - 1 - i):
            print(j, "[J SECOND]")
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


arr = [1, 4, 6, 2, 7, 9, 55]
print(bubble_sort(arr))


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here

    return arr
