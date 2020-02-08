n=int(input())
s=list(map(int,input().split()))
l=s[0]
r=s[1]
for x in range(l,r+1):
  if x==n:
    print("yes")
    break
else:
  print("no")
