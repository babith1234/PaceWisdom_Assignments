a=[{1:10, 2:20},{3:30, 4:40},{5:50,6:60}] 
b={}
for i in a:
    for j in i:
        print(j)
        b[j]=i[j]
print(b)