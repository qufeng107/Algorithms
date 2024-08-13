'''
Author: qufeng107 qufeng107@gmail.com
Date: 2024-08-13 20:05:10
LastEditors: qufeng107 qufeng107@gmail.com
LastEditTime: 2024-08-13 20:14:07
FilePath: /Algorithms/Linked List/Intersection Linked Lists/solution.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# A + B = B + A
# A + B - C = B + A - C
class Solution1:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A = headA
        B = headB

        while True:
            if not A and not B:
                return None
            elif A == B:
                return A

            if not A:
                A = headB
            else:
                A = A.next
            
            if not B:
                B = headA
            else:
                B = B.next
            


# use hash set
class Solution2:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A = headA
        B = headB
        node_set = set()

        while A:
            node_set.add(A)
            A = A.next
        
        while B:
            if B in node_set:
                return B
            else:
                B = B.next
        
        return None
            