L1=[12,23,23,56,67,24]
count=0
for i in L1:
    count+=1
print (count)

L1.remove(L1[3])
print(L1)

L1.insert(0,33)
print(L1)

L1.append(99)
print(L1)

if 67 in L1:
    print("67 is here in",L1.index(67))
'''
for k in L1:
    if k==67:
        #break
        print("67 is in position",L1[i])
        break
    else:
        print("67 is not here")
        break
'''