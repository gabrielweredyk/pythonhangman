import random
blank = []
guesses = 7
guessed = []
solved = False
with open('words.txt', 'r') as f:
    wordlist = f.readlines()
    for i in range(len(wordlist)):
        wordlist[i] = wordlist[i].strip()
    w = wordlist[random.randint(0, len(wordlist) - 1)]
    for i in range(len(w)):
        blank.append("_")
    while guesses > 0:
        print(blank)
        print("You have", guesses, "guesses left")
        print("Guessed letters:", guessed)
        guess = input("Guess:")
        if guessed.count(guess) != -1 and len(guess) == 1:
            guessed.append(guess)
            right = False
            for i in range(len(w)):
                if (guess == w[i]):
                    blank[i] = guess
                    right = True
            if right == False:
                guesses -= 1
            else:
                for i in range(len(w)):
                    solved = True
                    if (blank[i] == "_"):
                        solved = False
                        break
        else:
            print("Guess was either already guessed or not a single letter")
        
        if solved:
            print(blank)
            print("Good job! You guessed", w, "correctly!")
            break
        
    
    if (solved == False):
        print("You lost! The word was", w)
    