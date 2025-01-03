list1=list(input('Enter list:'))
index1=int(input('Enter index:'))                  
if index1-len(list1) < 0:

    print(list1[:index1],list1[index1+1:])
else:
    print('this index doesn\'t exist')
