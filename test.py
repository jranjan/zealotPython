class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0 or x == 1:
            return x

        s = 0
        while s * s <= x:
            s = s + 1

        if s * s > x:
            s = s - 1
        return s

if __name__ == "__main__":
    s = Solution()
    print(s.mySqrt(125))
    print(s.mySqrt(225))
    print(s.mySqrt(25))
    print(s.mySqrt(2))
    print(s.mySqrt(1))
    print(s.mySqrt(0))
    print(s.mySqrt(144))
    print(s.mySqrt(190))
    print(s.mySqrt(399))
    print(s.mySqrt(900))