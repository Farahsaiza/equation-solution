import math
A=int(input("first number"))
B=int(input("second number"))
C=int(input("third number"))
D=B*B-4*A*C
if D>0:
    print("x1=",-B-math.sqrt(D)/2*A)
    print("x2=",-B+math.sqrt(D)/2*A)
elif D==0:
    print("x=",-B/2*A)
else:
    print("this equation is not solved in R")
