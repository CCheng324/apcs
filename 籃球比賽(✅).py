score1=[int(x) for x in input().split()]#main 1
score2=[int(y) for y in input().split()]
score3=[int(z) for z in input().split()]#main 2
score4=[int(k) for k in input().split()]
home_win=0
guest_win=0

home1=sum(score1)
guest1=sum(score2)
if home1>guest1:
    home_win+=1
else:
    guest_win+=1
    
home2=sum(score3)
guest2=sum(score4)
if home2>guest2:
    home_win+=1
else:
    guest_win+=1

print(f"{home1}:{guest1}")
print(f"{home2}:{guest2}")
if home_win>guest_win:
    print("Win")
elif home_win==guest_win:
    print("Tie")
else:
    print("Lose")