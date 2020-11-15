# using backtracking

def bit_string(n, s):
    if n == 1:
        return s
    return [digit + bits for digit in bit_string(1, s) for bits in bit_string(n-1, s)]


print(bit_string(3, 'abc'))
