n=int(input())
l=list(map(int,input().split()))
b=1
for i in l:
  b=b&i
  if b==0:
    break
print(b)
