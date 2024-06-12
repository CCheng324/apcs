x,n=map(int,input().split())
d=[int(a) for a in input().split()]
right=[]
left=[]
d.append(x)
d.sort()
m_point=d.index(x)+1
last_p=0

for i in range(len(d)):
    if d[i]>d[m_point-1]:
        right.append(d[i])
        
for j in range(len(d)):
    if d[j]<d[m_point-1]:
        left.append(d[j])

if len(right)>len(left):
    print(len(right),right[len(right)-1])
else:
    print(len(left),left[0])




