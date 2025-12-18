class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        subString = []
        longest = 0

        while right < len(s):
            if s[right] not in subString:
                subString.append(s[right])
                longest = max(longest, len(subString))
                right += 1
            else:
                subString.pop(0)
                left += 1
        return longest

# 2.way using set for better performance
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        right = 0
        seen = set()
        longest = 0
        for right in range(len(s)):
            while s[right] in seen :
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest = max(longest, right - left + 1)
        return longest
            