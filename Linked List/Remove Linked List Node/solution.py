'''
Author: qufeng107 qufeng107@gmail.com
Date: 2024-08-14 21:36:46
LastEditors: qufeng107 qufeng107@gmail.com
LastEditTime: 2024-08-14 21:57:07
FilePath: /Algorithms/Linked List/Remove Linked List Node/solution.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution1:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # remove head
        while head is not None and head.val == val:
            head = head.next

        # check head
        if head is None:
            return None

        pointer = head

        while pointer.next is not None:

            if pointer.next.val == val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        
        return head




class Solution2:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # add a temp head
        temp_head = ListNode( next = head )
        pointer = temp_head

        while pointer.next is not None:

            if pointer.next.val == val:
                pointer.next = pointer.next.next
            else:
                pointer = pointer.next
        
        return temp_head.next


