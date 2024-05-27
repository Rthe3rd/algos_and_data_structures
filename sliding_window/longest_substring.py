# 3. Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.



def longest_substring(string):
    # loop through each of the letters in the string
    # first pointer moves along to each letter
    # second moves once you find something that has already been in the set
    check_set = set()
    left = 0
    consecutive_count = 0
    for right in range(len(string)):
        # if we find a character that we've already seen, we need to remove characters the left most portion of the string from our checkset
        # since the string must be continous.  Continue removing values from the set until the duplicate value is found/removed. Could be the first
        # removal, could be many! 
        while string[right] in check_set:
            check_set.remove(string[left])
            # move the left side of our window over 1
            left += 1
        # if we haven't seen this character, add it
        check_set.add(string[right])
        # update the running max for each letter
        consecutive_count = max(consecutive_count, right - left + 1)
    return consecutive_count


s1 = "abcabcbb"
# Output: 3

s2 = "bbbbb"
# Output: 1

s3 = "pwwkew"
# Output: 3

s4 = "cabcadefg"

print(longest_substring(s1))
# print(longest_substring(s2))
# print(longest_substring(s3))
print(longest_substring(s4))