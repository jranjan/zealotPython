# Given an array of integers, return indices of 
# the two numbers such that they add up to a specific target. 
# You may assume that each input would have 
# exactly one solution, and you may not use the same element twice.

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        count = len(nums)
        for i in range(count):           
           for j in range(i+1, count):
               if nums[i] + nums[j] == target:
                  return [i, j]
        return None
