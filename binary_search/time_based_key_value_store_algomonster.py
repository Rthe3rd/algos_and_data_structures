class TimeMap:

    def __init__(self):
        self.histories = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.histories:
            self.histories[key] = []
        self.histories[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        left, right = 0, len(self.histories[key]) - 1
        position = -1
        while left <= right:
            mid_point = (left + right) // 2

            if self.histories[key][mid_point][0] <= timestamp:
                left = mid_point + 1
                position = mid_point

            else:
                right = mid_point - 1
        
        if position != -1: 
            return self.histories[key][position][1]
        return ""

    

["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

timemap1 = TimeMap()
timemap1.set("foo", "bar", 1)
timemap1.get("foo", 1)