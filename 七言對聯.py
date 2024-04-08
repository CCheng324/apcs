#七言對聯
n=int(input())
a=False
b=False
c=False
boo=[a,b,c]
ans=["A","B","C"]
tmp=[]

for i in range(n):
  shang=[int(x) for x in input().split()]
  xia=[int(y) for y in input().split()]
  if (shang[1]==shang[3] or shang[1]!=shang[5]) or (xia[1]==xia[3] or xia[1]!=xia[5]):
    a=True
  if shang[6]!=1 or xia[6]!=0:
    b=True
  if (shang[1]==xia[1]) or (shang[3]==xia[3]) or (shang[5]==xia[5]):
    c=True

if a==True:
	tmp.append("A")
	

if b==True:
	tmp.append('B')
	
if c==True:
	tmp.append('C')
if a==False and b==False and c== False:
	tmp.append("None")
	
print("".join(map(str,tmp))) 