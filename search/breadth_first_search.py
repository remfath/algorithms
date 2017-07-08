#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
# 广度优先搜索

from collections import deque


def breadth_first_search(queues):
    searched = []
    times = 0
    while queues:
        times += 1
        person = queues.popleft()
        if person in searched:
            continue
        searched.append(person)

        if check_is_target(person):
            print(person, "is the target person:", times)
            print(searched)
            return True
        else:
            queues += graph[person]
    return False


def check_is_target(name):
    return name[-1] == "o"


graph = {}
graph['me'] = ["chen", "cui"]

graph["chen"] = ["bing", "remfath"]
graph["bing"] = ["dang", "yue", "remfath"]
graph["remfath"] = []
graph["dang"] = ["yue"]
graph["yue"] = []

graph["cui"] = ["huan", "cuihuan"]
graph["cuihuan"] = []
graph["huan"] = ["tao", "hong"]

graph["tao"] = ["hong"]
graph["hong"] = []

search_queue = deque()
search_queue += graph["me"]

breadth_first_search(search_queue)
