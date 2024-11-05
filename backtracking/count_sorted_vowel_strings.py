class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1. how do we know if we reach a leaf node? 
        # 2. how do we branch, generate the tree?
        all_combinations = []
        def dfs_helper(start_index, path):
            # 1. how do we know if we reached a leaf node? Base case!
            if start_index == n:
                all_combinations.append("".join(path))
                return

            # 2. How do we generate?
            for letter in ["a", "e", "i", "o", "u" ]:
                path.append(letter)
                dfs_helper(start_index + 1, path)
                path.pop()

        dfs_helper(0, [])
        return all_combinations