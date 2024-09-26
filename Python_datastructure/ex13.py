string = input("Enter the string")
pattern = input("Enter the pattern")

flag=True
if len(pattern)>len(string):
    exit
for i in range(0,len(pattern)):
    if pattern[i]!=string[i]:
        flag=False

if flag==True:
    print(True)
else:
    print(False)    