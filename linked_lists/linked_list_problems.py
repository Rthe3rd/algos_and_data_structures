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

    def rotate_list(self, head, k):
        if not head or not head.next:
            return head

        # find the length of the list
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        # find the tail
        tail = head
        while tail.next:
            tail = tail.next

        # find how many times the nodes will move, taking into account possible cycle => k > length
        k =  k % length
        if not k:
            return head

        # move a pointer to where the new tail will be 
        new_tail = head
        for _ in range(length - k - 1):
            new_tail = new_tail.next

        # New head is the next node after the new_tail or "current"
        new_head = new_tail.next
        # point new_tail's next to null 
        new_tail.next = None
        # OLD will always point to the old head
        tail.next = head
        # return the NEW head
        return new_head.val

    def remove_duplicates_from_sorted_II(self, head):
        dummy = ListNode(-1, head)
        prev = dummy
        current = head
        # edge casesL empty list, list of 1
        if not head or not head.next:
            return head
        while current:
            while current.next and current.val == current.next.val:
                current = current.next
            if prev.next == current:
                prev = prev.next
                current = current.next
            else:
                prev.next = current.next
                current = prev.next
        return dummy.next

    def remove_duplicates_from_sorted_I(self, head):
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
                continue
            else:
                current = current.next
        return head

    def partition_list(self, head, x):
        current = head
        high_head = ListNode()
        high_tail = high_head
        low_head = ListNode()
        low_tail = low_head

        while current:
            if current.val < x:
                low_tail.next = current
                low_tail = low_tail.next
            else:
                high_tail.next = current
                high_tail = high_tail.next
            current = current.next

        high_tail.next = None
        low_tail.next = high_head.next
        return low_head.next
    
    def reverse_list_two(self, head, left, right):
        dummy = ListNode(None, head)
        left_prev = dummy
        current = head
        # find the position that current should go to
        for i in range(left - 1):
            left_prev = current
            current = current.next
        # reverse the links
        prev = None
        for i in range(right - left + 1):
            ahead = current.next
            current.next = prev
            prev = current
            current = ahead
        # update the pointers
        left_prev.next.next = current
        left_prev.next = prev
        return dummy.next
        

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

linked_list = LinkedList(1)
linked_list.add_node(2)
linked_list.add_node(3)
linked_list.add_node(4)
linked_list.add_node(5)
print(linked_list.reverse_list_two(linked_list.head, 1, 5))
print('+++++++++')
linked_list.print_nodes()