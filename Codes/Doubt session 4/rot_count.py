def count_rotations(arr):
    start,end =0,len(arr)-1
    while start< end:
        mid = start +(end-start) //2
# if mid is greater the next element then it the pivot
        if mid<end and arr[mid] >arr[mid+1]:
            return mid+1
        #if mid is ammler than prev element then prev element is the pivot
        if mid>start and arr[mid-1]>arr[mid]:
            return mid

        #the pivot will lie on the unsorted side
        if arr[start]<arr[mid]:
            start = mid+1
        else:
            end = mid-1
        
    return 0

def main():
    print(count_rotations([4,5,7,9,10,-1,2]))

main()