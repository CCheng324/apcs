n=int(input())
fen=0
data=([int(i) for i in input().split()])
data.insert(0,101)
data.insert(n+1,101)
for j in range(n+1):
    if data[j]==0:
        fen+=min(data[j-1],data[j+1])
print(fen)

