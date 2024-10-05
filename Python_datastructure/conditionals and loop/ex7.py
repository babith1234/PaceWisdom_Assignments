n = int(input("Enter n"))
list=[]

for _ in range(n):
    list.append(int(input()))

count = 0

for num in list:
    if num>30:
        count+=1
print(count)