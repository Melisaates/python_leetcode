class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        number = 0
        output =[]

        
        negative = x<0
        x=abs(x)

        while x != 0 :
            num = x % 10
            x = x//10
            number = number *10 + num
        if negative:
            number = -number
        if number<-2**31 or number>2**31 -1:
            return 0
            
            
        
        return number
