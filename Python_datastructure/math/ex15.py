sum=0
product=1
i=0
while(True):
    num=int(input("Enter any number"))
    sum+=num
    product*=num
    i+=1
    char = input("Press q to quit")

    if char=="q":
        break

print("Average: ",sum/i)
print("Product: ",product)
