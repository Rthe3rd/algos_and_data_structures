# Check if string s is a palindrome
import re

def is_palindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.replace(" ","").lower()
    left = 0 
    right = len(s) - 1
    while left <= right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

s = 'yes sam mAsseY'
s = 'yes sam mAsse'

print(is_palindrome(s))