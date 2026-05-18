import random
from word_list import words as word_list
from hangman_art import stages


chosen_word = random.choice(word_list)
placeholder=""
for letter in chosen_word:
    placeholder += "_"

print(placeholder)

game_over= False
correct_letters=[]

lives=6

while not game_over:
    print(f"******************** {lives} LIVES LEFT!  ********************")

    guess = input("Write a letter to check if it is in word: \n")

    if guess in correct_letters:
        print("You already guessed this letter. No lives lost.\n" )

    display=""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word and guess not in correct_letters:
        lives-=1
        print(f"You guessed {guess}, that's not in the word. You lose a life. \n")



    print(display)
    print(stages[lives])

    if "_" not in display:
        game_over=True
        print("******************** YOU WIN! ********************")
    elif lives==0:
        print(f"******************** IT WAS {chosen_word}, GAME OVER   ! ********************")
        game_over=True