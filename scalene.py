l=list(map(int,input().split()))
c=l.pop()
b=l.pop()
a=l.pop()
if a!=b and a!=c:
  if b!=c:
    print('yes')
  else:
    print('no')
else:
  print('no')
