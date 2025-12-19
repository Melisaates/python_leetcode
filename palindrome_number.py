class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str=[]
        num=0
        while abs(x)>0:
            if x<0:
                return False
            else: 
                num=x%10
                str.append(num)
                x=x/10
        print("str:",str)
        right= len(str) -1
        left=0
        while left < right:
            print(str[left])
            print(str[right])
            if str[left]!=str[right]:
                print(str[left])
                print(str[right])
                return False
            left += 1
            right -=1
        return True   
#2.way- Palindrome Number
# complexity O(n)
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0:
            return False
        str_x = str(x)
        left =0
        right = len(str_x) -1
        while left < right:
            if str_x[left] != str_x[right]:
                return False
            left +=1
            right -=1
        return True

