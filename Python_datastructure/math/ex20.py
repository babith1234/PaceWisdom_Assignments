list=[]
n = int(input("Enter n"))
for _ in range(n):
    list.append(int(input()))

new_list = []

new_list = [(num*num) for num in list]

print(new_list)