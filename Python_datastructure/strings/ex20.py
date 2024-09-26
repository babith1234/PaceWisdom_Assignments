string = input("Enter the string")
new_string=""

for i in range(0,len(string)-1):
    if string[i]!=string[i+1]:
        new_string+=string[i]

print(new_string)
        
