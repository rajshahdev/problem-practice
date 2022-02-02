k = sorted("dad")
j = sorted("dad")
if len(k) == len(j):
    if k == j:
        print("string is anagram")
    else:
        print("string is not anagram")
else:
    print("string is not anagram")

# list1 = []
# for i in k:
#     list1.append(i)

# for j in range(len(list1)-1):
#     for i in range(len(list1)-1):
#         if list1[i] > list1[i+1]:
#             list1[i], list1[i+1] = list1[i+1], list1[i]

# j = ''.join(list1)
