"""
n = 5
then we've to print the below pattern
*****
****
***
**
*
"""


n = int(input("enter the 'n' "))
for i in range(1,n+1):
    for j in range(i,n+1):
        print("*", end="")
    print()