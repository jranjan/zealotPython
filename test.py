

if __name__ == "__main__":
    arr = [57, 57, -57, 57]
    m1 = arr[0]
    for x in arr:
        if x >= m1:
            m1 = x
        else:
            m2 = x

    for x in arr:
        if x == m1:
            continue
        if x > m2:
            m2 = x

    print(m2)
