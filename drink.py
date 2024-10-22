n=int(input())
w1,w2,h1,h2=map(int,input().split())
v=[int(x) for x in input().split()]
ind=0
nowv1=0
nowv2=0
res=[]
overflow=0
v.insert(0,0)
for i in range(n):
    nowv1+=v[i+1]
    if nowv1>w1**2*h1:
        ind=i+1
        overflow=nowv1-w1**2*h1
        res.append(h1+overflow/w2**2)
        break
    else:
        res.append(v[i]/w1**2)

nowv2=overflow
for j in range(ind,n):
    if nowv2>w2**2*h2:
        res.append((w2**2*h2-nowv2-v[j])/w2**2)
        break
    else:
        nowv2+=v[j]
        res.append(v[j]/w2**2)
print(int(max(res)))
