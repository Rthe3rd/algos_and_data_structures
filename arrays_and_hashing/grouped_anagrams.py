class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        if [""] in strs or None in strs:
            return [[""]]
        for string in strs:
            sorted_string = "".join(sorted(string))
            if not sorted_string in anagrams:
                anagrams[sorted_string] = [string]
            else:
                anagrams[sorted_string].append(string)
        grouped_anagrams = []
        for key, value in anagrams.items():
            grouped_anagrams.append(value)
        return grouped_anagrams