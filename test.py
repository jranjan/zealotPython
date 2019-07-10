#Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.


"""
Major issue: Approach problem.

If we simply keep counters here, then as soon as we encounter
the closing square bracket, we would know there is an unmatched opening
square bracket available as well. But, the closest unmatched opening bracket
available is a curly bracket and not a square bracket and hence the counting
approach breaks here.

I WAS TRYING TO  SOLVE BY USAGE OF COUNT. The counting algorithm would
have worked if there would have been only one type of parenthesis. See
https://leetcode.com/problems/valid-parentheses/solution/.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = len(s)
        if l == 0:
            return True
        elif l > 2 and (l % 2 != 0 and not self._is_special(s[l/2+1])):
            return False
        else:
            pass

        l1o = l2o = l3o = 0
        for i in range(l):
            if s[i] == '(' or s[i] == ')':
                if s[i] == '(':
                    if l2o != 0 or l3o !=0:
                        return False
                    l1o = l1o + 1
                elif l1o != 0:
                    l1o = l1o - 1
                else:
                    if l1o == 0 or l2o != 0 or l3o != 0:
                        return False
            elif s[i] == '[' or s[i] == ']':
                if s[i] == '[':
                    l2o = l2o + 1
                elif l2o != 0:
                    l2o = l2o - 1
                else:
                    if l2o == 0 or l1o != 0 or l3o != 0:
                        return False
            elif s[i] == '{' or s[i] == '}':
                if s[i] == '{':
                    l3o = l3o + 1
                elif l3o != 0:
                    l3o = l3o - 1
                else:
                    if l3o == 0 or l1o != 0 or l2o != 0:
                        return False
            else:
                pass

        if l1o  != 0 or l2o !=0 or l3o != 0:
            return False
        return True

    def _is_special(self, c):
        if c == '(' or c == '[' or c == '{' or \
                        c == ')' or c == ']' or c == '}':
            return True
        return False


if __name__ == "__main__":
    s = Solution()
    r = s.isValid("[{]}")
    print(r)