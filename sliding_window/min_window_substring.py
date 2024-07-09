import re
def minWindow(s, t):
    if len(s) < len(t):
        return ''

    left = 0
    right = 0
    current_matches = 0

    needed_matches = len(set(list(t)))
    counting_hash = {}
    hash_to_match = {}
    window_indices = [-1,-1]
    result_length = float('infinity')

    for letter in t:
        hash_to_match[letter] = 1 + hash_to_match.get(letter, 0)

    while right < len(s):
        letter = s[right]
        counting_hash[letter] = 1 + counting_hash.get(letter, 0)
        if letter in hash_to_match and counting_hash[letter] == hash_to_match[letter]:
            current_matches += 1
        while current_matches == needed_matches:
            if right - left + 1 < result_length:
                window_indices = [left, right]
                result_length = right - left + 1
            counting_hash[s[left]] -= 1
            if s[left] in hash_to_match and counting_hash[s[left]] < hash_to_match[s[left]]:
                current_matches -= 1
            left += 1
        right += 1
    left, right = window_indices

    return s[left: right + 1] if result_length != float('infinity') else ""

s1 = "ADOBECODEBANC"
t1 = "ABC"
# Output: "BANC"


s2 = "a"
t2 = "a"
# Output: a

s3 = "a"
t3 = "aa"
# Output: ""

print(minWindow(s1, t1))
print(minWindow(s2, t2))
print(minWindow(s3, t3))