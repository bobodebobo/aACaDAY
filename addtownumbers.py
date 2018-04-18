# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def jie(self, l, ll, carry):
        while(l or carry):
            if l == None:
                ll.next = ListNode(carry)
                carry = 0
                break
            ll.next = ListNode((l.val + carry)%10)
            if int((l.val + carry)/10):
                carry = 1
            else:
                carry = 0
            ll = ll.next
            l = l.next
            
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = l3 = ListNode(0)
        carry = 0
        while(l1 != None and l2 != None):
            l3.next = ListNode((l1.val+l2.val+carry)%10)
            l3 = l3.next
            if int((l1.val+l2.val+carry)/10):
                carry = 1
            else:
                carry = 0
            l1 = l1.next
            l2 = l2.next
            
        if l1 == None and l2 == None:
            self.jie(l1, l3, carry)
            return head.next
        if l2 == None:
            self.jie(l1, l3, carry)
        if l1 == None:
            self.jie(l2, l3, carry)   
        return head.next
