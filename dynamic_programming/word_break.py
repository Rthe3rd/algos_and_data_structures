# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.


# The start_index strategy here works because we are using the .startswith(word_in_dict) strategy.  How could this be done without this built in?
def wordBreak(s: str, wordDict: list[str]) -> bool:
    # memoize should map what? something to value => somethig to boolean value => start_index to boolean
    # if you already know that a given start index works, or doesn't work, you want ot use that data to prevent further recursive calls along that branch
    memoize = {}

    # start_index determines the length of the "pre-fix" of the target string "s"
    # As you add words from the word dict in an attemp to match the target "s", you need to move the start of the prefix accordingly
      # start_index + len(word)
    def dfs(start_index):
        # if you reach the length of the word, return true.
        # You can only reach here if the previous prefixes "start with" the word(s) added from the word dict
        if start_index == len(s):
            return True

        # Why do we need memoization
        if start_index in memoize:
            return memoize[start_index]

        # initial value is False because we haven't "broken" the target word yet.
        ans = False
        # ever word is considered at every level
        for word in wordDict:
            # no additional states needed
            # if s[start_index:].startswith(word):
            if s[start_index:start_index + len(word)] == word:
                
                # only move forward if this evaluates to true, i.e. the next prefix matches at least one of the words in the word dict
                if dfs(start_index + len(word)):
                    ans = True
                    break
                memoize[start_index] = ans
        # return the answer now that you have finished recursive calls
        return ans

    return dfs(0)

s = "leetcode" 
wordDict = ["leet","code"]
print(wordBreak(s, wordDict))

s = "applepenapple" 
wordDict = ["apple","pen"]
# Output: true
print(wordBreak(s, wordDict))

s = "catsandog" 
wordDict = ["cats","dog","sand","and","cat"]
# Output: false
print(wordBreak(s, wordDict))