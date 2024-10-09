class Solution:
    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        # candles array
        candles = []
        results = []
        # get an array where each candles index is tracked
        for i in range(len(s)):
            if s[i] == "|": candles.append(i) 

        # perform binary search with eacb query
        for left_query, right_query in queries:
            left_most_candle = -1
            right_most_candle = -1

            # left/right pointers are the boundary of the candles array
            left, right = 0, len(candles) - 1

            # find the left most candle inside
            while left <= right:
                mid_point = (left + right) // 2
                if candles[mid_point] >= left_query:
                    right = mid_point - 1
                    left_most_candle = mid_point
                else:
                    left = mid_point + 1

            left, right = 0, len(candles) - 1
            # find the right most candle
            while left <= right:
                mid_point = (left + right) // 2
                if candles[mid_point] <= right_query:
                    left = mid_point + 1
                    right_most_candle = mid_point
                else:
                    right = mid_point - 1

            # number_candles = distance between left/right most candles - the amount of candles between them
            if (left_most_candle != -1 and right_most_candle != -1) and (right_most_candle > left_most_candle):
                results.append((candles[right_most_candle] - candles[left_most_candle]) - (right_most_candle - left_most_candle))
            else:
                results.append(0)

        return results



# Output: [2,3]
# Output: [9,0,0,0,0]

solution1 = Solution()
print(solution1.platesBetweenCandles(s = "**|**|***|", queries = [[2,5],[5,9]]))

# Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]




