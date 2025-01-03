list1=list(input('Enter list:'))
a=len(list1)
b=int(a/2)
c=int((a/2)-(a%2))
if a % 2== 1 :
    print(list1[b])
else:
    print(list1[c-1],list1[c])
   