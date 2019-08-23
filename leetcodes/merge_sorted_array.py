class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        m_new = m
        j = 0
        for i in range(n):
            e = nums2[i]
            while e > nums1[j] and j < m_new:
                j = j + 1
            print(j)
            nums1.insert(j, e)
            m_new = m_new + 1
            nums1.pop()

if __name__ == "__main__":
    s = Solution()
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1)