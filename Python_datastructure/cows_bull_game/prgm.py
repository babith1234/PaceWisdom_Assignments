import random

def generate_random():
    digits = random.sample(range(10),4)
    return ''.join(map(str,digits))


match_list = [0 for _ in range(0,4)]


def main():
    print("Welcome to Cows and Bulls Game!")
    secret_number = generate_random()
    print(secret_number)

    bull_count=0
    cow_count=0
    guess_count = 0

    while True:
        guessed_number = input("Enter a 4-digit number")
        guess_count+=1

        if len(guessed_number)<4 or not guessed_number.isdigit():
            print("Please Enter a valid 4 digit number")
            continue

        if secret_number == guessed_number:
            print("guessed_count ",guess_count)
            print("Bulls=",bull_count," ","Cows=",cow_count)
            break
         
        i=0 
        while(i<len(guessed_number)):
            if(guessed_number[i]==secret_number[i] and not match_list[i]):
                cow_count+=1
                match_list[i]=1
            elif(guessed_number[i]!=secret_number[i] and match_list[i]):
                cow_count-=1
                bull_count+=1
                match_list[i]=0
            i+=1
        print(cow_count," cows",", ",bull_count," bulls")    
 
if __name__ == "__main__":
    main()
         
