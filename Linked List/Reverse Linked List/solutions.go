/*
 * @Author: qufeng107 qufeng107@gmail.com
 * @Date: 2024-08-11 17:05:35
 * @LastEditors: qufeng107 qufeng107@gmail.com
 * @LastEditTime: 2024-08-11 21:07:51
 * @FilePath: /Algorithms/Linked List/Reverse Linked List/solutions.go
 * @Description:
 *
 * Copyright (c) 2024 by ${git_name_email}, All Rights Reserved.
 */

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

// recursion
func reverseBookList1(head *ListNode) []int {

	if head == nil {
		return []int{}
	}

	return append(reverseBookList(head.Next), head.Val)

}

// traverse linked list to get length, traverse linked list again to get value
func reverseBookList2(head *ListNode) []int {

	length := 0
	tempHead := head
	for tempHead != nil {
		length++
		tempHead = tempHead.Next
	}

	reverse_list := make([]int, length)
	for i := 1; head != nil; i++ {
		reverse_list[length-i] = head.Val
		head = head.Next
	}

	return reverse_list

}