#Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from queue import PriorityQueue
class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return
        a = PriorityQueue()
        while(head):
            a.put(head.val)
            head = head.next
        tou = n = ListNode(0)
        while not a.empty():
            n.next = ListNode(a.get())
            n = n.next
        return tou.next

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        midn = mid = last = head
        while last != None and last.next != None and last.next.next != None:
            mid = mid.next
            midn = midn.next
            last = last.next.next
        midn = midn.next
        mid.next = None
        l1 = self.sortList(head)
        l2 = self.sortList(midn)
        return self.merge(l1, l2)
    
    def merge(self, l1, l2):
        l = p = ListNode(0)
        while l1 != None and l2 != None:
            if l1.val > l2.val:
                p.next = l2
                p = p.next
                l2 = l2.next
            else:
                p.next = l1
                p = p.next
                l1 = l1.next
        if l1 == None and l2 == None:
            return l.next
        while l1 != None:
            p.next = l1
            l1 = l1.next
            p = p.next
        while l2 != None:
            p.next = l2
            l2 = l2.next
            p = p.next
        return l.next
