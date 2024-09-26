string = input("Enter the string")

for i in range(0,len(string)):
    if string[i]=='.':
        dot_index=i
    if string[i]==',':
        comma_index=i


new_list=list(string)
new_list[dot_index] = ","
new_list[comma_index] = "."

print(''.join(new_list))
