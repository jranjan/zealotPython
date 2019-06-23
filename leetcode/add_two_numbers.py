# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = l3p = None
        carry = 0
        l1p = l1
        l2p = l2
        while l1p != None and l2p != None:            
            d = (l1p.val + l2p.val) % 10             
            n = ListNode(d+carry)
            n.next = None
            if l3 is None:
                l3 = n
            else:
                l3p.next = n
            l3p = n
            carry =  (l1p.val + l2p.val) / 10 
            l1p = l1p.next
            l2p = l2p.next
            
        leftover = l1p if l1p != None else l2p
        if leftover is None and carry != 0:
            n = ListNode(carry)
            if l3 is None:
                l3 = n
            else:
                l3p.next = n   
                
        while leftover != None:
            d = ListNode(leftover.val+carry)
            if l3 is None:
                l3 = n
            else:
                l3p.next = n
            leftover = leftover.next
        return l3
