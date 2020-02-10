l=list(input().split(" "))
b=l.pop()
a=l.pop()
if a==b:
  print("D")
else:
  if ((a=='R' and b=='P') or (a=='P' and b=='R')):
    print('P')
  elif ((a=='R' and b=='S') or (a=='S' and b=='R')):
    print('R')
  else:
    print('S')
