# 3 calculate the no of ways to get sum equal to k using combination of (2,5,10)
def reachSum(k):
    print(reachSumHelper(k))

def reachSumHelper(k, d={2:0, 5:0, 10:0}, a = []):
    if(k<0):
        return len(a)

    if(k==0):
        if(d not in a):
            a.append(dict(d))
        return len(a)

    for x in [2,5,10]:
        d[x] += 1
        reachSumHelper(k-x, d, a)
        d[x] -= 1

    return len(a)

i = int(input())
reachSum(i)