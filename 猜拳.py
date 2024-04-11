browin=False
siswin=False
#input()--------------------------
F=int(input())
N=int(input())
sis=[int(a) for a in input().split()]
#---------------------------------



for k in range(N):
  print(F,end=' ')
  if (F==0 and sis[k]==2) or (F==2 and sis[k]==5) or (F==5 and sis[k]==0):
    print(f': Won at round {k+1}')
    browin=True
    break
  elif (F==2 and sis[k]==0) or (F==5 and sis[k]==2) or (F==0 and sis[k]==5):
    print(f': Lost at round {k+1}')
    siswin=True
    break

#判斷下次出拳(哥)-------------------
  if sis[k]==sis[k-1]:
    if sis[k]==0:
      F=5
    if sis[k]==2:
      F=0
    if sis[k]==5:
      F=2
  else:
    F=sis[k]
#----------------------------------

if browin==False and siswin==False:
  print(f': Drew at round {k+1}')

