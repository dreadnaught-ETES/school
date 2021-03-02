import random
number=random.randint(1, 10)
gO=False
C=5
print("Welcome to The Lair")
print("a text-based horror escape game where your only goal is to survive and escape")
print("***")
print("You fell asleep in your bed and woke up to find yourself in a stone cavern. You can hear a low, scratchy growl behind you.")
while C > 0: 
    CO1=int(input("There are three paths in front of you. You hear the growling closer than before and you can feel an icy cold and rancid smelling air brush across your ear. You run without thinking. Pick a number between 1 and 10: "))
    if CO1==number:
        print("Your footsteps seemed to thunder around you, echoing wildly off the slippery stone walls of the cavern.")
        print("Ahead you see a door, rusty and barely opened. With as much effort as you can manage, you shove past the door and into a room, slamming the door behind you.")
        print("Your blood chills as you look around. A corner of the room holds a mass of unidentifiable debris and human remains with a dark tunnel burrowed into it.")
        print("You see rusty barrels with half opened lids, some are filled with a dark fluid. And there is a half eaten corpse in the corner.")
        EP1=input("There must be something that can help you here. What do you investigate? (barrels/nest/corpse) ")
        if EP1.lower().strip() == 'nest':
            print("The fetid air flowing out of the burrow in the middle of the nest threatens to choke you as you get near the opening.")
            print("You swallow thickly, drowning your fear and senses in cold determination before slowly lowering your hands to touch the slick floor of the opening.")
            print("As you start forward on your hands and knees, feeling the fetid mucus-like substance of the lining seep through the fabric covering your knees,")
            print("something blurs into your vision, violently digging deeply and painfully into your hands. You try to cry out but your scream is silenced by the intrusion")
            print("of the next blur, which burrows its way out through your back. Your last awareness is the choking of your breath and warm wetness of your life coating the")
            print("bottom of the tunnel before being yanked down the tunnel into the moist and rotten darkness.")
            print("YOU HAVE BEEN KILLED AND EATEN BY MUTANT EARTHWORMS...")
            print("MORAL::: DON'T STICK YOUR FACE INTO A CREEPY NEST...")
            tAgain=input("Would you like to use a crystal to travel back and try again? (yes/no) ")
            if tAgain.lower().strip() == 'no':
                gO=True
                print("You gave up and did not escape.")
                exit(0)
            if tAgain.lower().strip() == 'yes':
                gO=False
                C += -1
                print(f"You have {C} crystals left. Good Luck.")
            else:
                gO=True
                print("You have lost your senses and fallen into madness...")
                exit(0)
        if EP1.lower().strip() == 'corpse':
            print("You steel yourself and creep towards the dessicated and half eaten corpse, trying not to take note of the exposed bones or obvious teeth marks.")
            print("Holding your breath, you dig around the body, searching whatever remains of its clothing and coming to a halt when your fingers brush against something that isn't flesh.")
            print("You pull out the object which looks like a small cylindrical case at closer inspection. You flip the slime covered latch and open the case.")
            print("You feel a shiver run up your spine as you pull out a long, thick syringe filled with a tar-like fluid that makes you feel uncomfortable to look at.")
            print("You grasp the syringe tightly and make your way to the only other exit in the room.")
            print("A syringe of whatever is better than nothing passes through your mind as you duck your way under the thick, dark, tendrils covering the hole in the eastern wall.")
            print("You stand straight after clearing the dark and unknown mass and immediately wish you hadn't.")
            print("The monster is crouched before you, hair lank and limp with rotting flesh hanging in trails off of its skeletal frame.")
            print("A low growl issues from it's throat as it looks at you with sickly yellow eyes set far too largely in a mottled and alien visage.")
            print("You only have 3 choices. Duck around it to reach the exit, try the syringe, or go back the way you came.")
            EP21=input("Which do you choose? (duck around/syringe/go back) ")
            if EP21.lower().strip() == 'duck around':
                print("The creature slams you into a wall so hard you feel your neck snap.")
                print("You can't move, paralyzed from the impact and a broken neck, the creature lopes gracelessly towards you.")
                print("It lowers it's face to yours and a cold rush of icy and death scented air passes between you before it")
                print("closes the gap between you, sinking razor sharp teeth into your chest and ripping it's way into a new meal.")
                print("You can't gather enough air to breathe, much less scream and your awareness fades with the sounds of squelching flesh")
                print("being shredded between inhuman jaws.")
                print("YOU HAVE BECOME THE MONSTER'S LATEST MEAL")
                print("MORAL::: DISTRACTIONS ARE IMPORTANT...")
                tAgain=input("Would you like to use a crystal to travel back and try again? (yes/no) ")
                if tAgain.lower().strip() == 'no':
                    gO=True
                    print("You gave up and did not escape.")
                    exit(0)
                if tAgain.lower().strip() == 'yes':
                    gO=False
                    C += -1
                    print(f"You have {C} crystals left. Good Luck.")
                else:
                    gO=True
                    print("You lost your senses and fell into madness...")
                    exit(0)
            if EP21.lower().strip() == 'go back':
                print("You shamelessly turn tail to run, weaving your way through the dark tendrils once again in the hopes that")
                print("the creature will get stuck amidst the vine-like growths. Suddenly the ground is pulled from beneath you as")
                print("the creature drags you back out from the corridor and up into the air in front of it's deathly rancid and icy breath.")
                print("It's large and grotesquely colored eyes glare into your own before it wraps one spindly and inhuman hand around your")
                print("head and pulls with a violent roar. You feel nothing else and know nothing else after a sickening crunch echoes through your skull.")
                print("THE MONSTER RIPPED YOUR HEAD OFF")
                print("MORAL::: NEVER TURN YOUR BACK WITHOUT THE UPPER HAND...")
                tAgain=input("Would you like to use a crystal to travel back and try again? (yes/no) ")
                if tAgain.lower().strip() == 'no':
                    gO=True
                    print("You gave up and did not escape.")
                    exit(0)
                if tAgain.lower().strip() == 'yes':
                    gO=False
                    C += -1
                    print(f"You have {C} crystals left. Good Luck.")
                else:
                    gO=True
                    print("You lost your senses and fell into madness...")
                    exit(0)
            if EP21.lower().strip() == 'syringe':
                print("You remember the syringe with that uncomfortably strange fluid inside and rummage in your bag to find it.")
                print("The creature screeches at you in rage and darts forward, nearly closing the distance before your hand pulls the")
                print("syringe out into the open. You don't hesitate or ponder the consequences, instead jamming the syringe deep into")
                print("the creature's neck as you use the force to pull yourself just barely out of it's path. The creature howls in pain,")
                print("a high-pitched and ear piercing wail assaulting your ears as it clasps its throat where the now empty syringe lies")
                print("embedded in dessicated flesh the color of mold. You can see the tar-like substance branching out into the monster's")
                print("body from the injection site, burning it's way through the monster's body. The wailing cuts off and the sudden silence")
                print("startles you as the monster collapses to the ground, it's body dissolving as the substance burns it away. The world sways")
                print("ripples around you and you start to panic as your vision blurs and darkness consumes you. You bolt upright in your bed,")
                print("right where you fell asleep before. The whole thing was a dream? You stare at your room in shock, the sweat running down")
                print("your body and making your clothes stick to you uncomfortably is all too real. You go to the bathroom and wash your face,")
                print("looking in the mirror for answers that aren't there before turning back to your room. A cold chill tears through your body")
                print("as you gaze at the object on your bed...there amongst your covers lies a clump of lank and greasy hair from a nightmare.")
                print("You decide it's time to move and spend the next two weeks packing and leave without giving any notice to your landlord.")
                print("Screw them...let them hunt you down. You've survived much worse...")
                print("YOU HAVE DEFEATED THE MONSTER THAT HELD YOU CAPTIVE AND ESCAPED THE LAIR")
                print("THE END")
                gO=True
                exit(0)
        if EP1.lower().strip() == 'barrels':
            print("You look inside the barrels one after another as quickly as you can.")
            print("The last barrel you look inside of is has various remains inside. You almost turn away but a glint at the bottom of the barrel catches your eye.")
            print("You brush aside the human detritus, trying to avoid having to vomit, and finally grasp a handle under your fingers before pulling out the object.")
            print("You look at your find, noting the worn grip and slippery blood covered barrel of the flare gun before turning to the only other exit in the room.")
            print("A flare gun is better than nothing passes through your mind as you duck your way under the thick, dark, tendrils covering the hole in the eastern wall.")
            print("You stand straight after clearing the dark and unknown mass and immediately wish you hadn't.")
            print("The monster is crouched before you, hair lank and limp with rotting flesh hanging in trails off its skeletal frame.")
            print("A low growl issues from it's throat as it looks at you with sickly yellow eyes set far too largely in a mottled and alien visage.")
            print("You only have 3 choices. Duck around it to reach the exit, try the flare gun, or go back the way you came.")
            EP22=input("Which do you choose? (duck around/flare gun/go back) ")
            if EP22.lower().strip() == 'duck around':
                print("The creature slams you into a wall so hard you feel your neck snap.")
                print("You can't move, paralyzed from the impact and a broken neck, the creature lopes gracelessly towards you.")
                print("It lowers it's face to yours and a cold rush of icy and death scented air passes between you before it")
                print("closes the gap between you, sinking razor sharp teeth into your chest and ripping it's way into a new meal.")
                print("You can't gather enough air to breathe, much less scream and your awareness fades with the sounds of squelching flesh")
                print("being shredded between inhuman jaws.")
                print("YOU HAVE BECOME THE MONSTER'S LATEST MEAL")
                print("MORAL::: DISTRACTIONS ARE IMPORTANT...")
                tAgain=input("Would you like to use a crystal to travel back and try again? (yes/no) ")
                if tAgain.lower().strip() == 'no':
                    gO=True
                    print("You gave up and did not escape.")
                    exit(0)
                if tAgain.lower().strip() == 'yes':
                    gO=False
                    C += -1
                    print(f"You have {C} crystals left. Good Luck.")
                else:
                    gO=True
                    print("You lost your senses and fell into madness...")
                    exit(0)
            if EP22.lower().strip() == 'go back':
                print("You shamelessly turn tail to run, weaving your way through the dark tendrils once again in the hopes that")
                print("the creature will get stuck amidst the vine-like growths. Suddenly the ground is pulled from beneath you as")
                print("the creature drags you back out from the corridor and up into the air in front of it's deathly rancid and icy breath.")
                print("It's large and grotesquely colored eyes glare into your own before it wraps one spindly and inhuman hand around your")
                print("head and pulls with a violent roar. You feel nothing else and know nothing else after a sickening crunch echoes through your skull.")
                print("THE MONSTER RIPPED YOUR HEAD OFF")
                print("MORAL::: NEVER TURN YOUR BACK WITHOUT THE UPPER HAND...")
                tAgain=input("Would you like to use a crystal to travel back and try again? (yes/no) ")
                if tAgain.lower().strip() == 'no':
                    gO=True
                    print("You gave up and did not escape.")
                    exit(0)
                if tAgain.lower().strip() == 'yes':
                    gO=False
                    C += -1
                    print(f"You have {C} crystals left. Good Luck.")
                else:
                    gO=True
                    print("You lost your senses and fell into madness...")
                    exit(0)
            if EP22.lower().strip() == 'flare gun':
                print("You scramble to make your fingers obey your commands as they seek the handle of the flare gun tucked away in")
                print("your bag. As soon as you feel them close on the worn grip, you clench them tightly and pull it out as the creature")
                print("screeches in rage and barrels towards you at a blinding speed. You squeeze the trigger as hard as you can,")
                print("fearful that it may be jammed and your death assured. Your heart skips beats in your chest as the creature leaps")
                print("at you before a blinding flash lights the darkness you had long since grown accustomed to without having realized it.")
                print("The monster screeches in both rage and pain now, covering it's eyes and you see the way out behind it.")
                print("You pray to whatever will listen before speeding towards the exit as fast as your legs can move your body.")
                print("Bright sunlights assails your eyes and you squint before falling down the embankment below the cave you just came out of.")
                print("You have no idea where you are but you no longer care. The monster's wailing in the caverns above spur you to move")
                print("and you get up shakily and stutter forward. The sun is sinking below the horizon before you see lights in the distance.")
                print("You laugh, uncertain and manic, before running headlong towards salvation...")
                print("YOU HAVE SURVIVED AND ESCAPED THE LAIR. YOU ARE SAFE")
                print("Or are you?")
                gO=True
                exit(0)
        else:
            print("At a loss for what to do, you leant against the wall with your head in your hands.")
            print("The thought that this may all be a nightmare creeps into your mind and you swear you can hear whispers of lullabies and 'Sleep' flit ")
            print("in and out of existance. You wonder if maybe there isn't a point there. Maybe this is a horrifying nightmare and nothing more.")
            print("The will to stay awake fades and your eyes close. The spirits of those who died here have gained another...")
            print("But there were worse ways to die right?")
            print("YOU HAVE BEEN GRANTED 'MERCY' BY THE DEAD AND JOINED THEIR RANKS")
            print("MORAL::: DON'T SLEEP IN PLACES OF DEATH...")
            tAgain=input("Would you like to use a crystal to travel back and try again? (yes/no) ")
            if tAgain == 'no'.lower().strip():
                gO=True
                print("You gave up and did not escape.")
                exit(0)
            if tAgain == 'yes'.lower().strip():
                gO=False
                C += -1
                print(f"You have {C} crystals left. Good Luck.")
            else:
                gO=True
                print("You lost your senses and fell into madness...")
                exit(0)
    if CO1 < number:
        print("You tear down the tunnel blindly, your footsteps shattering the silence with every footfall and the encroaching growls of")
        print("whatever follows you from behind. Your next step makes no sound and you look down in shock when nothing supports your weight.")
        print("You try to catch yourself but fail, falling into the darkness of the chasm below...you don't feel a thing when you hit the bottom.")
        print("YOU FELL TO YOUR DEATH IN A SECTION OF COLLAPSED CAVERN")
        print("MORAL::: LOOK BEFORE YOU LEAP...")
        tAgain=input("Would you like to use a crystal to travel back and try again? (yes/no) ")
        if tAgain.lower().strip() == 'no':
            gO=True
            print("You gave up and did not escape.")
            exit(0)
        if tAgain.lower().strip() == 'yes':
            gO=False
            C += -1
            print(f"You have {C} crystals left. Good Luck.")
        else:
            gO=True
            print("You lost your senses and fell into madness...")
            exit(0)          
    if CO1 > number:
        print("Your footsteps seemed to be loud in cavern's silence, echoing wildly off the slippery stone walls.")
        print("You run so far and so long you run out of breath and have to stop. You don't know how many twists and turns your path made but you are most definitely lost now.")
        print("At the very least, that growling has stopped and all you can hear is a low droning hum.")
        print("The hum seems to be getting louder the longer you hear it and as it rises in volume you swear you can feel it crawling up your spine in growing tremors.")
        print("What was a low drone has become a painstakingly unbearable flood of noise at a volume that rattles your bones.")
        print("As you feel something drip down and out of your ear, the world goes silent and your vision blurs at the edges before blackening altogether.")
        print("You know you are dying, and all you can think of is why it had to be you...")
        print("THE MONSTROUS VOICE OF SOLITUDE HAS SHATTERED YOUR BEING AND YOU HAVE DIED")
        print("MORAL::: MARK YOUR PATH")
        tAgain=input("Would you like to use a crystal to travel back and try again? (yes/no) ")
        if tAgain == 'no'.lower().strip():
            gO=True
            print("You gave up and did not escape.")
            exit(0)
        if tAgain == 'yes'.lower().strip():
            gO=False
            C += -1
            print(f"You have {C} crystals left. Good Luck.")
        else:
            gO=True
            print("You lost your senses and fell into madness...")
            exit(0)
#THANKS FOR PLAYING
# this actually took a good minute. i hope i dont get points docked for the story parts but i figured i would give my all 