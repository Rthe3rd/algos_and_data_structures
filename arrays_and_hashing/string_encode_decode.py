# String Encode and Decode
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.


def string_encode(list_of_strings):
    return " ".join(list_of_strings)

def string_decode(string):
    return string.split(" ")


joined_string = string_encode(["neet","code","love","you"])
print(joined_string)
split_string = string_decode(joined_string)
print(split_string)