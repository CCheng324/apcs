n=int(input())
h_score=0
s_false=0
first_point=0
time=[]
score=[]

def sum_score(a,b,c):
    if a-b-2*c<0:
        return 0
    else:
        return a-b-2*c
      
for i in range(n):
    t,s=map(int,input().split())
    if s==-1:
        s_false+=1
    time.append(t)
    score.append(s)
    
h_score=max(score)
first_point=time[score.index(h_score)]

print(sum_score(h_score,n,s_false),first_point)