n=int(input())
ans = {"A":False,
       "B":False,
       "C":False}

for i in range(2*n):
  for j in range(n):
    shang=[int(x) for x in input().split()]
    xia=[int(y) for y in input().split()]
    if (shang[1]==shang[3] or shang[1]!=shang[5]) or (xia[1]==xia[3] or xia[1]!=xia[5]):
      ans["A"] = True
    if shang[6]!=1 or xia[6]!=0:
      ans["B"] = True
    if (shang[1]==xia[1]) or (shang[3]==xia[3]) or (shang[5]==xia[5]):
      ans["C"] = True
    for key,value in ans.items():
      if value == True:
        print(key,end="")
      if ans["A"] == False and ans["B"] == False and ans["C"] == False:
        print("None")