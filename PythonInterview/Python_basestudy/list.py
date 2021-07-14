list0=[]
list1=[1,2,3]
print(list1[1])
print(list1[len(list1)-1])
print(list1[-1])
print(id(list1))
list1.append(4)
list1.append(5)
print(id(list1))
list2=list1
print((id(list2)))
list1.insert(1,33)
print(list1)
list1.extend([44,55,66])
print(list1)
del list1[2]
print(list1)
s=list1.pop()
print(list1)
print(s)
list1.remove(55)
print(44 in list1)
#enumrate的第二个参数，为初始计数值
for i,value in enumerate(list1,3):
    print(i,value)

print(list1.count(44))
print(list1)
print(id(list1))
list1.reverse()
print(list1)
print(id(list1))

list1.sort()
print(list1)
