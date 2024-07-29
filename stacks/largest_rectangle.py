def largestRectangle(heights):
    indices_heights_stack = [] # pair of elements: index and height  
    max_area = 0

    for index, height in enumerate(heights):
        if len(indices_heights_stack) == 0:
            indices_heights_stack.append([index, height])
        else:
            start = index
            while indices_heights_stack and height < indices_heights_stack[-1][1]:
                current_index, current_height = indices_heights_stack.pop()
                max_area = max(max_area, (index - current_index) * current_height)
                start = current_index
            indices_heights_stack.append([start, height])
    for bar in indices_heights_stack:
        max_area = max(max_area, (len(heights) - bar[0]) * bar[1])

    return max_area


heights1 = [2,1,5,6,2,3]
heights2 = [2,4]
heights3 = [3,6,5,7,4,8,1,0]

print(largestRectangle(heights1))
print(largestRectangle(heights2))
print(largestRectangle(heights3))