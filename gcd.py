l=list(map(int,input().split()))
m=l.pop()
n=l.pop()
gcd=1
i=2
while n<=i and m<=i:
  if n%i==0 and m%i==0:
    gcd=i
  i=i+1
if n==0 or m==0:
  print("-1")
else:
  print(gcd)
