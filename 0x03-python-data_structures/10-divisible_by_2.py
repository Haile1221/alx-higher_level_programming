#!/usr/bin/python3
def divisible_by_2(my_list=None):
    if my_list is None:
        my_list = []

    boolist = [True if i % 2 == 0 else False for i in my_list]
    return boolist
