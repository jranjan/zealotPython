class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0

        if len(needle) > len(haystack):
            return -1

        # I was trying to complicate the issue without reason.
        # It is better to think in terms of simple loops before thinking
        # of optimization. I also feel that it is better to hear
        # clearly what problem is saying.
        nl = len(needle)
        hl = len(haystack)
        # prepare index which start with needle's first letter
        indexes = []
        for i in range(hl):
            if needle[0] == haystack[i]:
                indexes.append(i)

        for x in indexes:
            start = j = int(x)
            # Needed this if condition. Otherwise, I was increasing time
            # complexity and system was timing out for long set of
            # input values.
            if start + nl <= hl:
                i = 0
                while i < nl and needle[i] == haystack[j]:
                    i = i + 1
                    j = j + 1
                if i == nl:
                    return start

        return -1


if __name__ == "__main__":
    s = Solution()
    print(str(s.strStr("iiiiiiii", "issip")))
    print(str(s.strStr("mississippi", "issip")))
    print(str(s.strStr("aabaaabaaac", "aabaaac")))
    print(str(s.strStr("hello", "ll")))