print("""

 _   _  _         _      _                                  _____      _                    _ 
| \ | |(_)       | |    | |                                |_   _|    | |                  | |
|  \| | _   __ _ | |__  | |_  _ __ ___    __ _  _ __  ___    | |  ___ | |  __ _  _ __    __| |
| . ` || | / _` || '_ \ | __|| '_ ` _ \  / _` || '__|/ _ \   | | / __|| | / _` || '_ \  / _` |
| |\  || || (_| || | | || |_ | | | | | || (_| || |  |  __/  _| |_\__ \| || (_| || | | || (_| |
\_| \_/|_| \__, ||_| |_| \__||_| |_| |_| \__,_||_|   \___|  \___/|___/|_| \__,_||_| |_| \__,_|
            __/ |                                                                             
           |___/                                                                              

    """)
import time,random
###### final_A
def final_A():
    hit_A = ['perfect hit', 'you miss']
    current_hit = random.choice(hit_A)
    my_p_hit = 'perfect hit'
    if current_hit != my_p_hit:
        print(f'Oh noo, {current_hit} :(')
        time.sleep(5)
        print("You are attempting to flee, but it's too late.")
        time.sleep(6)
        print('Misfortune,the alligator ate you')
        time.sleep(7)
        game_over("You weren't strong enough\n And your bad luck killed you!")
    else:
        current_hit == my_p_hit
        print(f'VICTORY !! You had a {my_p_hit}')
        time.sleep(5)
        print("Will you attempt to flee when the alligator's teeth start to loosen up? (yes/no)")
        answer = input('>')
    if answer == 'yes':
        print('Oh noo!! Your escape is noticed by the Alligator.\n And he bite you even more fiercely')
        time.sleep(4)
        print('the Alligator was too smart for you, you died')
        time.sleep(5)
        game_over(' You died from blood loss, be smarter next time')
    else:
        answer == 'no'
        print('Wow, you manage to avoid getting eaten by the alligator. \n He thought you passed away !!')
        time.sleep(4)
        print('He no longer cared about you and let you go.')
        time.sleep(4)
        print('You were more intelligent than any other explorer, and the island was amazed by your good fortune and let you go.')
        time.sleep(6)
        print("""
           
   ____     __   ,-----.      ___    _             .-''-.     .-'''-.     _______      ____    .-------.     .-''-.   ______      
   \   \   /  /.'  .-,  '.  .'   |  | |          .'_ _   \   / _     \   /   __  \   .'  __ `. \  _(`)_ \  .'_ _   \ |    _ `''.  
    \  _. /  '/ ,-.|  \ _ \ |   .'  | |         / ( ` )   ' (`' )/`--'  | ,_/  \__) /   '  \  \| (_ o._)| / ( ` )   '| _ | ) _  \ 
     _( )_ .';  \  '_ /  | :.'  '_  | |        . (_ o _)  |(_ o _).   ,-./  )       |___|  /  ||  (_,_) /. (_ o _)  ||( ''_'  ) | 
 ___(_ o _)' |  _`,/ \ _/  |'   ( \.-.|        |  (_,_)___| (_,_). '. \  '_ '`)        _.-`   ||   '-.-' |  (_,_)___|| . (_) `. | 
|   |(_,_)'  : (  '\_/ \   ;' (`. _` /|        '  \   .---..---.  \  : > (_)  )  __ .'   _    ||   |     '  \   .---.|(_    ._) ' 
|   `-'  /    \ `"/  \  ) / | (_ (_) _)         \  `-'    /\    `-'  |(  .  .-'_/  )|  _( )_  ||   |      \  `-'    /|  (_.\.' /  
 \      /      '. \_/``".'   \ /  . \ /          \       /  \       /  `-'`-'     / \ (_ o _) //   )       \       / |       .'   
  `-..-'         '-----'      ``-'`-''            `'-..-'    `-...-'     `._____.'   '.(_,_).' `---'        `'-..-'  '-----'`     
                                                                                                                                  

            """)
###### alligator()
def alligator():
    time.sleep(4)
    print('The water tasted fantastic, but... \n You are suddenly pulled down to the pond')
    time.sleep(5)
    print('You must act quickly to avoid drowning!')
    time.sleep(4)
    print('Will you hit it randomly? (y/n)')
    answer = input('>')
    if answer == 'n':
        print('The island is disappointed')
        time.sleep(4)
        game_over('You are a coward.')
    else:
        answer =='y'
        print('Fighting is the way to go! Good luck !')
        time.sleep(4)
        final_A()

