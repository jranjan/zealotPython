# Problem:
#
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range. For the purpose of
# this problem, assume that your function returns 0 when the reversed
# integer overflows
#
# Hurdles:
# Reverse an integer! Being a C programmer, it took time to splint
# a number into set of integers which I did after applying same logic
# of division operator. I made couple of mistake in using operand.
#

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """        
        
        nl = []        
        nf = -1 if x < 0 else 1        
        n = abs(x)
        while n > 9:
            nl.append(n % 10)
            n = n /10
        nl.append(n)
        new_n = 0
        for v in nl:
            new_n = new_n * 10 + v
            if abs(new_n) > (pow(2, 31)-1):
                return 0
        return new_n * nf 

if __name__ == "__main__":
    s = Solution()
    print(s.reverse(1234))
	print(s.reverse(-1234))
    print(s.reverse(12))
    print(s.reverse(1))
    print(s.reverse(10))
	print(s.reverse(-1234242424))