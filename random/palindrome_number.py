
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    left = 0
    y = str(x)
    right = len(y) - 1
    
    while left < right:
        if y[left] != y[right]:
            return False
    return True

print(isPalindrome(-121))