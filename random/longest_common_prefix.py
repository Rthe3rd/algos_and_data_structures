# 14. Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

# Example 1:
strs1 = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
strs2 = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings
strs3 = ["reflower","flow","flight"]


# class Solution(object):
def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
# find the shortest string in the given strings
# iterate backwards through the string
# create a substring with the moving index
# check if the current sub-string is in all of the strings, starting at 0:length of sub-string -1
# return if sub-string true
# else continue iterating backwards
    min_length = len(strs[0])
    min_string = strs[0]
    for string in strs:
        if min_length > len(string):
            min_length = len(string) 
            min_string = string 

    for i in range(min_length - 1, -1, -1):
        current_substring = min_string[0:i+1]
        in_all = True
        for string in strs:
            if current_substring not in string[0:len(current_substring)]:
                in_all = False
        if in_all:
            return current_substring
    return 'None!'


print(longestCommonPrefix(strs1))
print(longestCommonPrefix(strs2))
print(longestCommonPrefix(strs3))
