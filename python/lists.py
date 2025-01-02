l=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,'hello',True,12.43]
print(len(l))
print(l)
for i in l:
    print(i)
print(l[::2])
print(l[-15:])
if 16 in l:
    print('yes')
li=[i*i for i in range(10) if i%2==0]
print(li)
l.append(16)
lis=[3,1,1,1,1,6,4,7,5,9]
lis.sort()
print(lis)
lis.sort(reverse=True)
print(lis.index(6))
print(lis.count(1))
m=l.copy()
lis.insert(4,57)
l.extend(m)   #you can also make a new list by doing k=l+m  