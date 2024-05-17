# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type. 

def is_Valid(input_string):
    if len(input_string) == 0:
        return True
    stack = []
    matching_hash = {"(" : ")", "{" : "}", "[": "]"}
    for character in input_string:
        if character == "(" or character == "[" or character == "{":
            stack.append(character)
        else:
            if len(stack) == 0:
                return False
            if matching_hash[stack[-1]] != character:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False