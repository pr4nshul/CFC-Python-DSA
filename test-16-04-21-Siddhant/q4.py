def Anargams(lists):
    result = []
    for string in lists:
        freq = {}
        for item in string:
            freq[item] = freq.get(item, 0) + 1
        result.append(freq)
    ans = []
    for i in range(len(result) // 2):
        for j in range(i + 1, len(result)):
            if result[i] == result[j]:
                ans.append([i + 1,j + 1])
    return ans 

# lists = ["cat", "dog", "god", "tca"]
lists = [item for item in input().split()]
print(Anargams(lists))