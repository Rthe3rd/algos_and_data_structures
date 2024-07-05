import heapq
def kClosest(points, k):
    """
    :type points: List[List[int]]
    :type k: int
    :rtype: List[List[int]]
    """
    minHeap = []
    heapq.heapify(minHeap)
    k_closest = []
    distance_coordinate_pair_hash = {}
    for coordinate_pair in points:
        distance = (coordinate_pair[0]**2 + coordinate_pair[1]**2)**(1/2)
        distance_coordinate_pair_hash[distance] = coordinate_pair
        heapq.heappush(minHeap, distance)

    for i in range(k):
        k_closest.append(distance_coordinate_pair_hash[heapq.heappop(minHeap)])

    return k_closest

points1 = [[1,3],[-2,2]]
k1 = 1

points2 = [[3,3],[5,-1],[-2,4]]
k2 = 2



# print(kClosest(points1, k1))
print(kClosest(points2, k2))
