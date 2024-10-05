list=[]
n = int(input("Enter n"))
for _ in range(n):
    list.append(int(input()))

key = int(input("Enter the key to remove"))
print(list)

for num in list:
    if num==key:
        list.remove(num)

print(list)        