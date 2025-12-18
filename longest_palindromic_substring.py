class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand(center):
        
            right = center + 1
            left = center - 1
            if left<0 or right>=len(s):
                return []
            elif s[center] == s[left]:
                    right=center
            elif s[center] == s[right]:
                    left=center
            
            

            while left>=0 and right<len(s) :
                
                if s[right] == s[left]:
                    right += 1
                    left -= 1
                elif s[right] != s[left]:
                    return s[left+1:right]
                



                # if left<0 and right>len(s):
                #     return s[left+1:right-1]
            return s[left+1:right]
        
        longest = 0
        subStringNew =[]
        for i in range(len(s)) :
            str = expand(i)
            
            if longest < len(str):
                subStringNew =[]
                longest=len(str)
                subStringNew=str
            


        return subStringNew

#2.way
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str  
        :rtype: str
        """
        
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        longest = ""
        for i in range(len(s)):
            # Tek karakterli palindromlar için
            odd_palindrome = expand(i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            # Çift karakterli palindromlar için
            even_palindrome = expand(i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
        return longest  
    
# 1.way using list



   
