def is_palindrome(n):
    if len(n) < 2:
        return True
    if n[0] != n[-1]:
        return False
    return is_palindrome(n[1: -1])


print(is_palindrome('abba'))
