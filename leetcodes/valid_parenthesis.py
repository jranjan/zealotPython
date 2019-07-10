class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        mappings = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for c in s:
            if c in mappings:
                if stack:
                    pc = stack.pop()
                    if pc != mappings[c]:
                        return False
                else:
                    return False
            else:
                stack.append(c)

        return not stack 