# Given a sorted linked list, delete all duplicates such that each element appear only once.
#
# Example 1:
#
# Input: 1->1->2
# Output: 1->2
# Example 2:
#
# Input: 1->1->2->3->3
# Output: 1->2->3



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head

        c = head
        cnxt = head.next
        while cnxt != None:
            if c.val == cnxt.val:
                c.next = cnxt.next
                cnxt = c.next
            else:
                c = c.next
                cnxt = cnxt.next

        return head