########anaconda_end()
def anaconda_end():
    print('You must provide the anaconda a number that is divisible by 7 \n If the number is correct, he will let you go.')
    time.sleep(8)
    print('You have no choice but to participate in his game because your knife is too short.')
    time.sleep(6)
    your_num = int(input('Pick a number that can be divisible by 7 to avoid being devoured.: '))
    if your_num%7 == 0 :
        print(f'{your_num} is divisible by 7')
        time.sleep(4)
        print('The island is greatly impressed by your intelligence, and the Anaconda decides to leave you alone despite its sadness. \n You escaped nightmare island')
        time.sleep(9)
        print("""
           
   ____     __   ,-----.      ___    _             .-''-.     .-'''-.     _______      ____    .-------.     .-''-.   ______      
   \   \   /  /.'  .-,  '.  .'   |  | |          .'_ _   \   / _     \   /   __  \   .'  __ `. \  _(`)_ \  .'_ _   \ |    _ `''.  
    \  _. /  '/ ,-.|  \ _ \ |   .'  | |         / ( ` )   ' (`' )/`--'  | ,_/  \__) /   '  \  \| (_ o._)| / ( ` )   '| _ | ) _  \ 
     _( )_ .';  \  '_ /  | :.'  '_  | |        . (_ o _)  |(_ o _).   ,-./  )       |___|  /  ||  (_,_) /. (_ o _)  ||( ''_'  ) | 
 ___(_ o _)' |  _`,/ \ _/  |'   ( \.-.|        |  (_,_)___| (_,_). '. \  '_ '`)        _.-`   ||   '-.-' |  (_,_)___|| . (_) `. | 
|   |(_,_)'  : (  '\_/ \   ;' (`. _` /|        '  \   .---..---.  \  : > (_)  )  __ .'   _    ||   |     '  \   .---.|(_    ._) ' 
|   `-'  /    \ `"/  \  ) / | (_ (_) _)         \  `-'    /\    `-'  |(  .  .-'_/  )|  _( )_  ||   |      \  `-'    /|  (_.\.' /  
 \      /      '. \_/``".'   \ /  . \ /          \       /  \       /  `-'`-'     / \ (_ o _) //   )       \       / |       .'   
  `-..-'         '-----'      ``-'`-''            `'-..-'    `-...-'     `._____.'   '.(_,_).' `---'        `'-..-'  '-----'`     
                                                                                                                                  

            """)
        time.sleep(5)

    else:
        print(f'{your_num} is not divisible by 7')
        time.sleep(4)
        print('The anaconda is savoring this opportunity to slowly and painfully devour you.')
        time.sleep(7)
        game_over('Your foolishness kills you')
    
###### anaconda()
def anaconda():
    time.sleep(3)
    print('The anaconda is staring at you. Will you attack or leave it alone?(leave/attack)')
    time.sleep(6)
    answer = input(">")
    if answer == "leave":
        print("You choose to leave it alone.")
        time.sleep(4)
        print("However, the moment you turn around, it attacks and devours you.")
        time.sleep(6)
        game_over('On this island, kind people never survive. \n You died because of your stupidity \n Never turn away from a predator. ')
        time.sleep(6)
    else:
        answer == "attack"
        print("\n You choose to attack! Good call ! You could have been eaten by the anaconda")
        time.sleep(6)
        anaconda_end()

    time.sleep(3)
