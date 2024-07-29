def generate_parantheses(n):
    # how to build the parantheses => recursion?
        # what is the base case?
    valid_params = []
    current_pattern = []

    def gen_helper(number_open, number_closed):
        if number_open == number_closed == n: # base case!
            valid_params.append("".join(current_pattern))
            return
        if number_open < n:
            current_pattern.append(('('))
            gen_helper(number_open + 1, number_closed)
            current_pattern.pop()

        if number_closed < number_open:
            current_pattern.append(')')
            gen_helper(number_open, number_closed + 1)
            current_pattern.pop()
    
    gen_helper(0, 0)
    return valid_params


print(generate_parantheses(1))
print(generate_parantheses(2))
print(generate_parantheses(3))

