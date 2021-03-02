import math
num=int(input("Want to find out if a number is prime? Enter a number here: "))
nroot=int(math.sqrt(num))
start=2
stop=nroot+1
if num==2:
    print("Your number is prime and special. 2 is the only even prime number.")
if num > 1:
    for i in range(2, nroot):
        if (num%i)==0:
            print(num,"isn't Prime, since" ,i, "times",num//i,"equals",num,".")
            break        
        if (num%i)!=0:
            print(num,"is Prime. Lucky You.")
            break
else:
    print("Honey, keep it out of the negatives, and nobody wants to divide by zero.")
#ok so the problem i am running into with this is that the range is excluding everything but 2 if i enter it as "for i in range(2,nroot)..."
#my other option was to try a specific number such as the square root of a ridiculous number....that didnt work...for the same reasons.
#trying to test the exclusion didnt work. i tried nroot=int(math.sqrt(num)+1) to see if it was an exclusion problem.
#but for some reason... nothing works. the program only works if the the input is divisible by 2....
#i even tried altering the indentations but that just generated an error. the only other thing i can list as responsible for the issue...
#is the i in range coding itself... i tried to redefine start and stop points...that didnt work either...
