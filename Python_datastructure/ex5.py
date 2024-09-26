string1 = input("Enter the string")
string2 = input("Enter the string")

temp1 = string1[0:2]
temp2 = string2[0:2]

string1 = string1.replace(temp1,temp2)
string2 = string2.replace(temp2,temp1)

print(string1)
print(string2)