list = []

n = int(input("Enter the value of n"))

for _ in range(0,n):
    list.append(input())

max_word=0
for word in list:
    max_word = max(len(word),max_word)

print(max_word)

