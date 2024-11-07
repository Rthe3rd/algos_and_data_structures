# def dfs(start_index, [...additional states]):
#     if is_leaf(start_index):
#         return 1
#     ans = initial_value
#     for edge in get_edges(start_index, [...additional states]):
#         if additional states: 
#             update([...additional states])
#         ans = aggregate(ans, dfs(start_index + len(edge), [...additional states]))
#         if additional states: 
#             revert([...additional states])
#     return ans

def numDecodings(digits):

  mem = dict()

  def dfs(start_index):
      if mem.get(start_index):
          return mem[start_index]

      if start_index == len(digits):
          return 1

      ways = 0


      if digits[start_index] == "0":
          return ways

      ways += dfs(start_index + 1)
      if 10 <= int(digits[start_index: start_index + 2]) <= 26:
          ways += dfs(start_index + 2)

      mem[start_index] = ways
      return ways

  return dfs(0)



s1 = "12"
# Output: 2
# # Explanation:
# "12" could be decoded as "AB" (1 2) or "L" (12).

s2 = "226"
# Output: 3
# Explanation:
# "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).


s3 = "06"
# Output: 0
# Explanation:
# "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.


print(numDecodings(s1))
print(numDecodings(s2))
print(numDecodings(s3))