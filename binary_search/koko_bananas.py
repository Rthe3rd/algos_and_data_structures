# 875. Koko Eating Bananas
# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.
import math

def koko_bananas(piles, h):

    # fastest koko would have to eat is max value of piles
    # slowest koko could eat is 1
    # perform a binary search between these values to find the possible k in which you can consume all bananas within h

    max_k = max(piles)

    left = 1
    right = len(piles) - 1
    range_of_rates = list(range(1,  max_k + 1))
    min_k = max_k

    while left <= right:
        mid_point = (right + left) // 2
        # How do you calculate the total time to consume all bananas in the piles?
        time_to_consume_bananas = 0 
        for index, value in enumerate(piles):
            time_to_consume_bananas += math.ceil(value / range_of_rates[mid_point])
        if time_to_consume_bananas <= h:
            right = mid_point - 1
            min_k = min(min_k, mid_point)
        else:
            left = mid_point + 1

    return range_of_rates[min_k]



piles1 = [3,6,7,11]
h1 = 8
# Output: 4

piles2 = [30,11,23,4,20]
h2 = 5
# Output: 30

piles3 = [30,11,23,4,20]
h3 = 6
# Output: 23

print(koko_bananas(piles1, h1))