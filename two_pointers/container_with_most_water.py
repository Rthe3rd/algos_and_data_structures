# Max area: Find the max area between to values in an list, where the area is defined as the lower of the two values multiplied by the distance between indices
import math

def max_area(height):
    if not height:
        return 0
    left = 0 
    right = len(height) - 1
    global_max = 0
    while left < right:
        current_area = (right - left) * (min(height[right], height[left]))
        global_max = max(current_area, global_max)
        if height[left] < height[right]:
            left += 1
        elif height[left] > height[right]:
            right -= 1
        else:
            left += 1
            right -= 1
    return global_max

height = [1,8,6,2,5,4,8,3,7]
# height = [1,1]
print(max_area(height))