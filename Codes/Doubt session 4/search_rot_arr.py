def search_rotated(arr,key):
    start,end= 0,len(arr)-1
    while start<=end:
        mid = start+ (end-start)//2
        if arr[mid] ==key:
            return mid
        
        if arr[start] <= arr[mid] :
            if key >arr[start] and key < arr[mid]:
                end = mid-1
            else:
                start=mid-1
        else:
            if key >arr[mid] and key <arr[end]:
                start=mid+1
            else:
                end=mid-1
    
    return -1

def main():
    print(search_rotated([4,5,7,9,10,-1,2],10))

main()