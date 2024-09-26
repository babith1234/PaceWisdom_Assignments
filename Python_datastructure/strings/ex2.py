string = input("Enter the string")
frequency = {}

for char in string:
    if char not in frequency:
        frequency[char]=1
    else:
        frequency[char]+=1


print(frequency)            
