n,m = 5,15

for i in range(n,m+1):
    if i > 1:
        for j in range(2,i):
            if i%j == 0:
                print("this is not a prime number")
                break
        else:
            print("prime number",i)

# to check if the number is prime or not

num = 5

if num > 1:
    for i in range(2,num):
        if num%i == 0:
            print("No prime number hai")
            break
    else:
        print("prime number")
else:
    print("no prime number hai")