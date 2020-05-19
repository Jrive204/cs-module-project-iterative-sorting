# Print out each element of the following array on a separate line:
# ['Joe', 2, 'Ted', 4.98, 14, 'Sam', 'void *', '42', 'float', 'pointers', 5006]
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any
# code. Run through the UPER problem solving framework while going through
# your thought process.
import collections
import itertools
import functools
import operator

#     joe   \n    2   \n   fed
# Print out each element of the following array on a separate line, but
# this time the input array can contain arrays nested to an arbitrarily
# deep level:
arr = ['Bob', 'Slack', ['reddit', '89', 101, ['alacritty', ('brackets'), 5, 375]], 0, [
    {'slice', 'owned'}], 22]


flatten = lambda *n: (e for a in n for e in (flatten(*a)
                                             if isinstance(a, (tuple, list)) else (a,)))


def flat(*args):
    return (e for a in args
            for e in (flat(*a)
                      if isinstance(a, (tuple, list)) else (a,)))


# print(flat(arr))


arr = list(flat(arr, arr))


# arr = [
#     'Joe',
#     2,
#     'Ted',
#     4.98,
#     14,
#     'Sam',
#     'void *',
#     '42',
#     'float',
#     'pointers',
#     5006]

# a = functools.reduce(operator.iconcat, str(arr), [])
# print(a)

# for i in arr:
#     for x in i:
#         print(x)


for i in arr:
    print(f'{i}')


# def my_print(arr):
#     for element in arr:
#         if isinstance(element, list):
#             my_print(element)
#         else:
#             print(element)


# my_print(arr)
