list1 = [12,6,8,3,0,23,4,1]

for j in range(len(list1) - 1):
    for i in range(len(list1)-1 - j):
        if list1[i] > list1[i+1]:
            list1[i],list1[i+1] = list1[i+1], list1[i]
        
print(list1)