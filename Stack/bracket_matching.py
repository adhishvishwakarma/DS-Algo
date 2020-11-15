from stack import Stack


def check_brackets(statement):
    stack = Stack()
    for ch in statement:
        if ch in ('{', '[', '('):
            stack.push(ch)
        if ch in ('}', ']', ')'):
            last = stack.pop()
            if last is '{' and ch is '}':
                continue
            elif last is '[' and ch is ']':
                continue
            elif last is '(' and ch is ')':
                continue
            else:
                return False
    if stack.size > 0:
        return False
    else:
        return True


sl = (
    "{(foo)(bar)}[hello](((this)is)a)test",
    "{(foo)(bar)}[hello](((this)is)atest",
    "{(foo)(bar)}[hello](((this)is)a)test))"
)

for s in sl:
    m = check_brackets(s)
    print("{}: {}".format(s, m))


def is_matched(expression):
    """
    Finds out how balanced an expression is.
    With a string containing only brackets.

    >>> is_matched('[]()()(((([])))')
    False
    >>> is_matched('[](){{{[]}}}')
    True
    """
    opening = tuple('({[')
    closing = tuple(')}]')
    mapping = dict(zip(opening, closing))
    # mapping = {'(': ')', '{': '}', '[': ']'}
    # print(mapping)
    queue = []

    for letter in expression:
        if letter in opening:
            queue.append(mapping[letter])
        elif letter in closing:
            if not queue or letter != queue.pop():
                return False
    return not queue


for s in sl:
    m = is_matched(s)
    print("{}: {}".format(s, m))
