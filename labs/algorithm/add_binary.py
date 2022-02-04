class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        r = list()
        a1 = list(a)[::-1]
        b1 = list(b)[::-1]

        leftover = a1 if len(a1) > len(b1) else b1
        min = len(a1) if len(a1) < len(b1) else len(b1)
        max = len(a1) if len(a1) > len(b1) else len(b1)

        i = 0
        c = 0
        while i < min:
            s = int(a1[i]) + int(b1[i]) + c
            if s == 3:
                r.append('1')
                c = 1
            elif s == 2:
                r.append('0')
                c = 1
            else:
                r.append(str(s))
                c = 0
            i = i + 1

        while i < max:
            s = int(leftover[i]) + c
            if s == 2:
                r.append('0')
                c = 1
            else:
                r.append(str(s))
                c = 0
            i = i + 1

        if c == 1:
            r.append('1')

        r = r[::-1]
        return "".join(r)


if __name__ == "__main__":
    s = Solution()
    r = s.addBinary("1", "111")
    print(r)