/*
 * @Author: qufeng107 qufeng107@gmail.com
 * @Date: 2024-08-11 17:05:35
 * @LastEditors: qufeng107 qufeng107@gmail.com
 * @LastEditTime: 2024-08-11 17:05:56
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

func reverseBookList(head *ListNode) []int {

	if head == nil {
		return []int{}
	}

	return append(reverseBookList(head.Next), head.Val)

}