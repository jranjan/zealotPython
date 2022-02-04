class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.min = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s.append(x)
        if self.min is None:
            self.min = x
        elif x < self.min:
            self.min = x
        return None

    def pop(self):
        """
        :rtype: None
        """
        n = len(self.s)
        if n > 0:
            x = self.s[n - 1]
            print(x, self.min, x)
            if self.min == x:
                print('.'*60)
                self.min = None
            del self.s[n - 1]
        return None

    def top(self):
        """
        :rtype: int
        """
        n = len(self.s)
        x = self.s[n - 1]
        return x

    def getMin(self):
        """
        :rtype: int
        """
        if self.min != None:
            return self.min
        else:
            self.min = self.s[0]
        print('*'*60)
        print(self.s)
        n = len(self.s)
        for i in range(n):
            if self.s[i] < self.min:
                self.min = self.s[i]
        print(self.min)
        print('*' * 60)
        return self.min

    def display(self):
        print(self.s)

if __name__ == "__main__":
    s = MinStack()
    print(s.push(-10))
    print(s.push(14))
    print(s.getMin())
    print(s.getMin())
    print(s.push(-20))
    print(s.getMin())
    print(s.top())
    print(s.getMin())
    print(s.getMin())
    print(s.pop())
    print(s.push(10))
    print(s.push(-7))
    s.display()
    print(s.getMin())
    print(s.push(-7))
    s.display()
    print(s.pop())
    print(s.top())
    print(s.getMin())
    print(s.pop())