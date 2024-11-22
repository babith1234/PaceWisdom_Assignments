array=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
new_list=[]
for i in array:
    if i not in new_list:
        new_list.append(i)
print(new_list)