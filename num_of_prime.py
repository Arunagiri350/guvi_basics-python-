l=list(map(int,input().split()))
r=l.pop()
l=l.pop()
count=0
for i in range(l,r+1):
    if i>1:
        for j in range(2,(i//2)+1):
            if i%j==0:
                break
        else:
            count=count+1
    elif i==1:
        count=count+1
print(count)
