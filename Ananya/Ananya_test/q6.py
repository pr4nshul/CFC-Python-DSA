# 6 count no of ways person can reach upstairs of steps n, where he can jump either 1,2 or 3 steps
def countways(n, count=0):
    if(n < 0):
        return count

    if(n == 0):
        count += 1
        return count

    for x in [1,2,3]:
        count = countways(n-x, count)

    return count

countways(5)