import turtle
t=turtle.Turtle()
sidel=int(input("Enter the length of the sides of your shape: "))
siden=int(input("Enter the number of sides for your shape: "))
color=input("Please enter the name or hex value (i.e. #RRGGBB) of your color: ")
t.fillcolor(color)
t.begin_fill()
for _ in range(siden):
    t.forward(sidel)
    t.right(360/siden)
t.end_fill()
#i had to look up some things for this and splicing what i found together was an interesting process.
#you absolutely NEED the empty parentheses at the ends...