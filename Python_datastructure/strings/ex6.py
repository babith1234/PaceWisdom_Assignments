string = input("Enter the string")

if(len(string)<3):
    print(string)
    
else:
    if string[-3:]=="ing":
        string+="ly"
        print(string)
    else:
        string+="ing"
        print(string)

