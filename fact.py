# using recursion

def fact(n) -> int:
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
n = 5
print(fact(n))

result = 1
for i in range(n,0,-1):
    result = result * i

print(result)
