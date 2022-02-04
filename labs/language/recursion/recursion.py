def add_list(n):
    if n == 1:
        l = list()
        l.append(str(n))
        return l
    else:
        ol = list()
        ol.append(add_list(n-1))
        return ol


if __name__ == "__main__":
    result = add_list(2)
    print result