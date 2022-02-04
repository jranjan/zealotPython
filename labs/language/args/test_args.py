# Hello World program in Python

print "Hello World!\n"


def f(**kwargs):
    print kwargs['a']
    print kwargs['b']
    print kwargs['c']


d = dict()
d['a'] = 1
d['b'] = 1
d['c'] = 1


if __name__ == "__main__":
    f()
