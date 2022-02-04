class Base(object):
    def __init__(self, parent='I am parent'):
        print(parent)


class Derived(Base):
    def __init__(self, child='I am child'):
        print(child)

    def testme(self, a, b, c=20):
        print(a, b, c)

if __name__ == "__main__":
    d = Derived()
