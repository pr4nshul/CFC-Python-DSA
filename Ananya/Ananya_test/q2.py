# 2 Given an array of strings give a list to pairs which are anagram to each other
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
def checkAnagram(s1, s2):
    d1 = {}
    for x in s1:
        if(x in d1.keys()):
            d1[x] += 1
        else:
            d1[x] = 1
    d2 = {}
    for x in s2:
        if(x in d2.keys()):
            d2[x] += 1
        else:
            d2[x] = 1
    return d1 == d2

def giveAnagram(arr, result=[]):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if(checkAnagram(arr[i], arr[j])):
                result.append([i+1, j+1])

    print(result)


name  = input()
array = [x for x in name.split(" ")]
giveAnagram(array)