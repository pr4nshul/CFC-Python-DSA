# 5 print strings with unique letters
def uniqueLetters(s):
    rs = ""
    for x in s:
        if x not in rs:
            rs += x
    return rs

i = int(input())
for x in range(i):
    s = input()
    print(uniqueLetters(s))