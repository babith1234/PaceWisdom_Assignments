quantity = int(input("enter the quantity"))
cost = quantity*100

if cost>1000:
    final_cost = cost - (10/100)*cost
else:
    final_cost = cost

print(final_cost)        
