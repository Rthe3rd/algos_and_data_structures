def letterCombinations(self, digits: str) -> list[str]:
    digits_to_char = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    combinations = ['']

    for digit in digits:
        # match the index of the digits_to_char list
        digit = int(digit) - 2
        possible_chars = digits_to_char[digit]
        
        print(f'combinations before: {combinations}')
        combinations = [prefix + letter for prefix in combinations for letter in possible_chars]
        print(f'combinations after: {combinations}')
        print(f'===================================')

    return combinations

print(letterCombinations('holder', '23'))
