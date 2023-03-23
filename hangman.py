import random



def get_word():
    secret_word = ["ball", "doll", "golf", "secret", "thief",'wares', 'soup', 'mount', 'extend','brown','expert','tired', 'humidity', 'backpack','crust','dent','market','knock',]
    word = random.choice(secret_word)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    count=6
    print(" Hangman Guesses: 0")
    print("+--+\n"
          "|     \n"
          "|      \n"      
          "|\     \n")
    
    print("Word "+word_completion)
    print("\n")
    while not guessed:
        guess = input(" Guess a letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print("You are WRONG :(")
                count -= 1
                if count == 5:
                 print( " Hangman Guesses: " + str(tries - count))
                 print("+--+\n"
                       "|  O\n"
                       "|      \n"      
                       "|\     \n")
                elif count == 4:
                 print( " Hangman Guesses: " + str(tries - count))
                 print("+--+\n"
                  "|  O\n"
                  "|  |  \n"      
                  "|\    \n")
                elif count == 3:
                 print( " Hangman Guesses: " + str(tries - count))
                 print("+--+\n"
                  "|  O\n"
                  "| /|   \n"      
                  "|\     \n")
                elif count == 2:
                 print( " Hangman Guesses: " + str(tries - count))
                 print("+--+\n"
                  "|  O\n"
                  "| /|\   \n"      
                  "|\     \n")
                elif count == 1:
                 print( " Hangman Guesses: " + str(tries - count))
                 print("+--+\n"
                  "|  O\n"
                  "| /|\   \n"      
                  "|\/     \n")
            
                elif count == 0:
                 print(" Hangman Guesses: " + str(tries - count))
                 print("+--+\n"
                  "|  O\n"
                  "| /|\   \n"      
                  "|\/ \    \n")
                 print("YOU HAVE LOST :( :( :(")
                 print("The correct word was " + word)
                 print("Try again next time!")
                 while input("Play Again? (Y/N) ").upper() == "Y":
                  word = get_word()
                  play(word)
            

                guessed_letters.append(guess)
            else:
                print("You are CORRECT !!!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        
        
        print(word_completion)
        print("\n")
    if guessed:
        print("YOU HAVE WON")
        print("The word was " + word)
        while input("Play Again? (Y/N) ").upper() == "Y":
                  word = get_word()
                  play(word)

    
def main():
    word = get_word()
    play(word)
    


if __name__ == "__main__":
    main()