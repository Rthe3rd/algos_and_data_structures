def dailyTemperatures(temperatures):
    res_stack = [0]*len(temperatures)
    check_stack = []
    for index, value in enumerate(temperatures):
        while check_stack and check_stack[-1][0] < value:
            temperature_index =  check_stack.pop()
            prev_index = temperature_index[1]
            res_stack[prev_index] = index - prev_index 
        check_stack.append([value, index])
    return res_stack

temperatures1 = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

temperatures2 = [30,40,50,60]
# Output: [1,1,1,0]

temperatures3 = [30,60,90]
# Output: [1,1,0]

print(dailyTemperatures(temperatures1))
print(dailyTemperatures(temperatures2))
print(dailyTemperatures(temperatures3))