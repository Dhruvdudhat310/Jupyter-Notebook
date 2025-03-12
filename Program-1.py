list1,list2,list3 = [],[],[]

size = int(input("Enter size of list : "))
print()
print("Enter in list1 : ")
for i in range(size):
    ele1 = int(input("Enter Element :"))
    list1.append(ele1)

print()
print("Enter in list2 : ")
for i in range(size):
    ele2 = int(input("Enter Element :"))
    list2.append(ele2)

for i in range(size):
    ele3 = list1[i] + list2[i]
    list3.append(ele3)

print()
print(".....List3 is.....")
print(list3)
