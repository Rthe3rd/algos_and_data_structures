# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the above operations.


def longest_repeating_character_replacement(string, k):
    count = {}
    result = 0
    left = 0
    max_frequency = 0
    for right in range(len(string)):
        count[string[right]] = 1 + count.get(string[right], 0)
        max_frequency = max(max_frequency, count[string[right]])
        # Either loop is valid, max value does not need to be updated
        # while right - left + 1 - max(count.values()) > k:
        while (right - left + 1) - max_frequency > k:
            count[string[left]] -= 1
            left += 1            
        result = max(right - left + 1, result)
    return result

s1 = "ABAB" 
k1 = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

s2 = "AABABBA"
k2 = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.


print(longest_repeating_character_replacement(s1, k1))
print(longest_repeating_character_replacement(s2, k2))