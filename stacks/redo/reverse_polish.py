import math
def reversePolish(tokens):
    operation_hash = {"+","-","*","/"}
    operand_stack = []
    operator_stack = []
    if len(tokens) == 1:
        return tokens[0]
    for element in tokens:
        if not element in operation_hash:
            operand_stack.append(int(element))
        else:
            second_operand = operand_stack.pop()
            first_operand = operand_stack.pop()
            if element == '+':
                carry = first_operand + second_operand
            if element == '-':
                carry = first_operand - second_operand
            if element == '*':
                carry = first_operand * second_operand
            if element == '/':
                carry = int(first_operand / second_operand)
            operand_stack.append(carry)
    return operand_stack.pop()


tokens1 = ["2","1","+","3","*"]
tokens2 = ["4","13","5","/","+"]
tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

print(reversePolish(tokens1))
print(reversePolish(tokens2))
print(reversePolish(tokens3))