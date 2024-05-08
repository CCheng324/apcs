n,d=map(int,input().split())
price=[int(a) for a in input().split()]#y
pri_in=price[0]#x
pri_out=0
profit=0
have_pri=True
for i in range(n):
    if price[i+1]>d+pri_in:
        pri_out=price[i+1]
        profit+=price[i+1]-pri_in
        have_pri=False#賣出
    
    elif price[i+1]<pri_out-d:
