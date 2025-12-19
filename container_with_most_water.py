#1.way- Container With Most Water
# time complexity: O(n)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        if n<2 or n>10**5:
            return 0
        
        
        left=0
        right= n-1
        horizontal=0
        maxArea=0
        while left<right:
            horizontal=right-left
            if height[left]<height[right]:
                vertical=height[left]
                left += 1
            else:
                vertical=height[right]
                right  -= 1
            
            maxArea=max(maxArea,horizontal*vertical)
        
        return maxArea



#2.way- Container With Most Water
# time complexity: O(n^2)
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        if n<2 or n>10**5:
            return 0

        maxArea=0
        heightArea=0
        count = 0
        for i in range(len(height)):  
            if height[i]<0 or height[i]>10**4:
                return 0          
            for j in range(len(height)):
                if i<j:
                    count += 1
                    heightArea=min(height[i],height[j])
                    newArea=heightArea*count
                    maxArea = max(maxArea,newArea)

            count = 0
        return maxArea
            


        