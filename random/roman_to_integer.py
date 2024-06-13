
def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    # running sum
    # if the next value is smaller, perform a subtraction?
    # determine if you are going to add or subtract the roman numeral
    # keep track of the previous value?
    # loop through, starting at the second value from the left?
    numeral_to_integer_hash = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    running_sum = 0
    integers = []
    for numeral in s:
        integers.append(numeral_to_integer_hash[numeral])


    for i in range(0, len(s)):
        if i > 0 and integers[i] > integers[i-1]:
            running_sum += integers[i] - integers[i-1] - integers[i-1]
        else:
            running_sum += integers[i]
    return running_sum