######## final_S()
def final_S():
    print('Would you like to return the baby to his mother? (y/n)')
    answer = input('>')
    if answer == 'y':
            print(' You made the right decision because sharks are an animal that can forgive.\n your luck strike once again')
            time.sleep(5)
            print('You escaped nightmare island')
            print("""
           
   ____     __   ,-----.      ___    _             .-''-.     .-'''-.     _______      ____    .-------.     .-''-.   ______      
   \   \   /  /.'  .-,  '.  .'   |  | |          .'_ _   \   / _     \   /   __  \   .'  __ `. \  _(`)_ \  .'_ _   \ |    _ `''.  
    \  _. /  '/ ,-.|  \ _ \ |   .'  | |         / ( ` )   ' (`' )/`--'  | ,_/  \__) /   '  \  \| (_ o._)| / ( ` )   '| _ | ) _  \ 
     _( )_ .';  \  '_ /  | :.'  '_  | |        . (_ o _)  |(_ o _).   ,-./  )       |___|  /  ||  (_,_) /. (_ o _)  ||( ''_'  ) | 
 ___(_ o _)' |  _`,/ \ _/  |'   ( \.-.|        |  (_,_)___| (_,_). '. \  '_ '`)        _.-`   ||   '-.-' |  (_,_)___|| . (_) `. | 
|   |(_,_)'  : (  '\_/ \   ;' (`. _` /|        '  \   .---..---.  \  : > (_)  )  __ .'   _    ||   |     '  \   .---.|(_    ._) ' 
|   `-'  /    \ `"/  \  ) / | (_ (_) _)         \  `-'    /\    `-'  |(  .  .-'_/  )|  _( )_  ||   |      \  `-'    /|  (_.\.' /  
 \      /      '. \_/``".'   \ /  . \ /          \       /  \       /  `-'`-'     / \ (_ o _) //   )       \       / |       .'   
  `-..-'         '-----'      ``-'`-''            `'-..-'    `-...-'     `._____.'   '.(_,_).' `---'        `'-..-'  '-----'`     
                                                                                                                                  

            """)

    else:
        answer == 'n'
        print("The shark's mother summons other sharks, which immediately kills you")
        time.sleep(5)
        print('you had no chance of survival')
        time.sleep(3)
        game_over(" Your fate was sealed by taking the young sharks, your choice killed you.")
        time.sleep(3)

########sharks()
def sharks():
    time.sleep(3)
    print('The mother of the baby shark is after you! \n ? Would you like to distract it?(y/n) ')
    time.sleep(4)
    answer = input('>')
    if answer == 'n':
        print('Well played; the sharks are enraged and will not be misled.')
        time.sleep(4)
        final_S()
    else:
        answer == 'y'
        print('Oh noo!! The sharks were too enraged to be confused and succeed in catching you!')
        time.sleep(4)
        game_over("You have been eaten!")

######## boat

def boat():
    print('Well that ambitious \n The island is challenging your luck')
    time.sleep(3)
    print('It can randomly give you a perfect boat or a broken one')
    time.sleep(4)
    type_boat = ['broken', 'perfect']
    current_boat = random.choice(type_boat)
    my_boat = 'perfect'
    if current_boat != my_boat:
        print(f'Oh noo, the island gave you a {current_boat} boat \n good luck with that :(')
        time.sleep(5)
        print('You are trying to leave the island with the broken boat')
        time.sleep(6)
        print('Misfortune, in the middle of the ocean your boat sink and you are eaten by a great white sharks ')
        time.sleep(7)
        game_over("The island kept your soul \n You died because you run out of luck!")

    else:
        current_boat == my_boat
        print(f'VICTORY !! the island gave you a {my_boat} boat')
        time.sleep(5)
        print('In the middle of the ocean you realize that you are starving \n Would you like to go fishing? (yes/no)')
        answer = input('>')
        if answer == 'yes':
            print('Oh noo!! You catch a baby sharks')
            time.sleep(4)
            sharks()
        else:
            answer == 'no'
            print('Amazing, you avoid being eaten by the hidden sharks \n But unfortunately you are dying from starvation !!')
            time.sleep(4)
            game_over("You died from starvation!")
    
###### challenge()
def challenge():
    print("You begin gathering woods in the forest when you find a stunning pond.") 
    time.sleep(2)
    print('Do you wish to satisfy your thirst by drinking from the lovely pond? (yes/no)')
    answer = input('>')
    if answer == 'yes':
        print('You drank from the pond')
        alligator()
    else:
        answer == 'no'
        print('Amazing, you did not drink from the pond \n And you avoid getting dragged by the unseen alligator.')
        time.sleep(4)
        print("Even when you manage to flee the island's temptation \n You are DYING from dehydration")
        time.sleep(3)
        game_over("Life is indeed unfair :( \n You perished as a result of your resistance to the island's temptation! ")

###### explore_forest
def explore_forest():
    print('Your exploration led you to some fruit that you could devour.')
    time.sleep(2)
    print('Will you consume those fruits ? (y/n)')
    answer = input('>')
    if answer == 'y':
        print('Oh noo! Misfortune they were poisoned fruit')
        time.sleep(3)
        game_over("The island kept your soul \n You died because of your gluttony!")
    else:
        answer == 'n'
        print('Good call! you could have been poisoned')
        time.sleep(2)
        challenge()

