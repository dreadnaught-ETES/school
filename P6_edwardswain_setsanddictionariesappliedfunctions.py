import random
inventory = {'wallet','cat','TV','matches','knife'}
questions={'Q1':'What is easiest to hold when empty but most desired when full?','Q2':'What is used by a criminal and by a housewife?','Q3':'What brings comfort and hurts you in the same hour?','Q4':'What costs more as it gets smaller?','Q5':'What comforts the homeless but can make someone be homeless?'}
Q1,Q2,Q3,Q4,Q5=questions['Q1'],questions['Q2'],questions['Q3'],questions['Q4'],questions['Q5']
Q1A,Q2A,Q3A,Q4A,Q5A='wallet','knife','TV','cat','matches'
Q=(Q1,Q2,Q3,Q4,Q5)
ask=random.choice(Q)#it took everything i had available in the projects focii to make this work...
lives=2
gO=False
print("                         ***Welcome to Random Riddles***")
print("Look at your inventory of available items to find the answer to whatever questions are asked.")
print(f"                 You have {lives} 'lives' until game over.")
while lives > 0:
    print(f"You have {lives} lives left")
    print(inventory)
    print(ask)
    answer=input("What in your inventory is the answer? ")
    if ask==Q1:
        if answer.lower().strip()==Q1A.lower().strip():
            print("Good Job, you got it right.")
            gO=True
            exit(0)
        if answer.lower().strip()!=Q1A.lower().strip():
            print("That's wrong my dude, try again.")
            lives+=-1
            gO=False
    if ask==Q2:
        if answer.lower().strip()==Q2A.lower().strip():
            print("Good Job, you got it right.")
            gO=True
            exit(0)
        if answer.lower().strip()!=Q2A.lower().strip():
            print("That's wrong my dude, try again.")
            lives+=-1
            gO=False
    if ask==Q3:
        if answer.lower().strip()==Q3A.lower().strip():
            print("Good Job, you got it right.")
            gO=True
            exit(0)
        if answer.lower().strip()!=Q3A.lower().strip():
            print("That's wrong my dude, try again.")
            lives+=-1
            gO=False
    if ask==Q4:
        if answer.lower().strip()==Q4A.lower().strip():
            print("Good Job, you got it right.")
            gO=True
            exit(0)
        if answer.lower().strip()!=Q4A.lower().strip():
            print("That's wrong my dude, try again.")
            lives+=-1
            gO=False
    if ask==Q5:
        if answer.lower().strip()==Q5A.lower().strip():
            print("Good Job, you got it right.")
            gO=True
            exit(0)
        if answer.lower().strip()!=Q5A.lower().strip():
            print("That's wrong my dude, try again.")
            lives+=-1
            gO=False
while lives == 0:
    print("Sorry dude, Game OVER")
    gO=True
    exit(0)