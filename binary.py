def Binary_search(arr,target):
    right=len(arr)-1
    left=0
    while left<=right:
        mid=(right+left)//2
        if arr[mid]==target:
            return mid
        elif target<arr[mid]:
            right=mid-1
        elif target>arr[mid]:
            left=mid+1
data1=[1,2,3,4,5,8,9,10,11,16,18,19]
print(Binary_search(data1,9))
