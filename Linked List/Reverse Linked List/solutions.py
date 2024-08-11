'''
Author: qufeng107 qufeng107@gmail.com
Date: 2024-08-11 15:33:28
LastEditors: qufeng107 qufeng107@gmail.com
LastEditTime: 2024-08-11 17:06:20
FilePath: /Algorithms/Linked List/Reverse Linked List/solutions.py
Description: 

Copyright (c) 2024 by ${git_name_email}, All Rights Reserved. 
'''




# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# traverse linked list and reverse list
class Solution1(object):
    def reverseBookList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        reverse_list = []

        # treverse linked list and save value into a list
        while (head is not None):
            reverse_list.append(head.val)
            head = head.next
        
        # reverse list
        return reverse_list[::-1]
    

# recursion
class Solution2(object):
    def reverseBookList(self, head):
        
        # boundary
        if not head:
            return []
        
        # recurse
        else:
            return self.reverseBookList(head.next) + [head.val]