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

        i = c = 0
        # Using rnage(start, stop, step) for syntax exploration only
        while i<max:
            if nums[i] == val:
                del nums[i]
                c = c + 1
                max = max - 1
            else:
                i = i + 1

        print nums
        return c

if __name__ == "__main__":
    s = Solution()
    nums = [0,1,2,2,3,0,4,2]
    print(s.removeElement(nums, 2))