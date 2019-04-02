# Using recursion

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


def reverse2(s):
    res = ""
    for c in s:
        res = c + res

    return res


s1 = "This is me"
print(reverse2(s1))