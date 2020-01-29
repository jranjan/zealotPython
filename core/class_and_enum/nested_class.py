class Parent():

    def __init__(self):
        c = self.Child()
        c.tell()

    class Child():
        def __init__(self):
            pass

        def tell(self):
            print("I am child")


if __name__ == "__main__":

    p = Parent()