"""
Use a stack to check if a string has balanced usage of parenthesis.
Example:
    (), ()(), (({[]})) <- Balanced.
    ((), {{)}], [][]]] <- Not Balanced.
"""

from stack_ds import Stack

def is_match(top, p):
    if top == "{" and p == "}":
        return True
    if top == "[" and p == "]":
        return True
    if top == "(" and p == ")":
        return True

    return False

def check_paranthesis(p_str):
    s = Stack()
    is_bal = True
    index = 0

    while len(p_str) > index and is_bal:
        paren = p_str[index]
        if paren in "{[(":
            s.push(paren)
        else:
            if s.is_empty():
                is_bal = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_bal = False

        index += 1

    if s.is_empty() and is_bal:
        return True
    else:
        return False

print(check_paranthesis("{{}}"))
print(check_paranthesis("{){(}}]"))