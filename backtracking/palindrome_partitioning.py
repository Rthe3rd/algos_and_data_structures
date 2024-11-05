def parition(s):
    results = []
    current_partition = []
    min_count = [len(s)]
    current_count = [0]

    def dfs_helper(i):

        if i >= len(s):
            results.append(current_partition.copy())
            # min_count[0] = min(min_count[0], current_count[0])
            return

        # starting at the current index, check to see if all of the remaining substrings are palidroms
        for j in range(i, len(s)):
            # check if the current substring is a palindrome
            # if it is, add it to the current partition
            if isPalindrome(s, i, j):
                current_partition.append(s[i:j+1])
                dfs_helper(j + 1)
                current_partition.pop()

    def isPalindrome(s, i , j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        # current_count[0] += 1
        return True
    dfs_helper(0)

    for pal_list in results:
        min_count[0] = min(len(pal_list), min_count[0])

    return results, min_count

print(parition(s = "aaab"))
print(parition(s = "aab"))
print(parition(s = "aa"))
print(parition(s = "a"))