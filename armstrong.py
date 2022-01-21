'''
armstrong number is number of n digit which are equal to nth power of its digit

for example take '153'
length = 3
1**3 + 5 ** 3 + 3 ** 3 = 153 which is equal to the '153'

'''


for i in range(1001):
    n = i
    n_len = len(str(n))
    result = 0
    while (n!=0):
        digit = n % 10
        result = result + digit ** n_len
        n = n // 10
    if result == i:
        print(result)