def ncr(n, r):
    # code here
    if r == 0:
        return 1
    elif n < r:
        return 0
    else:
        return ncr(n - 1, r - 1) + ncr(n - 1, r)


print(ncr(5, 2))
