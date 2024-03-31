#購買力
n,d=map(int,input().split())
money=[]
buy=0
for i in range(n):
  price=[int(x) for x in input().split()]
  if max(price)-min(price)>=d:
    money.append(int(sum(price)/3))
    buy+=1
print(buy,sum(money))
