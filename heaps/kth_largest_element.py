import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = nums

        # O(n)
        heapq.heapify(self.heap)
        
        # O((n-k)log(n))
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)


    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        # add value to heap
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

y = [[3,[4,5,8,2]],[3],[5],[10],[9],[4]]
obj = KthLargest(1, [5,3,2,1,4,5])
print(obj.add(11))
