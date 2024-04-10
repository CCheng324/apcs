for i in range(int(input())):
  tmp=[]
  s=[int(a) for a in input().split()]
  x=[int(b) for b in input().split()]
  
  if not(all(c[1]!=c[3] and c[1]==c[5] for c in [s,x])):
    tmp.append("A")
  if not(s[6]==1 and x[6]==0):
    tmp.append("B")
  if not((s[1]!=x[1] and s[3]!=x[3] and s[5]!=x[5])):
    tmp.append("C")

  if tmp==[]:
    print("None")
  else:
    print(*tmp,sep="")
