dic={1:'a',2:'b'}
a=int(input("Enter the key(num):"))
for i in dic:
    if i==a:
        print("Key already exists")
        break
else:
    print("It doesn't exist")