# 567. Permutation in String
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

s1 = "ba"
s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

s3 = "ab"
s4 = "eidboaoo"
# output: false

s5 = "adc"
s6 = "dcda"

import re

def permutation_in_string(s1, s2):
    # left side of window
    left = 0
    # Track how many characters in s1 have been found or "matched" in s2.  Eventually needs to hit 26
    matches = 0

    # if length of s1 is longer than s2, it can't be contained within s2
    if len(s1) > len(s2):
        return False
    # comparing counts of lowercase characters using lists 
    s1_count, s2_count = [0] * 26, [0] * 26

    # Add one to whatever value is in the array at the position corresponding to that letter string_count[(ord(letter) - ord('a'))]
    # Only checking the first window that is the length of the string: [0:len(s1)] => non-inlcusive
    for i in range(len(s1)):
        s1_count[ord(s1[i]) - ord('a')] += 1 
        s2_count[ord(s2[i]) - ord('a')] += 1 

    # TRICK: Track number of matches between s1 and s2.  26 will indicate when the current window of s2 contains the same character counts of s1
    for i in range(26):
        matches += (1 if s1_count[i] == s2_count[i] else 0)

    # Loop forward through all values of s2 starting at the boundary of where you ended initially checked, s2[len(s1): len(s2)] 
    # At the start of the loop, left is 0 and right is len(s1) => 
    for right in range(len(s1), len(s2)):
        # check to see if matches are already at 26 from the first window
        if matches == 26:
            return True
        # Calculate the index in the count hash/list that needs to be updated by moving the RIGHT pointer over 
        index = ord(s2[right])  - ord('a')
        # Update the value of the count hash/list at the calculated index since you are ADDING it to the window 
        s2_count[index] += 1
        # If adding, after updating the count hash/list the values of the two count hashes/lists are equal, increment/update the matches count
        if s1_count[index] == s2_count[index]:
            matches += 1
        # If after adding and updating the count hash/list the values of the two count hashes/lists are off by 1, decrement/update the matches count
        elif s1_count[index] + 1 == s2_count[index]:
            matches -= 1

        # Calculate the index in the count hash/list that needs to be updated by moving the LEFT pointer over 
        index = ord(s2[left])  - ord('a')
        # Update the value of the count hash/list at the calculated index since you are REMOVING it from the window 
        s2_count[index] -= 1
        # If the count hashes/lists are equal at the index, after decrementing, increment the matches count 
        if s1_count[index] == s2_count[index]:
            matches += 1
        # If the count hashes/lists are NOT equal at the index, after decrementing, decrement the matches count 
        elif s1_count[index] - 1 == s2_count[index]:
            matches -= 1
        # move the left index over
        left += 1
    return matches == 26

print(permutation_in_string(s1, s2))
print(permutation_in_string(s3, s4))
print(permutation_in_string(s5, s6))