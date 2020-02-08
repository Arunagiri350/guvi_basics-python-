import math
l=list(map(int,input().split()))
a=l[0]
b=l[1]
p=a*b
sq=math.sqrt(p)
sq1=math.floor(sq)
if (sq-sq1)==0:
  print("yes")
else:
  print("no")
