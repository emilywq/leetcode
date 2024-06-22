class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        chars = {}
        count = 0
        maxcount = 0
        for i,v in enumerate(s):
            index = chars.get(v)
            if index is None or index < i - count:
                count += 1
            else:
                count = i - index
            chars[v] = i
            maxcount = max(maxcount, count)
        return maxcount