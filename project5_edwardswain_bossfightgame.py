B1,B2,B3,B4,B5='Pervy Dude','Glittergoth','Morelullz','RonaV','Karen'
B1H,B2H,B3H,B4H,B5H=1000,2000,4000,8000,16000
B1A,B2A,B3A,B4A,B5A=500,1000,1500,2000,4000
PDa,GGa,MLa,RVa,Ka='Close Proximity Mouth Breathing','Uncomfortably Intense Creeper Stare','Show Meme','Viral Cough','Let Me Speak to Your Manager'
pH=10000
attack=-500
defend=.50
potion=500
poison=-250
attackT='You swing away.'
defendT='You call your mom on speaker for safety'
potionT='You chug an energy drink.'
poisonT='You used Axe Body Spray'
gameOver=False
enemyH=0
enemyA=0
while pH > 0:#enjoy this crackfest btw
    print(f"Your health: {pH}")
    print(f"{B1}, {B2}, {B3}, {B4}, and {B5} have appeared to ruin your day and steal your tacos.")#i also realized that i cant remove any boss names after defeat since they are also a tuple.
    enemy=input(f"Who will you beat with your mighty bat? ")
    if enemy == 'pervy dude'.lower().strip():
        enemyH += B1H
        enemyA += B1A
        while enemyH > 0:#i found out the hard way that tuples cant do greater than or less than functions...its not compatible
            print(f"Your health: {pH}")
            print(f"Boss Health: {enemyH}")
            turn=input(f"What will you do:  Attack/Defend/Potion/Poison ")
            if turn == 'attack'.lower().strip():
                print(attackT)
                enemyH += attack
                print(f"Pervy Dude used {PDa}")
                pH -= B1A
                print(f"Your health dropped by {B1A}.")
            if turn == 'defend'.lower().strip():
                print(f"Pervy Dude used {PDa}")
                print(defendT)
                pH -= B1A*.50
                print("Your health dropped by",B1A*defend,".")
            if turn == 'potion'.lower().strip():
                print(potionT)
                print(f"Your health recovered by {potion}")
                pH += potion
                print(f"Pervy Dude used {PDa}")
                pH -= B1A
            if turn == 'poison'.lower().strip():
                print(poisonT)
                enemyH += poison
                print(f"Pervy Dude used {PDa}")
                pH -= B1A
                print(f"Your health dropped by {B1A}")
    if enemy == 'glittergoth'.lower().strip():
        enemyH += B2H
        enemyA += B2A
        while enemyH > 0:
            print(f"Your health: {pH}")
            print(f"Boss Health: {enemyH}")
            turn=input(f"What will you do:  Attack/Defend/Potion/Poison ")
            if turn == 'attack'.lower().strip():
                print(attackT)
                enemyH += attack
                print(f"{B2} used {GGa}")
                pH -= B2A
                print(f"Your health dropped by {B2A}.")
            if turn == 'defend'.lower().strip():
                print(f"{B2} used {GGa}")
                print(defendT)
                pH -= B2A*.50
                print("Your health dropped by",B2A*defend,".")
            if turn == 'potion'.lower().strip():
                print(potionT)
                print(f"Your health recovered by {potion}")
                pH += potion
                print(f"{B2} used {GGa}")
                pH -= B2A
            if turn == 'poison'.lower().strip():
                print(poisonT)
                enemyH += poison
                print(f"{B2} used {GGa}")
                pH -= B2A
                print(f"Your health dropped by {B2A}")
    if enemy == 'morelullz'.lower().strip():
        enemyH += B3H
        enemyA += B3A
        while enemyH > 0:
            print(f"Your health: {pH}")
            print(f"Boss Health: {enemyH}")
            turn=input(f"What will you do:  Attack/Defend/Potion/Poison ")
            if turn == 'attack'.lower().strip():
                print(attackT)
                enemyH += attack
                print(f"{B3} used {MLa}")
                pH -= B3A
                print(f"Your health dropped by {B3A}.")
            if turn == 'defend'.lower().strip():
                print(f"{B3} used {MLa}")
                print(defendT)
                pH -= B3A*.50
                print("Your health dropped by",B3A*defend,".")
            if turn == 'potion'.lower().strip():
                print(potionT)
                print(f"Your health recovered by {potion}")
                pH += potion
                print(f"{B3} used {MLa}")
                pH -= B3A
            if turn == 'poison'.lower().strip():
                print(poisonT)
                enemyH += poison
                print(f"{B3} used {MLa}")
                pH -= B3A
                print(f"Your health dropped by {B3A}")
    if enemy == 'RonaV'.lower().strip():
        enemyH += B4H
        enemyA += B4A
        while enemyH > 0:
            print(f"Your health: {pH}")
            print(f"Boss Health: {enemyH}")
            turn=input(f"What will you do:  Attack/Defend/Potion/Poison ")
            if turn == 'attack'.lower().strip():
                print(attackT)
                enemyH += attack
                print(f"{B4} used {RVa}")
                pH -= B4A
                print(f"Your health dropped by {B4A}.")
            if turn == 'defend'.lower().strip():
                print(f"{B4} used {RVa}")
                print(defendT)
                pH -= B4A*.50
                print("Your health dropped by",B4A*defend,".")
            if turn == 'potion'.lower().strip():
                print(potionT)
                print(f"Your health recovered by {potion}")
                pH += potion
                print(f"{B4} used {RVa}")
                pH -= B4A
            if turn == 'poison'.lower().strip():
                print(poisonT)
                enemyH += poison
                print(f"{B4} used {RVa}")
                pH -= B4A
                print(f"Your health dropped by {B4A}")
    if enemy == 'karen'.lower().strip():
        enemyH += B5H
        enemyA += B5A
        while enemyH > 0:
            print(f"Your health: {pH}")
            print(f"Boss Health: {enemyH}")
            turn=input(f"What will you do:  Attack/Defend/Potion/Poison ")
            if turn == 'attack'.lower().strip():
                print(attackT)
                enemyH += attack
                print(f"{B5} used {Ka}")
                pH -= B5A
                print(f"Your health dropped by {B5A}.")
            if turn == 'defend'.lower().strip():
                print(f"{B5} used {Ka}")
                print(defendT)
                pH -= B5A*.50
                print("Your health dropped by",B5A*defend,".")
            if turn == 'potion'.lower().strip():
                print(potionT)
                print(f"Your health recovered by {potion}")
                pH += potion
                print(f"{B5} used {Ka}")
                pH -= B5A
            if turn == 'poison'.lower().strip():
                print(poisonT)
                enemyH += poison
                print(f"{B5} used {Ka}")
                pH -= B5A
                print(f"Your health dropped by {B5A}")
while pH <= 0:
    gameOver=True
    print("You failed to save your tacos and now you will starve.")