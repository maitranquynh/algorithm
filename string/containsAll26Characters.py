def isOk(s):
    dic = {'a': 0,'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,'j': 0
        ,'k': 0,'l': 0,'m': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,'t': 0
        ,'u': 0,'v': 0,'w': 0,'x': 0,'y': 0,'z': 0}

    for c in s.lower():
        if c in dic:
            dic[c] += 1

    print(dic)
    if 0 in dic.values():
        return False

    return True


s1 = "a dog is running crazily on the ground who doesn't care about the world"
s2 = "A b c d e f g h i j k l m n o p q r s 1234t u v w x y Z @#$"

print(isOk(s1))
print(isOk(s2))
