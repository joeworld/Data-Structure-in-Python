"""
Use a Stack data structure to convert integer values to binary.
Example: 242
    242/2 = 121 -> 0
    121/2 = 60  -> 1
    60/2  = 30  -> 0
    30/2  = 15  -> 0
    15/2  = 7   -> 1
    7/2   = 3   -> 1
    3/2   = 1   -> 1
    1/2   = 0   -> 1
"""
from stack_ds import Stack

def div_by_2(y):
    s = Stack()

    while 0 < y:
        x = y % 2
        s.push(x)
        y = y // 2

    res = ""
    while not s.is_empty():
        res += str(s.pop())

    return res

print(div_by_2(242))