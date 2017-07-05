#!/bin/env python3
# -*- encoding: utf-8 -*-


def quick_sort(arr):
    '''
    Quick sort

    :param arr:
    :return:
    '''
    if len(arr) < 2:
        return arr
    pivot = arr[0]

    arr.remove(pivot)
    big_arr = []
    small_arr = []
    for item in arr:
        if item >= pivot:
            big_arr.append(item)
        else:
            small_arr.append(item)
    return quick_sort(small_arr) + [pivot] + quick_sort(big_arr)


def quick_sort2(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    big_arr = [item for item in arr[1:] if item >= pivot]
    small_arr = [item for item in arr[1:] if item < pivot]
    return quick_sort2(small_arr) + [pivot] + quick_sort2(big_arr)


arr = [12, 3, 2, 99, 20, 44, 7]
print(quick_sort2(arr))
