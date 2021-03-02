inventory = {'wallet','cat','TV','matches','knife'}
#this is the set version of the demonsration so i will be using the set for both parts of the completed product.
questions = {'Q1','Q2','Q3','Q4','Q5'}
Q1 = "What is easiest to hold when empty but most desired when full?"
Q2 = "What can commit a crime and also be used daily?"
Q3 = "What costs more the smaller it gets?"
Q4 = "What can hurt you and comfort you in the same hour?"
Q5 = "What comforts the homeless but can make someone be homeless?"
#so I'm running into an organizational issue where the question numbers and their text values are redundant.
#this is only going to get worse since i have to connect the questions to answer values...
#i can use a tuple for this part to make it work, a dictionary would work for this too, but im not using those in this demonstration...
Q1A,Q2A,Q3A,Q4A,Q5A='wallet','knife','TV','cat','matches'
answers = {'Q1A','Q2A','Q3A','Q4A','Q5A'}
#theres the right answer list, the if/else statements of the game in the final product will determine the links between the questions and the answers
#let the demonstration begin....
print(questions)
print(answers)
print(Q1)
print(Q1A)
#theres actually not a lot of versatility with sets for this specific of a game basis. 
#this is why i need dictionaries. when you use only one method for recall, you cant connect things properly.
#with a lot of effort i could likely make this work with only lists, if/elses, loops, and tuples.
#but that effort is what makes things like this both redundant and uninteresting.
#the final product will be much different