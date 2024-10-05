x = int(input("X:"))
y = int(input("Y:"))
z = int(input("Z:"))

if x==y==z:
    print("Equilateral")
elif x==y or y==z or x==z:
    print("Isosceles")
else:
    print("Scalene")        