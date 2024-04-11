x_win=False
y_win=False
def w_or_f(x,y):
 if x-y<0:
  x_win==True
 else:
  y_win==True
#input()--------------------------
F=int(input())
N=int(input())
sis=[int(a) for a in input().split()]
#---------------------------------

f=[F]
for k in range(N):
  w_or_f(F,sis[k])
 
#判斷下次出拳(哥)-------------------
  if sis[k]==sis[k-1]:
    if sis[k]==0:
      F==5
      f.append(5)
    if sis[k]==2:
      F==0
      f.append(0)
    if sis[k]==5:
      F==2
      f.append(2)
  else:
    F==sis[k]
#----------------------------------
  if x_win==True:
    print(f'{} : Won at round {k+1}')
  elif y_win==True:
    print(f'{} : Lost at round {k+1}')
if x_win==False and y_win==False:
  print(f'{} : Drew at round {k+1}')
