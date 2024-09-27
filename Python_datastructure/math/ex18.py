
odd=[]
even=[]
prime=[]

for i in range(1,101):
    flag=0
    if i%2==0:
        even.append(i)
    elif i%2!=0:
        odd.append(i)
    for j in range(2,(i//2)+1):
        if i%j==0:
            flag=1
            break   
    if flag==0:
        prime.append(i)

# print(even)
# print(odd)
# print(prime)

for num in even:
    if num%4==0 and num%6==0 and num%8==0 and num%10==0 and num%3==0 and num%5==0 and num%7==0 and num%9==0:
        print(num,end=",")

for num in odd:
    if num%4==0 and num%6==0 and num%8==0 and num%10==0 and num%3==0 and num%5==0 and num%7==0 and num%9==0:
        print(num,end=",")        