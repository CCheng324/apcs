n=int(input())
x1,y1=map(int,input().split())
max1,min1=0,401
for i in range(1,n):
    x2,y2=map(int,input().split())
    res=abs(x2-x1)+abs(y2-y1)
    max1,min1=max(max1,res),min(min1,res)
    x1,y1=x2,y2
print(max1,min1)
