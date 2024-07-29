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

    def merge_k_sorted_lists(self, lists):
        # edge cases
        if not lists or len(lists) == 0:
            return None
        while len(lists) > 1:
            merged_lists = []
            # loop in pairs with edge case if you have an odd lengthed list
            for i in range(0, len(list), 2):
                list_1 = lists[i]
                list_2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(self.merge_two_sorted_lists(list_1, list_2))
            lists = merged_lists
        return merged_lists[0]

    def merge_two_sorted_lists(list_1, list_2):
        dummy = ListNode()
        current = dummy
        while list_1 and list_2:
            if list_1.val < list_2.val:
                current.next = list_1 
            else:
                current.next = list_2 
                list_2 = list_2.next
            current = current.next  
        if list_1:
            current.next = list_1
        if list_2:
            current.next = list_2
        return dummy.next
    
    def reverse_nodes_in_k_groups(self, head, k):
        # edge cases
        if not head or not head.next:
            return head
        # pointers/nodes that will reverse portions of the list
        # dummy node
        dummy = ListNode(None, head)
        # will need a pointer that points to the node right before the start of the group that is being reversed
        group_prev = dummy

        while True:
            kth = self.get_kth(group_prev, k)
            if not kth:
                break
            group_next = kth.next

            # reverse group
            prev = kth.next
            current = group_prev.next
            while current != group_next:
                ahead = current.next
                current.next = prev
                prev = current
                current = ahead
            # first node in our group
            temp = group_prev.next
            # put kth at the beginning of the group
            group_prev.next = kth
            group_prev = temp
        return dummy.next

    # Helper to get the kth node
    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

linked_list = LinkedList(1)
linked_list.add_node(2)
linked_list.add_node(3)
linked_list.add_node(4)
linked_list.add_node(5)
print(linked_list.reverse_nodes_in_k_groups(linked_list.head, 1))
print('+++++++++')
linked_list.print_nodes()