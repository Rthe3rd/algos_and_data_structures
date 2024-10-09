class SnapshotArray:

    def __init__(self, length: int):
        # set up data scructures to hold histories and snap_id
        self.histories = [[[-1, 0]] for val in range(length)] #[[], [], [], [], [] ...]
        self.snap_id = 0


    def set(self, index: int, val: int) -> None:
        self.histories[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        # given an index and snap id, return the most recent value
        # binary searching on the snap_id at the given index of histories

        # Initialize right/left pointers and return variable
        left = 0
        right = len(self.histories[index]) - 1
        position = -1

        # while-loop
        while left <= right:
            # initialize mid_point for each iteration
            mid_point = (left + right) // 2

            # self.histories[index][mid][0] => the snap_id of the mid_point "pair" at index "index"
            if self.histories[index][mid_point][0] <= snap_id:
                left = mid_point + 1
                position = mid_point
            else:
                right = mid_point - 1

        return self.histories[index][position][1]
