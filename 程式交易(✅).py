n,D=map(int,input().split())
history_price=[int(a) for a in input().split()]
have=history_price[0]
profit=0
have_ticket=True
for i in range(1,len(history_price)):
    if have_ticket:
        if history_price[i]>=have+D:
            have_ticket=False
            profit+=history_price[i]-have
            have=history_price[i]
    elif not have_ticket:
        if history_price[i]<=have-D:
            have_ticket=True
            have=history_price[i]
print(profit)