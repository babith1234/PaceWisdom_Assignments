string = input("Enter the string")
newString=""
if(len(string)<2):
    print("Empty string")
else:
    newString+=string[0:2]+string[-2:]
    print(newString)
