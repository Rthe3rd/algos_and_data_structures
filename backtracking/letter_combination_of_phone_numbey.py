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

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        all_combinations  = []
        KEYBOARD = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def dfs_helper(start_index, path):
            if start_index == len(digits) :
                all_combinations.append("".join(path))
                return

            next_number = digits[start_index]
            for letter in KEYBOARD[next_number]:
                path.append(letter)
                dfs_helper(start_index + 1, path)
                path.pop()
        if not digits:
            return []
        dfs_helper(0, [])
        return all_combinations