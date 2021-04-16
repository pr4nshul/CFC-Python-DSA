def removeDuplicates(string):
    result = []
    for item in string:
        if item not in result:
            result.append(item)
    return "".join(result)

ans = []
test = int(input())
for _ in range(test):
    string = input()
    ans.append(removeDuplicates(string))

for item in ans:
    print(item)