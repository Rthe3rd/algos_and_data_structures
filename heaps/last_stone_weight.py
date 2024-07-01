# class Solution(object):
import heapq
def lastStoneWeight(stones):
    """
    :type stones: List[int]
    :rtype: int
    """
    stones = [-x for x in stones]
    heapq.heapify(stones)
    while len(stones) > 1:
        y = heapq.heappop(stones)
        x = heapq.heappop(stones)
        if x != y:
            remaining_stone = abs(y) - abs(x)
            heapq.heappush(stones, -remaining_stone)
    if len(stones) == 1:
        return -1*stones[0]
    return 0


stones1 = [2,7,4,1,8,1]
stones1 = [2,2,2,2,2,24]
stones1 = [2,2,2,2,2,2]
print(lastStoneWeight(stones1))




        