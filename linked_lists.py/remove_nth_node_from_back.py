# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        # create a dummy and point it's .next to the head
        dummy = ListNode()
        dummy.next = head
        ahead = head

        # move ahead to the nth position
        # for _ in range(n):
        while n > 0 and ahead:
            ahead = ahead.next
            n -= 1 

        #  WHILE ahead is not None, move all pointers up
        before = dummy
        current = head
        while ahead:
            before = before.next
            ahead = ahead.next

        before.next = before.next.next 
        
        return dummy.next

        
        