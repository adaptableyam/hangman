import random
import sys
from pathlib import Path


def main():

    hangman = (

    """
    _________
        |/        
        |              
        |                
        |                 
        |               
        |                   
        |___                 
        """,

    """
    _________
        |/   |      
        |              
        |                
        |                 
        |               
        |                   
        |___                 
        H""",

    """
    _________       
        |/   |              
        |   (_)
        |                         
        |                       
        |                         
        |                          
        |___                       
        HA""",

    """
    ________               
        |/   |                   
        |   (_)                  
        |    |                     
        |    |                    
        |                           
        |                            
        |___                    
        HAN""",


    """
    _________             
        |/   |               
        |   (_)                   
        |   /|                     
        |    |                    
        |                        
        |                          
        |___                          
        HANG""",


    """
    _________              
        |/   |                     
        |   (_)                     
        |   /|\                    
        |    |                       
        |                             
        |                            
        |___                          
        HANGM""",



    """
    ________                   
        |/   |                         
        |   (_)                      
        |   /|\                             
        |    |                          
        |   /                            
        |                                  
        |___                              
        HANGMA""",


    """
    ________
        |/   |     
        |   (_)    
        |   /|\           
        |    |        
        |   / \        
        |               
        |___           
        HANGMAN""")
    
    MAX_WRONG = len(hangman) - 1
    WRONG_GUESS = -1
    

    playing = input("Hello, would you like to play hangman? (Y/N) ")
    if playing.lower() == "yes" or playing.lower() == 'y':
        #Main Game loop, runs while playing
        while True:
            won_game = False
            wrong = 0
            letters = []

            print("\nGreat! Here we go..")

            word = loadWord("wordlist.txt")
            so_far = "_" * len(word)
            placements = []

            #Runs until game over
            while wrong != MAX_WRONG:

                so_far = "".join(so_far)
                if so_far == word:
                    won_game = True
                    break
                
                #These keep the player current on game conditions: How many wrong, letters used, chars in word, word so far.
                print(hangman[wrong])
                print(f"\nThe letters you've used so far are: {letters}\n")
                print(f"({len(word)} Characters) Your word so far is: {so_far}")


                #Convert into list so can replace the _'s with the correct letters using indexing
                so_far = list(so_far)
                
                guess = input("Make your guess: ").upper()

                validateGuess(guess, letters)

                for i, char in enumerate(word):
                    answer = evaluateGuess(guess, i, char)
                    if answer == None:
                        continue
                    else:
                        placements.append(answer)

                if len(placements) == 0:
                    wrong += 1

                else:
                    for x in range(len(placements)):
                        so_far[placements[x]] = guess

                placements.clear()

            #Print statements for end of game
            print(hangman[wrong])
            print("Game over!\n")
            if won_game:
                print("Congratulations, you win!")
            else:
                print("Better luck next time!")
            print(f"Your word was: {word}")

            #Post game loop, offers play again functionality
            play_again = input("Would you like to play again? (Y/N) ")
            if play_again.lower() == "yes" or play_again.lower() == 'y':
                continue
            else:
                sys.exit()
            
    else:
        sys.exit()


def evaluateGuess(guess, i, char):

    if guess == char:
        return i
    else:
        return None


def validateGuess(guess, letters):


    while len(guess) != 1:
        print("Please submit only 1 character")
        guess = input("Make your guess: ").upper()
    
    while guess in letters or len(guess) != 1:
        print("\nYou've already guessed that letter!\n")
        print(f"The letters you've used so far are: {letters}\n")
        guess = input("Make your guess: ").upper()
    
    letters.append(guess)
    return letters


def loadWord(file):
    word_list = []

    p = Path(__file__).with_name(file)

    with p.open('r') as f:
        for line in f:
            new_word = f.readline().strip()
            if new_word != '':
                word_list.append(new_word.upper().replace('\n', ''))

    word = random.choice(word_list)
    return word


if __name__ == '__main__':
    main()
