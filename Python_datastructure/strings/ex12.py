string = input("Enter the string")

upper_count=0

for i in range(0,len(string)):
    i=1
    if string[i]>='A' and string[i]<='Z':
        upper_count+=1
    i+=1
    if i==4:
        break

if upper_count>=2:
    string = string.upper()

print(string)    