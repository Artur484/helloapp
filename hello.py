def isqrt(x):
    N = 0
    a = 0
    L = x.bit_length()
    L += (L % 2)
    for i in range(L, -1, -1):
        n = (x >> (2*i)) & 0b11
        if ((N - a*a) << 2) + n >= (a << 2) + 1:
            b = 1
        else:
            b = 0
        a = (a << 1) | b
        N = (N << 2) | n

    return a, N-a*a


n = int(input())
print(isqrt(n * 2)[0])
