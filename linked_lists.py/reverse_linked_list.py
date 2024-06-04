# Write Linked List and LLNode classes
# Create methods that solve the LL problems

# LL Node
class ListNode():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, value):
        new_node = ListNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def print_nodes(self):
        if self.head is None:
            return None
        current = self.head
        while current:
            print(current.value)
            current = current.next

class Solution(object):
    #     let current = head
    #     let previous = null

    # while(current){
    #     let temp = current.next
    #     current.next = previous
    #     previous = current
    #     current = temp
    # }
    # return previous  
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        before = None
        while current:
            after = current.next
            current.next = before
            before = current
            current = after
        return before
