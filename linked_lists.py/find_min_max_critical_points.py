class LinkedList(object):
    def __init__(self, val=None):
        new_node = ListNode(val)
        self.head = new_node
        self.length = 1

    def add_node(self, val):
        if self.length == 0:
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = ListNode(val)
        self.length += 1

    def print_nodes(self):
        current = self.head
        if not current:
            return 'no list!'
        while current:
            print('current node: ', current.val)
            current = current.next

    def nodesBetweenCriticalPoints(self, head):
        before = head
        current = before.next
        ahead = before.next.next
        node_number = 0
        critical_points_by_node_number = []
        if not ahead:
            return [-1, -1]
        while ahead:
            node_number += 1
            if current.val < before.val and current.val < ahead.val or current.val > before.val and current.val > ahead.val:
                critical_points_by_node_number.append(node_number)
            before = before.next
            current = current.next
            ahead = ahead.next
        if len(critical_points_by_node_number) < 2:
            return [-1,-1]
        min_distance = critical_points_by_node_number[-1] - critical_points_by_node_number[0] + 1
        for i in range(1, len(critical_points_by_node_number)):
            min_distance = min(critical_points_by_node_number[i] - critical_points_by_node_number[i-1], min_distance)
        return [min_distance, critical_points_by_node_number[-1] - critical_points_by_node_number[0]]

    def swapPairs(self, head):
        if not head:
            return []
        if not head.next:
            return head

        dummy = ListNode(0, head)
        current = head
        prev = dummy
        while current and current.next:
            # save a pointers we are going to change
            next_pair = current.next.next
            second = current.next
            
            # reverse nodes
            second.next = current
            current.next = next_pair
            prev.next = second

            # update pointers
            prev = current
            current = next_pair
        return dummy.next

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

linked_list = LinkedList(1)
linked_list.add_node(2)
linked_list.add_node(3)
linked_list.add_node(4)
linked_list.swapPairs(linked_list.head)
linked_list.print_nodes()