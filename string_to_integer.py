# 8. String to Integer (atoi)
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).
# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
# Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
# If the first sequence of non-whitespace characters in s is not a valid integral number,
# or if no such sequence exists because either s is empty or it contains only whitespace characters, no conversion is performed.
# 1.way
# complexity O(n)
#1h 34min
class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)< 0 or len(s) >200:
            return 0
        index = 0
        number=0
        negative = False
        digitCounter=0
        digit = False
        while index < len(s):
            # if s[index] == " ":
            #     index += 1
            

            print("index: ",index)
            if s[index].isdigit():
                print("digit ",s[index])

                if digitCounter== 0:
                    if index != 0:
                        if s[index-1]=="-":
                            negative = True
                        if s[index-1]=="+":
                            negative = False
                
                digit =True
                digitCounter += 1

                
                number=number*10+int(s[index])
                index += 1
            

            else:
                digit = False
                if digitCounter==0  and s[index]!="-" and s[index]!=" " and s[index]!="+":
                    return 0  
                elif digitCounter==0 and index!= len(s)-1:
                    if  s[index]=="+" and s[index+1].isdigit()==False:
                        return 0
                    if  s[index]=="-" and s[index+1].isdigit()==False:
                        return 0
                    
                
                index += 1
                if digitCounter != 0 and digit==False:
                    if negative==True and number >0:
                        number = -number
                    if number >2**31 -1 :
                        number = 2**31 -1 
                    if number <-2**31:
                        number = -2**31
                    

                    return number
            
      
        if negative==True and number>0:
            number = -number
        if number >2**31 -1 :
            number = 2**31 -1 
        if number <-2**31:
            number = -2**31
        return number

#2.way 
# complexity O(n)
class Solution(object) :
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()  # Remove leading whitespace
        if not s:
            return 0

        negative = False
        index = 0
        if s[0] == '-':
            negative = True
            index += 1
        elif s[0] == '+':
            index += 1

        number = 0
        while index < len(s) and s[index].isdigit():
            number = number * 10 + int(s[index])
            index += 1

        if negative:
            number = -number

        # Clamp the number to the 32-bit signed integer range
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        if number < INT_MIN:
            return INT_MIN
        if number > INT_MAX:
            return INT_MAX

        return number
