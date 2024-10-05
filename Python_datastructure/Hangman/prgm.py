import random


list = []
correct_guess=""

with open('input.txt', 'r') as file:
    for line in file:
        list.append(line.strip())

def random_guess():
      gueesed_word = random.choice(list)
      print(gueesed_word)
      return gueesed_word
  

def user_guess_letter():
       print(f"Your correctly guessed till here: {correct_guess}")
       guessed_letter = input("Guess your Letter:")
       return guessed_letter


def user_guess():
    global correct_guess
    guess_count = 6
    random_word = random_guess()
    guessed_letters =[]
    word_index=0
    print("Welcome to Hangman!")
   

    while guess_count:
        letter = user_guess_letter()
        if letter == random_word[word_index] and word_index != len(random_word)-1:
            word_index+=1
            correct_guess+=letter
        else:
            if letter not in guessed_letters:
                guess_count-=1
                print("Incorrect guess")
                print(f"Your Left with{guess_count} attempts")
                             
        guessed_letters.append(letter)

    if word_index == len(random_word)-1:
            print("You won the Game")
    else:
         print("Your attempts are done .You lost the Game, please start a new game")
    user_guess()


if __name__ == "__main__":
    user_guess()            