######### raft()
def raft():
    type_raft = ['broken', 'sturdy']
    current_raft = random.choice(type_raft)
    my_raft = 'perfect'
    if current_raft != my_raft:
        print(f'Oh noo, the island gave you a {current_raft} sturdy \n good luck with that :(')
        time.sleep(5)
        print('You are trying to leave the island with the broken raft')
        time.sleep(6)
        print('Misfortune, in the middlle of the ocean your raft sink and you are eaten by a great white sharks ')
        time.sleep(7)
        game_over("The island kept your soul \n you died because you run out of luck!")
    else:
        current_raft == my_raft
        print(f'VICTORY !! the island gave you a {my_raft} raft')
        time.sleep(5)
        print('In the midlle of the ocean you realize that you are starving \n Would you like to go fishing? (yes/no)')
        answer = input('>')
        if answer == 'yes':
            print('Oh noo!! You catch a baby sharks')
            time.sleep(4)
            sharks()
        else:
            answer == 'no'
            print('Amazing, you avoid being eaten by the hidden sharks \n But you are dying from starvation !!')
            time.sleep(4)
            game_over("You died of starvation!")   
######### water
time.sleep(2)
def water():
    print(" You choose to flee the island by the water\n  Be careful, it may have been the right decision or your doom.")
    time.sleep(4)
    print('Would you like to try building a boat or a raft?(b/r)')
    answer = input(">")
    if answer == "b":
        print('You choose to make a boat')
        time.sleep(2)
        boat()
    else:
        answer =='r'
        print('You choose to make a raft')
        time.sleep(4)
        print('The island is testing your luck; it will either handed you randomly a solid raft or a broken raft.')
        time.sleep(5)
        raft()

######### forest
time.sleep(2)  
def forest():
    print('You chose to flee the island by the forest \n  Be careful, it may have been the right decision or your doom.')
    time.sleep(4)
    print('You can either explore the forest or make a weapon.(e/w)')
    answer = input(">")
    if answer == "e":
        print(" \n You choose to explore.")
        explore_forest()
    else:
        answer == "w"
        print("\n You choose to make a weapon!")
        time.sleep(2)
        print( '...You were too scared to explore the forest...')
        time.sleep(3)
        print('and decide to use what you have on hand to create a weapon')
        time.sleep(3)
        print(' ... and that was nothing :( ')
        time.sleep(3)
        print('You are forced to choose randomly whatever is on the ground from the plane crash.')
        time.sleep(5)
        print('But you still hope to find a good weapon like a knife ')
        time.sleep(6)
        weapon = ['knife', 'belt', 'perfum', 'pen']
        current_weapon = random.choice(weapon)
        my_weapon = 'knife' 
    while current_weapon != my_weapon:
        print(f'Ohh noo it is not the right weapon, lets try again, you randomly found {current_weapon}') 
        time.sleep(6)
        current_weapon = random.choice(weapon) 
    if current_weapon == my_weapon:
        print(f"VICTORY ! You have found your weapon! And it is a {my_weapon} ")
        time.sleep(5)
        print('Just as you reach for the weapon, an ANACONDA appears in front of you!')
        anaconda()

######## play_again()
def play_again():
  print("\n Do you want to play again? (y or n)")
  answer = input(">").lower()
  if "y" in answer:
    start()
  else:
    exit()
######## game_over()
def game_over(reason):
  print("\n" + reason)
  print("Game Over!")
  play_again()

######## start
time.sleep(1)
def start():    
    print( 'MAYDAY! MAYDAY! MAYDAY! WE ARE CRASHING' )
    time.sleep(4)
    print( 'HELP! HELP! HELP! ' )
    time.sleep(3)
    print('what... just happend...' )
    time.sleep(2)

    start_game = input('Would you like to start the game Nightmare Island? (Y/N) ')

    if start_game == 'n' or  start_game =='N':
        print("...Come on..don't be a chicken...")
        time.sleep(2)
        print('This will happen again until you consent to enter the island.... hihihi')
        time.sleep(4)
        start()

    else:
        start_game == 'y' or  start_game =='Y'
        time.sleep(2)
        print('Good luck!') 
        time.sleep(2)
        print('You are entering nightmare island')
        time.sleep(2)
        name = input("Enter you name adventurer :  ")
        print(f"\n Greetings {name} \n You have crashed on a deserted island and must either fight for your life or die in order to escape...")
        time.sleep(5)
        print('Your decisions matter, so make them wisely and thoughtfully.')
        time.sleep(5)
        print("You have just emerged from the collision, you are by yourself, and you have no one else.")
        time.sleep(4)
        print("You can attempt to leave the island by water or by the forest. (water/forest)")
  
    answer = input(">")
    if "water" in answer:
        water()
    elif answer == "forest":
        forest()
    else:
        game_over("Don't you know how to type something properly?")

start()