class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        right = len(s) -1
        left = 0
        subString =[]
        longestSub = []

        while left < right:
            if not s[left] in subString:
                subString.append(s[left])
                left +=1
                
            else:
                if len(longestSub) < len(subString):
                    longestSub = subString
                subString = [] 
                subString.append(s[left])

        return len(longestSub)
           
            


            


