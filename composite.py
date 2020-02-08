a=int(input())
if a>1:
  for j in range(2,(a//2)+1):
    if a%j==0:
      print('yes')
      break
  else:
    print('no')
elif a==1:
  print('no')
