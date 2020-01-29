from my_math.algebra import operations as ap

if __name__ == "__main__":
    a = 6
    b = 9

    print('Sum of %d and %d is %d.\n' % (a, b, ap.add(a, b)))
    print('Subtraction of %d and %d is %d.\n' % (a, b, ap.subtract(a, b)))
    print('Multiplication of %d and %d is %d.\n' % (a, b, ap.multiply(a, b)))
    print('Division of %d and %d is %d.\n' % (a, b, ap.div(a, b)))

    print('Supported function by algebra.operations module %s are:\n' % (dir(ap)))
    print(help(ap.add))
