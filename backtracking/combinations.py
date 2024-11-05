# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order.

def combine(n: int, k: int) -> list[list[int]]:
  results = []
  current_path = []

  def dfs(start):
      if len(current_path) == k:
          results.append(current_path.copy())
          return

      for num in range(start, n + 1):
          current_path.append(num)
          dfs(num + 1)
          current_path.pop()

  dfs(1)
  return results

print(combine(n = 4, k = 2))

# Example 1:

n = 4
k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

# Example 2:

n = 1
k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.