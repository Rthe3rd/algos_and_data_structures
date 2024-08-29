class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []

        right_bound = len(matrix[0])
        down_bound = len(matrix)
        left_bound = 0
        up_bound = 0

        while left_bound < right_bound and up_bound < down_bound:   

            for i in range(left_bound, right_bound):
                result.append(matrix[up_bound][i])
            up_bound += 1

            for i in range(up_bound, down_bound):
                result.append(matrix[i][right_bound - 1])
            right_bound -= 1

            if not(left_bound < right_bound and up_bound < down_bound):
                break

            for i in range(right_bound - 1, left_bound -1, -1):
                result.append(matrix[down_bound-1][i])
            down_bound -= 1

            for i in range(down_bound - 1, up_bound - 1, -1):
                result.append(matrix[i][left_bound])
            left_bound += 1

        return result

print(Solution.spiralOrder(1, matrix = [[1,2,3],[4,5,6],[7,8,9]]))
