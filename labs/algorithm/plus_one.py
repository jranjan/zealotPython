# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
#
# The digits are stored such that the most significant digit is at the head of the list, and each
# element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero, except the number 0 itself.
#
#
# Example 1:
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        dc = len(digits)
        carry = 1 if digits[dc - 1] == 9 else 0
        for i in range(dc):
            if digits[dc - i - 1] + carry > 9:
                digits[dc - i - 1] = 0
                carry = 1
            else:
                digits[dc - i - 1] = digits[dc - i - 1] + 1
                carry = 0
                break

        print digits
        if carry == 1:
            digits.insert(0, 1)

        return digits
