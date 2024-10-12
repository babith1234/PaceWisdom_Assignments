a=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
b=[]
for i in a:
    if i not in b:
        b.append(i)
print(b)