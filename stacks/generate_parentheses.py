# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# If open count is greater than closed count, you can add either
# If open count is equal to closed count, you can only add an open
# If the open/close count is less than 3, you can add an open/close

def generate_parantheses(n_pairs):

    stack = []
    results = []

    def assemble_parantheses(number_of_open, number_of_closed):
        if number_of_open == number_of_closed == n_pairs:
            results.append("".join(stack))
            return
        
        if number_of_open < n_pairs:
            stack.append("(")
            assemble_parantheses(number_of_open + 1, number_of_closed)
            stack.pop()

        if number_of_open > number_of_closed:
            stack.append(")")
            assemble_parantheses(number_of_open, number_of_closed + 1)
            stack.pop()

    assemble_parantheses(0, 0)

    return results


print(generate_parantheses(1))