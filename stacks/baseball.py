def calPoints(operations):
    """
    :type operations: List[str]
    :rtype: int
    """
    # just have an array
    stack = []
    # integer "x" => add "x" to the stack [x1, x2, x3, ...] => stack.append(x)
    for element in operations:
        if isinstance(int(element), int):
            stack.append(element)
    # + sign => append(stack.pop() + stack.pop())
        elif element == '+':
            new_score = stack[-1] + stack[-2]
            stack.append()
    # "D" => append(2*stack.pop()) 
        elif element == 'D':
            stack.append(2*stack[-1]) 
    # "C" => stack.pop()
        # elif element == 'C':
            # stack.pop()
    return stack


operations = ["5","2","C","D","+"]
print(calPoints(operations))