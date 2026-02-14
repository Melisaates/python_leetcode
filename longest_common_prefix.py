# 1.way- Longest Common Prefix
# time complexity: O(n*m) n is number of strings, m is length of the shortest string
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        
        if strs[0] != "":
            first_str =strs[0]
            result_str = first_str 
        else:
            return ""

        if len(strs)==1:
            return strs[0]
        
        for i in range(1,len(strs)):
            
            if  strs[i]=="":
                return ""
            limit=min(len(result_str),len(strs[i]))
                
            for j in range(limit):
                if strs[i][j]!= result_str[j]:
                    break
                else:
                    j +=1

            result_str = result_str[:j]
        if result_str == "":
            return ""

        return result_str

                






                


# 2.way- Longest Common Prefix
# time complexity: O(n*m) n is number of strings, m is length of the shortest string
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         if not strs:
#             return ""
        
#         prefix = strs[0]
        
#         # Check each string in the array
#         for s in strs[1:]:
#             # Reduce the prefix until it matches the start of the string
#             while not s.startswith(prefix):
#                 # Shorten the prefix by one character
#                 prefix = prefix[:-1]
#                 if not prefix:
#                     return ""
        
#         return prefix
    