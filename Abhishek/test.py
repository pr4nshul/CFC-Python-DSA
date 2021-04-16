"""
Ravi the hopper
"""

def hopper(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    hop1 = hopper(n-1)
    hop2 = hopper(n-2)
    hop3 = hopper(n-3)
    return hop1 + hop2 + hop3


"""
remove duplicates from string
"""
def removeDuplicates(unprocessed,st):
    if not unprocessed:
        return None
    if  len(unprocessed) == 1:
        item = unprocessed.pop()
        return item
    first = unprocessed.pop(0)
    rest  = removeDuplicates(unprocessed,st)
    if rest is None:
        if first not in st:
            st.insert(0,first)
    elif first == rest[0]:
        for i in range(len(rest)):
            st.insert(0,rest[i])
    else:
        for i in range(len(rest)):
            st.insert(0,rest[i])
        st.insert(0,first)


"""
Complete the task --Naman
"""
import math
import sys
def completeTask(arr,target):
    if target  == 0:
        return 0
    if target < 0:
        return math.inf

    answer = sys.maxsize
    for i in range(len(arr)):
        chance = 1 + completeTask(arr,target - arr[i])
        answer = min(chance,answer)
    return answer


"""
check anagrams
"""

def anagramchecker(l):
    if not l:
        return []
    answer = []
    excluded = []
    anagramHelper(l,0,answer,excluded)
    return answer

def anagramHelper(l,index,answer,excluded):
    if index > len(l) -1:
        return
    if index in excluded:
        return

    first_str = l[index]
    for i in range(index+1, len(l)):
        if(checkanagram(first_str,l[i])):
            excluded.append(index)
            excluded.append(i)
            answer.append([index + 1,i + 1])
            break
    anagramHelper(l,index + 1,answer,excluded)

def checkanagram(first,second):
    if not first and second:
        return False
    if not second and first:
        return False
    l1 = len(first)
    l2 = len(second)
    if l1 != l2:
        return False
    return sorted(first) == sorted(second)







if __name__ == "__main__":
    #print(hopper(5))
    #print(hopper(4))


    #st = []
    #removeDuplicates(list("tomorrow"),st)
    #print(''.join(st))

    """
    complete task
    """

    #arr = [2,5,10]
    #target = 25
    #print(completeTask(arr,target))

    """
    anagrams
    """

    l = ["cat","dog","god","tca"]
    print(anagramchecker(l))


