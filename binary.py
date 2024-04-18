def binary_scarch(arr,target):
    left=0
    right=len(arr)-1
    
    while right>=left:
        mid=(right+left)//2
        if arr[mid]==target:
            return mid
        if arr[mid]>target:
            right=mid-1
        if arr[mid]<target:
            left=mid+1
    return -1

data=[1,2,3,4,5,6,7,8,9]
aim=3
if binary_scarch(data,aim)==-1:
    print(f"{aim}not exist")
else:
    print(f"{aim} index={mid}")
