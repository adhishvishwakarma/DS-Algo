from functools import reduce

class E:
    def __init__(self, i, n, a, s):
        self.i = i
        self.n = n
        self.a = a
        self.s = s

T = E(20, 'T', 35, 10000)

T.__dict__['exp'] = 10

b = T.s * (T.exp + len(T.__dict__))//100

