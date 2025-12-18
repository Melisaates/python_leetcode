# Problem: Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such
# 2.way
# complexity O(n)
class Solution(object):
    def twoSum(self, nums, target):
        # Create a dictionary to store the numbers and their indices
        num_map = {}
        for i, num in enumerate(nums):
            # Calculate the complement
            complement=target - num
            # Check if the complement exists in the dictionary
            if complement in num_map:
                # If found, return the indices
                return [num_map[complement], i] 
            # Store the number and its index in the dictionary
            num_map[num] = i
        return []


# 1.way
# complexity O(n^2)
# class Solution () :
#     def twoSum(self,nums,target):
#         
#         # num is used to represent each element in the list, i is the index
#         for i,num in enumerate(nums):

#             for j,numJ in enumerate(nums):
#                 if(i!=j):
#                     if(num+numJ==target):
#                         return [i,j]
                    
            

#         return []   

# Solution = Solution()
