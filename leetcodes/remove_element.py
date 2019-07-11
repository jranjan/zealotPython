# Given an array nums and a value val, remove all instances of
# that value in-place and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond
# the new length.

# Learning:
# I did not read the problem statement correctly and was returning different value
# than desired.


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        max = len(nums)
        if max == 0:
            return 0

        i = 0
        while i < max:
            print str('*' * 60 + str(i))
            if nums[i] == val:
                del nums[i]
                max = max - 1
            else:
                i = i + 1
            print nums

        return len(nums)