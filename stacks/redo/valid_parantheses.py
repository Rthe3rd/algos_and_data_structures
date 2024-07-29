def isValid(input_string):
    matching_hash = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    stack = []
    for element in input_string:
        if element in matching_hash:
            if not stack:
                return False
            if matching_hash[element] != stack[-1]:
                return False
            stack.pop()
        else:
            stack.append(element)
    if stack:
        return False
    return True


s1 = "()"
# Output: true

s2 = "()[]{}"
# Output: true

s3 = "(]"
# Output: false

print(isValid(s1))
print(isValid(s2))
print(isValid(s3))