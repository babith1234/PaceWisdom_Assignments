string = input("Enter the string")
char = string[0]
new_string=char

for i in range(1,len(string)):
    if string[i]==char:
        new_string+="$"
    else:
        new_string+=string[i]    

print(new_string)
