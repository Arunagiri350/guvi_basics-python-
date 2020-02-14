l=list(map(int,input().split()))
a=l.pop()
b=l.pop()
c=l.pop()
if (a+b<=c) or (b+c<=a) or (a+c<=b):
  print('no')
else:
  print('yes')
