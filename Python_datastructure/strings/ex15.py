string = input("Enter the string")

frequency_map = {}

for char in string:
    if char not in frequency_map:
        frequency_map[char]=1
    else:
        frequency_map[char]+=1;    

for char,frequency in frequency_map.items():
    if frequency!=1:
        print(char," ",frequency)