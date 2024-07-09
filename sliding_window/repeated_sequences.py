# 187. Repeated DNA Sequences
# Medium
# When studying DNA, it is useful to identify repeated sequences within the DNA.
# The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
# For example, "ACGAATTCCG" is a DNA sequence.
# Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

def repeated_sequence(s):
    # set to check if sequence has already been made
    # if the length of s is shorter than 10, return None
    if len(s) < 10:
        return []
    seen = set()
    repeats = set()
    left = 0
    while left <= len(s) - 10:
        dna = s[left:left+10]
        if dna in seen:
            repeats.add(dna)
        seen.add(dna)
        left += 1
    return list(repeats)


s1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# Output: ["AAAAACCCCC","CCCCCAAAAA"]

s2 = "AAAAAAAAAAA"
# Output: ["AAAAAAAAAA"]
print(repeated_sequence(s1))
print(repeated_sequence(s2))

# Constraints:
# 1 <= s.length <= 105
# s[i] is either 'A', 'C', 'G', or 'T'.