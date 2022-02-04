import  os

class Test:

    myno = 100

    def access(self):
        print self.myno
        print Test.myno


if __name__ == "__main__":
    t = Test()
    t.access()

    print Test.myno