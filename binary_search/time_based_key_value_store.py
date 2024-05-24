# 981. Time Based Key-Value Store
# Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

# Implement the TimeMap class:

# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".


class TimeMap(object):

    def __init__(self):
        self.time_map = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.time_map:
            self.time_map[key] = [[timestamp, value]]
        else:
            self.time_map[key].append([timestamp, value])
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        if key not in self.time_map:
            return ""
        left = 0
        right = len(self.time_map[key]) - 1
        timestamp_prev = ''

        while left <= right:
            mid_point = (right + left) // 2
            if self.time_map[key][mid_point][0] == timestamp:
                return self.time_map[key][mid_point][1]
            if self.time_map[key][mid_point][0] < timestamp:
                timestamp_prev = self.time_map[key][mid_point][1]
                left = mid_point + 1
            else:
                right = mid_point - 1
        return timestamp_prev


timeMap = TimeMap()
timeMap.set('foo', 'bar', 1)

print(timeMap.get('foo', 1))
print(timeMap.get('foo', 3))
timeMap.set('foo', 'bar2', 4)
print(timeMap.get('foo', 4))
print(timeMap.get('foo', 5))