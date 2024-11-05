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


def generate_p(n):
    results = []
    current_path = []

    def dfs(start_index, number_open, number_closed):
        if start_index == n * 2:
            results.append("".join(current_path))
            return

        if number_open < n:
            current_path.append("(")
            dfs(start_index + 1, number_open + 1, number_closed)
            current_path.pop()

        if number_open > number_closed:
            current_path.append(")")
            dfs(start_index + 1, number_open, number_closed + 1)
            current_path.pop() 

    dfs(0, 0 ,0)

    return results

print(generate_p(1))
print(generate_p(2))
print(generate_p(3))