package main

import (
	"fmt"
	"time"
)

func simple_search(list []int, item int) bool {
	start := time.Now()
	times := 0
	for _, val := range list {
		times ++
		if val == item {
			run_time := time.Since(start)
			fmt.Println("Simple search: loop", times, "times, total", run_time , ", found", item)
			return true
		}
	}
	run_time := time.Since(start)
	fmt.Println("Simple search: loop", times, "times, total", run_time , ", not found")
	return false
}

func binary_search(list []int, item int) bool {
	start := time.Now()
	times := 0
	low_index := 0
	high_index := len(list) - 1
	for low_index <= high_index {
		times++
		middle_index := int((low_index + high_index) / 2)
		guess := list[middle_index]
		if guess == item {
			run_time := time.Since(start)
			fmt.Println("Simple search: loop", times, "times, total", run_time , ", found", item)
			return true
		}
		if guess > item {
			high_index = middle_index - 1
		} else {
			low_index = middle_index + 1
		}
	}
	run_time := time.Since(start)
	fmt.Println("Simple search: loop", times, "times, total", run_time , ", not found")
	return false
}

func main() {
	list := []int{}
	for i := 1; i <= 1000000; i++ {
		list = append(list, i)
	}
	item := 380060
	simple_search(list, item)
	binary_search(list, item)
}
