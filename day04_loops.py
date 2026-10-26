for i in range(1,6):
    print(i)
    #sum of given numbers
total=0
for i in range(1,6):
    total=total+i
    print(total)
    #sum of even numbers
total=0
for i in range(2,6,2):
    total=total+i
    print(total)
    #while loop
    i=1
    while i<=5:
        print(i)
        i=i+1
print("Break Example:")

for i in range(1, 6):
    if i == 3:
        break
    print(i)

print("Continue Example:")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)
for i in range(1,6):
    for j in range(1,3):
        print(i,j)
print("star pattern")
for i in range(1,5):
    for j in range(1,5):
        print("*",end="")
    print( )
for i in range(1,5):
    for j in range(i):
        print("*",end=" ")
    print( )
#multiplication table
number=5
for i in range(1,11):
    result=number*i
    print(f"{number}x{i}={result}")