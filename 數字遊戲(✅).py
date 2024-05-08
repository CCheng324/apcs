a1,a2,a3=map(int,input().split())
inp=[a1,a2,a3]
def mode(arr):
    
    data1=list(set(arr))
    res={x:arr.count(x) for x in data1}
    data1.remove(max(res,key=res.get))
    if data1==[]:
        data1=[a1]
        data2=[str(x) for x in data1]
        print(max(res.values())," ".join(data2))
    elif max(res,key=res.get) not in data1:
        data1.append(max(res,key=res.get))
        data1.sort(reverse=True)
        data2=[str(x) for x in data1]
        print(max(res.values())," ".join(data2))
mode(inp)