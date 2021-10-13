import math


a = int(input("Please enter the numerator value: "))
while (a<1):
    print("Please re-enter the valid numerator! Value must be greater than 0")
    a = int(input("Re-enter the numerator value: "))


b = int(input("Please enter the denominator value : "))
while (b<1):
    print("Please re-enter the valid denominator! Value must be greater than 0")
    b = int(input("Re-enter the denominator value : "))

formula = math.gcd(a, b)

if (a < b):
    print (f"{a}/{b} is a proper fraction")
    if formula == 1:
        print("This proper fraction cannot be reduced any further")
    elif formula != 1:
        a //= formula
        b //= formula
        print(f"This proper fraction can be reduced to: {a}/{b}")
             
elif (a > b):
    print (f"{a}/{b} is a improper fraction")
    if formula == 1 :
        print("This improper fraction cannot be reduced any further")
    elif formula != 1 :
        a //= formula
        b //= formula
        print(f"This improper fraction can be reduced to: {a}/{b}")
        
    mix = a // b
    rmdr = a % b
    if rmdr != 0:
        print ("The mixed number is :'{} and {}/{}'".format(mix, rmdr, b))
    elif rmdr == 0:
        print(f"The whole num is {mix}")
        
