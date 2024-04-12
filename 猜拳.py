#input------------------------
f=int(input())
n=int(input())
sis=[int(a) for a in input().split()]
 #----------------------------
someone_win=False

for i in range(n):
    print(f,end=" ")
    #browin----------
    if (f==0 and sis[i]==2) or (f==2 and sis[i]==5) or (f==5 and sis[i]==0):
        print(f': Won at round {i+1}')
        someone_win=True
        break
    #siswin----------
    elif (f==2 and sis[i]==0) or(f==5 and sis[i]==2) or (f==0 and sis[i]==5):
        print(f': Lost at round {i+1}')
        someone_win=True
        break               
    
    #判斷出拳---------
    if sis[i]==sis[i-1]:
        if sis[i]==0:
            f=5
        elif sis[i]==2:
            f=0
        elif sis[i]==5:
            f=2
    else:
        f=sis[i]

if not(someone_win):
    print(f': Drew at round {i+1}')

