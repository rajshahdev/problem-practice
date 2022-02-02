k = [10,15,4,23,0]


# if string then 
# kstr = 'raj'
# k = []
# for i in kstr:
#     k.append(i)
# print(k)

for j in range(len(k)-1):
    for i in range(len(k)-1-j):
        if k[i] > k[i+1]:
            k[i],k[i+1] = k[i+1], k[i]

print(k)