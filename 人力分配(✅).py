a1,b1,c1=map(int,input().split())
a2,b2,c2=map(int,input().split())
n=int(input())
tmp=[]
for i in range(n+1):
    y1=(a1*(i**2))+(b1*i)+c1
    j=n-i
    y2=(a2*(j**2))+(b2*j)+c2
    tmp1=y1+y2
    tmp.append(tmp1)
print(max(tmp))