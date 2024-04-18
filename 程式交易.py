n=int(input())
D=int(input())
hispri=[int(x) for x in input().split()]
pri_in=hispri[0]
pri_out=0
profit=0
hav=True


for i in range(1,n+1):
    if hav==True:
        if hispri[i]>=pri_in+D:
            profit+=hispri[i]-pri_in #profit=y-x
            hav=False
            pri_out
    elif hav==False:
        if hispri[i]<=
