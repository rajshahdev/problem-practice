# if we want to find in a range
num1 = 5
num2 = 30
for num in range(num1,num2):
    result = 0
    for i in range(1,num):
        if num%i == 0:
            # print(i)
            result = result + i

    if num == result:
        print("the given number is perfect number", num)
    # else:
    #     print("not a pefect number")


# if we want to find a particular perfect number
num = 6
result = 0
for i in range(1,num):
    if num%i == 0:
        # print(i)
        result = result + i

if num == result:
    print("the given number is perfect number", num)