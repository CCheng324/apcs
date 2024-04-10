#七言對聯
n=int(input())
a=False
b=False
c=False
find=False
ans=["A","B","C"]
tmp=[]
boo=[]
for i in range(n):
  shang=[int(x) for x in input().split()]
  xia=[int(y) for y in input().split()]
  if (shang[1]==shang[3] or shang[1]!=shang[5]) or (xia[1]==xia[3] or xia[1]!=xia[5]):
    a=True
  if shang[6]!=1 or xia[6]!=0:
    b=True
  if (shang[1]==xia[1]) or (shang[3]==xia[3]) or (shang[5]==xia[5]):
    c=True
  boo=[a,b,c]
  for j in range(3):
    if boo[j]==True:
      tmp.append(ans[j])
      find=True
  if find==False:
    tmp.append("None")
  print("".join(map(str,tmp))) 
