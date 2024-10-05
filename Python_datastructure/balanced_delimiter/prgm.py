delimitter = input("Enter the string")

stack = []
flag=1

for char in delimitter:
    if char=='(' or char=='[' or char=='{':
        stack.append(char)
    elif (char==')' and stack[-1]=='(') or (char==']' and stack[-1]=='[' )or (char=='}' and stack[-1]=='{'):
        stack.pop() 
    else:  
        print("false")
        break
        
if not stack:
    print("True")
else:
    print("False")

