class ListNode():
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        previous = None
        carry = 0
        c1 = l1
        c2 = l2
        dummy = ListNode()
        summed_node = dummy

        while c1 or c2 or carry:
            # calculate the next digit
            val1 = c1.val if c1 else 0
            val2 = c2.val if c2 else 0
            
            # calculate the sum and carry
            total = val1 + val2 + carry
            node_value = total % 10
            carry = total // 10
            summed_node.next = ListNode(node_value)

            # move the pointers
            summed_node = summed_node.next
            c1 = c1.next if c1 else None
            c2 = c2.next if c2 else None

        return dummy.next