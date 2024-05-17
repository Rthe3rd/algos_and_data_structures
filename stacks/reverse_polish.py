# 150. Evaluate Reverse Polish Notation
# Attempted
# Medium
# Topics
# Companies
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.


def reverse_notation(tokens):
    operands = []
    current_total = 0
    for i in range(len(tokens)):
        value = tokens[i]
        if value != '-' and value != '+' and value != '*' and value != '/':
            value = int(value)
            operands.append(value)
        else:
            second_operand = operands.pop()
            first_operand = operands.pop()
            if tokens[i] == "+":
                current_total = first_operand + second_operand
            if tokens[i] == "-":
                current_total = first_operand - second_operand
            if tokens[i] == "*":
                current_total = first_operand * second_operand
            if tokens[i] == "/":
                current_total = int(first_operand / second_operand)
            operands.append(current_total)

    return operands[0]

print(reverse_notation(["2","1","+","3","*"]))
print(reverse_notation(["4","13","5","/","+"]))
print(reverse_notation(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(reverse_notation(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(reverse_notation(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))