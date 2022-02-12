n = 6
first = 0
second = 1

for i in range(n):
    print(first, end=" ")
    temp = first
    first = second
    second = temp + second

