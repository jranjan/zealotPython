# Determine whether an integer is a palindrome. An integer 
# is a palindrome when it reads the same backward as forward.

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        nl = []
        n = x 
        while n > 9:
            nl.append(int(n % 10))
            n = n / 10
        nl.append(n)
        dc = len(nl) 
        h = int(dc/2)
        for i in range(h):
            if nl[i] != nl[dc-i-1]:
                return False
        return True


