#PI Computation
import math

i=1
j=3
#limit=pow(10,2)
#limit = 10 ** 9 # 1 Bilione # 8
#limit = 10 ** 8 # 7
limit = 10 ** 7 # 6
#limit = 10 ** 6 # 5
#limit = 10 ** 5 # 4
# limit = 10 ** 4 # 3
#limit = 10 ** 3 # 1
# limit = 10 ** 9 # 10 Bilione # 8

pi1=0
pi2=0
#3.1415926
while(i <= limit ):
    pi1 = pi1 + (4.0 / i)
    i = i + 4
    pi2 = pi2 - (4.0 / j)
    j = j + 4

    #if( i>=10**8 or i==10**9):
    #print(i , " : " ,   pi1, " | ", j, " : ", pi2)
    #print(" ")

    # print(j, " : ", pi2)
    #print(" ")

# while (j <= limit):
#     pi2 = pi2 - (4.0 / j)
#     j = j + 4
#     print(i , " : " , pi2)
#     print()

print(pi1)
print()
print(pi2)
print()
print()

pi0 = pi1+pi2
print("PI = ",pi0)

