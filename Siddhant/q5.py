


def countWays(n, m = 3):
    temp = 0
    result = [1]

    for i in range(1, n + 1):
        start = i - m - 1
        end = i - 1
        if start >= 0:
            temp -= result[start]

        temp += result[end]
        result.append(temp)
    return result[n]
step = int(input())
print(countWays(step))
