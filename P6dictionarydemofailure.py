#here i am not going to use sets at all, just dictionaries and tuples as well to make it fair...
questions={'Q1':'What is easiest to hold when empty but most desired when full?','Q2':'What is used by a criminal and by a housewife?','Q3':'What brings comfort and hurts you in the same hour?','Q4':'What costs more as it gets smaller?','Q5':'What comforts the homeless but can make someone be homeless?'}
print(questions)
#the above prints the whole dictionary, below prints the value for that key...
print(questions['Q1'])
questions['Q6']='What does the fox say?'
#now we have added a new entry
print(questions)
questions['Q5']="IT'S OVER 9000!!!"
#now we have changed an entry
print(questions)
questions.pop('Q5')
#now we have deleted an entry
print(questions)
#the usage of functions and their fullfillment will be seen in the final game.