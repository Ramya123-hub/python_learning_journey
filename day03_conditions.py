age=int(input("enter age:"))
if age>=18:
    print("your eligible to vote")
else:
    print("your not eligible to vote")
    #elif statement
    marks=int(input("enter marks:"))
    if marks>=90:
        print("grade A")
    elif marks>=75:
        print("grade B")
    elif marks>=50:
        print("grade C")
    else:
        print("fail")
age=20
is_had=True
if age>=18 and is_had:
    print("your elgible to vote")
else:
    print("your not eligible to vote")
age=16
has_permission=True
if age>=16 or has_permission:
    print ("allowed")
else:
    print("not allowed")
marks = int(input("Enter your marks: "))
attendance = int(input("Enter your attendance percentage: "))

if marks >= 40 and attendance >= 75:
    print("Eligible for exam")
else:
    print("Not eligible for exam")
is_raining = False

if not is_raining:
    print("You can go outside")
else:
    print("Take an umbrella")

