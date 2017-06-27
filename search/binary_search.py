#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
二分查找 Binary Search
'''

from datetime import datetime
import math


def simple_search(list, item):
    '''
    Simple search
    O(n)

    :param list:
    :param item:
    :return:
    '''
    start_time = datetime.now().timestamp()
    times = 0

    for ele in list:
        times += 1
        if ele == item:
            end_time = datetime.now().timestamp()
            print('total times: {}, {} ms'.format(times, (end_time - start_time) * 1000))
            return item


def binary_search(list, item):
    '''
    Binary search
    O(log2n)

    :param list:
    :param item:
    :return:
    '''
    start_time = datetime.now().timestamp()

    low = 0
    high = len(list) - 1
    times = 0

    while low <= high:
        times += 1
        mid = (low + high) / 2
        mid = int(mid)
        guess = list[mid]

        if guess == item:
            end_time = datetime.now().timestamp()
            print('total times: {}, {} ms'.format(times, (end_time - start_time) * 1000))
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


def binary_simple_rate(max):
    '''
    Calculate the rate between binary search and simple search
    O(n) / O(log2n)

    :param max: int
    :return: float
    '''
    return max / math.log2(max)


my_list = list(range(1000))
print(simple_search(my_list, 591))
print(binary_search(my_list, 591))

print(binary_simple_rate(10000))
