class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = s.split()
        if len(l) == 0:
            return 0
        lw = l[len(l)-1]
        return len(lw)

if __name__ == "__main__":
    s = Solution()
    n = s.lengthOfLastWord("Hello World")
    print(n)