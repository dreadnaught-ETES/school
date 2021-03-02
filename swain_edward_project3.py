import random
wordlist='aquarius','aquatic','amused','acerbic','alien','alienate','bemused','mischief','holistic','manual','malnourished','misdemeanor','felony','discharge','disembowel','echelon','epilepsy','pestilent','vestibule','dazed','contrary'
word=random.choice(wordlist)
name=input("Please tell me your name, player: ")
print(f"Hello, {name}, let's play a game.")
print("             ****The Hanged Man****")
print("You have 10 tries to guess my word before the man is hung.")
wrong_list=[]
print(f"      My word has {len(word)} letters. Good Luck, {name}.")
guess_list=[]
for i in range (len(word)):
    guess_list.append("_")
print(*([i for i in guess_list]))
tries=10
success=[]
for i in range (len(guess_list)):
    success.append("_")
while (tries>0):
    guess=input("Please guess a letter: ")
    if not guess.isalpha():
        print("Please make sure your guesses are only letters of the alphabet. Do try to not overcomplicate this...")
        tries+=-1
    elif (len(guess)>1):
        print("I would thank you to keep your guess to just one letter...")
        tries+=-1
    elif (guess in wrong_list):
        print("Deja vu? You have guessed that letter before...")
        tries+=-1
    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                guess_list[i]=word[i]
                success[i]=guess_list[i]
                if [i for i in success]==[i for i in word]:
                    print(*([i for i in success]))
                    print("You guessed my word and the man was saved. Congratulations.")
                    exit(0)
    else:
        print("That letter is not in my word. I'm sorry...")
        wrong_list.append(guess)
        tries+=-1
    print("You have already guessed",*([i for i in wrong_list]))
    print(*([i for i in guess_list]))
    print(f"You have {tries} tries left.")
    if tries==-1:
        print("You have failed and the man has been hanged...")
        print("It's your own fault for giving the same letter every time...")
        print(f"My word was {word}...")
    while tries==0:
        if [i for i in success]==[i for i in word]:
            print("You guessed my word and the man was saved. Congratulations.")
            exit(0)
        if [i for i in success]!=[i for i in word]:
            print(f"You have lost and the man was hanged! My word was {word}")
            exit(0)