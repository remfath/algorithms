#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

def find_smallest(list):
    '''
    Find the smallest number in a list

    :param list:
    :return:
    '''
    smallest = list[0]
    smallest_index = 0
    for i in range(1, len(list)):
        if list[i] < smallest:
            smallest = list[i]
            smallest_index = i
    return smallest_index


def select_sort(list):
    '''
    Selection sort

    :param list:
    :return:
    '''
    new_list = []
    for i in range(len(list)):
        smallest_index = find_smallest(list)
        new_list.append(list.pop(smallest_index))
    return new_list


list = [11, 40, 45, 444, 2, 45]
print(find_smallest(list))
print(select_sort(list))
