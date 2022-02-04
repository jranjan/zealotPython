def fib(n):
    print('Your fib numbers are: %s'%n)
    start = 0
    next = 1
    result = 0
    for i in range(n):
        print result
        result = start + next
        start = next
        next = result


def fib2(n):
    if n < 0:
        return
    print('Your fib numbers are: %s'%n)
    start = 0
    next = 1
    print(start)
    if n == 1:
        return
    print(next)
    for i in range(n-2):
        temp = start
        start = next
        next = start + temp
        print(next)


def fib3(n):
    if n == 1:
        print(0)
        return 0
    elif n == 2:
        print(0)
        print(1)
        return 1
    else:
        next = fib3(n-1) + fib3(n-2)
        print next
        return next


def fib4(n):
    func = lambda: n*n*n
    return func


def fib5(n):
    if n >= 0:
        start = 0
        next = 1
        yield start
        if n == 1:
            return
        yield next
        while (n > 1):
            temp = start
            start = next
            next = temp + start
            yield next
            n -= 1


def test_fib2():
    fib2(-1)
    fib2(0)
    fib2(1)
    fib2(10000)

if __name__ == "__main__":
    # fib(4)
    # fib2(4)
    # test_fib2()
    func = fib5(10000)
    print next(func)
    print next(func)
    print next(func)
    print next(func)
