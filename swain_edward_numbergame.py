import random
num=random.randint(1,100)
lives=5
gameOver=False
while lives == 0:
    gameOver=True
while not gameOver:
    guess=int(input("Guess my number (1 to 100): "))
    if guess==num:
        print("You got it dude.")
        print("YOU WIN!")
        gameOver=True
        break
    while guess != num:
        if guess > num and guess < 100:
            print("Too high, bub.")
            gameOver=False
            lives += -1
            if lives == 0:
                gameOver=True
                print("GAME OVER")
                break
            print("Guess again, dude. You have",lives,"tries left.")
            break
        if guess < num and guess > 1:
            print("Too low, yo.")
            gameOver=False
            lives += -1
            if lives == 0:
                gameOver=True
                print("GAME OVER")
                break
            print("Guess again, dude. You have",lives,"tries left.")
            break
        if guess > 100 or guess < 1:
            print("Dude, seriously? 1 to 100 means keep it between the lines, dog.")
            gameOver=False
            lives += -1
            if lives == 0:
                gameOver=True
                print("GAME OVER")
                break
            print("Guess again, dude. You have",lives,"tries left.")
            break
#troubleshooting this was a beast. The right answer has to come before the second loop...i am ashamed to say it took me an hour to realize that.
#I spliced the concept of number guessing with a text adventure game i had done before to add lives and make it loop.
#These are always fun to make. 
#The winning statement is a quote from the little girl from full house. Cookies if you knew that already.
