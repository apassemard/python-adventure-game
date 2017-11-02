# -*- coding: utf-8 -*-
#this line is to import our story from the story.py file
import story
import monsters
import math
import random
import time

#defining some colors
colors = {
   'blue' : '\033[96m',
   'red'  : '\033[91m',
   'yellow' : '\033[93m',
   'green' : '\033[92m',
   'end'  : '\033[0m',
   'bold' : '\033[1m',
   }

############################################################################
# Player card
############################################################################
player = {
   'card' : {
         'AC' : 16 ,
         'HP' : 10 ,
         'CON' : 16 ,
         'DEX' : 11 ,
         'STR' : 17 ,
         'damage_dice' : 1 ,
         'dice_rolls' : 6 ,
         'experience' : 0
    },
  }

############################################################################
# This function will determine if an input (some_string) is actually an integer
############################################################################
def IsItAnInteger(some_string):
    try:
        int(some_string)
        return True
    except ValueError:
        return False

############################################################################
# This function will look up which list of choices needs to be displayed
# to the player
############################################################################
def list_choices(location):
    if story.dungeon[location]['type'] == 'room': #if we are in a room
        if story.dungeon[location]['enemies']: #if there are enemies
            return story.dungeon[location]['choices_if_enemies']
        else: #if there is no enemy
            return story.dungeon[location]['choices_no_enemies']
    elif story.dungeon[location]['type'] == 'action': #if we are in an action
        room = story.dungeon[location]['room']
        if story.dungeon[room]['enemies']:
            #return the list for when there are enemies
            return story.dungeon[location]['choices_if_enemies']
        else: #if there is no enemy
            #return the list for when there are NO enemies
            return story.dungeon[location]['choices_no_enemies']

############################################################################
# This function will gather the user keyboard input and return the selection
############################################################################
def get_player_choice(all_choices):
    global keep_going
    input_error_message = colors['red']+"You have to enter the number corresponding to your choice.."+colors['end']
    #We need a variable to store choice numbers as we display the list
    #we start this at 1
    choice_number = 1
    #We display some text asking the player what they want to do
    print ("\nWhat would you like to do? : ")
    #then we go through all the choices in the list
    for each_choice in all_choices:
            #display the text for the choice
            print ("   "+str(choice_number)+": "+each_choice['text'])
            #add 1 to the choice number so each choice has a different value
            choice_number = choice_number + 1
    #Adding an extra choice every time, to allow the player to quit
    print ("   "+str(choice_number)+": Quit the game (you are too scared to stay here...)?")
    #when done displaying all choices one by one
    #prompt the player for an answer and store it in 'player_choice'
    player_choice = raw_input(colors['yellow']+"Make your choice: "+colors['end'])
    if IsItAnInteger(player_choice):
        player_choice = int(player_choice)
    else:
        print (input_error_message)
        return False
    #We need to check if the player chose to quit.
    #let's use a variable for clarity that will store the value of quit
    value_for_quit = choice_number
    if player_choice == value_for_quit: #choice_number stores the value of QUIT
        #a funny message for the quiter..
        print (colors['red']+"Chicken!! You do not deserve to be a hero!!"+colors['end'])
        keep_going = False
        #Return False to tell the main loop that no choice was made
        return False
    #IF the choice was not to Quit, we test if it's one of the others
    elif (player_choice >= 1 and player_choice < value_for_quit):
        #return the choice
        return player_choice
    else: #something other than any of the choices was entered
        #Return False to tell the main loop that no choice was made
        print (input_error_message)
        return False

############################################################################
# This function is doing a dice roll and applies modifiers
############################################################################
def roll_dice(number_of_dice, number_of_sides, adjustment):
    result = 0
    print("Dice roll: "+str(number_of_dice)+"D"+str(number_of_sides))
    for i in range (number_of_dice):
        #Rolling the dice as many times as needed!!
        roll = math.ceil(random.random() * number_of_sides)
        result = result + roll
    #if there is an adjustment
    if adjustment > 0:
        #Applying the adjustment
        result = result + adjustment
        #Displaying the result
        print("Result: "+str(int(roll))+" + adjustment of "+str(adjustment)+" = "+colors['bold']+str(int(result))+colors['end'])
    else: #if there is no adjustment the message is different
        print("Result with no adjustment: "+colors['bold']+str(int(result))+colors['end'])
    return int(result)

############################################################################
# This function will return the adjustment to apply to a given value
############################################################################
def adjustment(base_value):
    if base_value <= 3:
        return -3
    elif (base_value == 4 or base_value == 5):
        return -2
    elif (base_value >= 6 and base_value <= 8):
        return -1
    elif (base_value >= 9 and base_value <= 12):
        return 0
    elif (base_value >= 13 and base_value <= 15):
        return 1
    elif (base_value == 16 or base_value == 17):
        return 2
    elif base_value >= 18:
        return 3

############################################################################
# This function will determine the initiative scores of all fighters
# and return a sorted list
############################################################################
def initiative(enemies):
    ############### SECTION 1 ###################################
    #Initialize a list of fighters
    fighter_list = list()
    #Looking at enemies' data first
    for enemy in enemies: #for each of them
        #print a little message to tell who we are throwing dices for
        print (colors['yellow']+"Initiative for: "+str(enemy)+colors['end'])
        #Copy the characteristic card of the ennemy
        monster_data = monsters.bestiary[enemy]['card'].copy()
        #Add a 'turn' key to distinguish players from enemies
        monster_data['turn'] = enemy
        #Get the dice adjustment based on the Dexterity
        dexterity_adjustment = adjustment(monster_data['DEX'])
        #Roll the dice a pass the adjustment
        initiative_score = roll_dice(1,20,dexterity_adjustment)
        #Add the characters AND the dice roll score in a 2D list
        data_with_initiative = [ monster_data , initiative_score ]
        #Finally add all the data about the character to the full list of fighters
        fighter_list.insert(0,data_with_initiative)
    ############### SECTION 2 ###################################
    #Looking at the player's data and do the same as for the enemies
    print (colors['blue']+"Initiative for Player"+colors['end'])
    player_data = player['card'].copy() #copy the dictionary
    player_data['turn'] = 'player' #Add a 'turn' key with value 'player'
    dexterity_adjustment = adjustment(player_data['DEX'])
    initiative_score = roll_dice(1,20,dexterity_adjustment)
    data_with_initiative = [ player_data , initiative_score ]
    #Add the data from the player in the full fighter list
    fighter_list.insert(0,data_with_initiative)
    #All we need to do is sort the list in the order of initiative throws
    list.sort(fighter_list, key=lambda x: x[1], reverse = True)
    ############### SECTION 3 ###################################
    #we now want to indicate the player when his or her turn is
    #for that we need to find where the player is in the list
    #Initialize the player's position to a value that is not possible like -1
    player_position = -1
    #Initialize the position tracker we will use to find where the player is
    #starting at 0 which is the first position in the list
    position_tracker = 0
    #Go through each character of the fighter_list
    for character in fighter_list:
        #if the character is the player
        if character[0]['turn'] == 'player':
            #update the player_position, adding 1 because 0 in the
            #list means first to strike
            player_position = position_tracker + 1
            break #stop the loop. We don't need to go further
        else:
            #if it's not the player, we move the tracker to the next position
            position_tracker = position_tracker + 1
    ############### SECTION 4 ###################################
    if player_position == 1:
        print (colors['blue']+"Player hits first!!"+colors['end'])
    elif player_position == len(fighter_list):
        print (colors['red']+"Player hits LAST..."+colors['end'])
    else:
        print ("Player is turn "+str(player_position))
    return fighter_list

############################################################################
# This function will handle fights
############################################################################
def enter_battle(the_room):
   # We first get the list of enemies that are in the room
   enemy_list = list(story.dungeon[the_room]['enemies'])
   #we need to update that list with cards of each enemy
   enemy_list_with_data = list()
   for enemy in enemy_list:
       enemy_list_with_data.append(monsters.bestiary[enemy]['card'].copy())
   # We determine the order in which the characters will hit
   turn_list = initiative(enemy_list)
   # Keep looping until enemies are dead or player is dead
   #we initialize a couple variables to keep track of the status of the fighters
   player_alive = True
   enemies_alive = True
   enemy_assign = -1
   while player_alive and enemies_alive: #as long as both are alive keep going
        # For each character in the fight including the player
        print ("-----------------------------------------------")
        #Now going through each fighter's turn
        for turn in turn_list:
            #Initialize some values
            hit_sucess = False
            damage = 0
            ################# Section 1: PLayer's hitting #####################
            if turn[0]['turn'] == 'player':  #if it's the player's turn
                #assign an enemy to the player
                if turn_list[0][0]['turn'] != 'player':
                    enemy_assign = 0
                else:
                    enemy_assign = 1
                #a 20 is an automatic hitroll, 20 give critical damages
                strength_adjustment = adjustment(player['card']['STR'])
                hitroll = roll_dice(1,20,strength_adjustment)
                if hitroll == (20 + strength_adjustment):
                    print ("Critical damages")
                    damage = roll_dice(1,4,0)
                    hit_sucess = True
                #a 1 is an automatic miss
                elif hitroll == (1 + strength_adjustment):
                    print ("Fumble.. what a miss!")
                else:
                    if hitroll >= enemy_list_with_data[0]['AC']:
                        print("Hitroll ("+str(hitroll)+") is higher than the enemy's AC ("+str(enemy_list_with_data[0]['AC'])+")")
                        hit_sucess = True
                    else:  #if hitroll is not high enough
                        print ("You miss your shot.")
                if hit_sucess: #If successful deal the damages
                    #deal damages
                    damage = damage + roll_dice(player['card']['damage_dice'], player['card']['dice_rolls'], strength_adjustment)
                    print ("You do "+str(damage)+" damages to the enemy")
                    enemy_list_with_data[0]['HP'] = enemy_list_with_data[0]['HP'] - damage
                    if enemy_list_with_data[0]['HP'] <=0:    #if enemy is dead
                        print (colors['red']+"Enemy is dead"+colors['end'])
                        #record the experience points gained by the player
                        player['card']['experience'] = player['card']['experience'] + enemy_list_with_data[0]['xp']
                        #remove the enemy from all the lists we are using for this fight
                        del enemy_list[0]
                        del enemy_list_with_data[0]
                        del turn_list[enemy_assign]
                        #we check if there are any enemies left
                        if len(enemy_list) == 0:
                            print (colors['green']+"You have defeated all the enemies!"+colors['end'])
                            #we update the room of the dungeon:
                            story.dungeon[the_room]['enemies'] = [] #removing enemies from this room
                            story.dungeon[the_room]['next_step'] = 'choices' #not more fighting
                            story.dungeon[the_room]['next_room'] = the_room #will depend on the choices
                            enemies_alive = False #that will stop the fight
                            #break #let's stop right now. No need to continue
                    else:
                        print ("HP remaining: "+str(enemy_list_with_data[0]['HP']))
            ################# Section 2: Enemy's hitting #####################
            else: #it's an enemy's turn
                print("A "+colors['bold']+turn[0]['turn']+colors['end']+" tries to hit")
                strength_adjustment = adjustment(turn[0]['STR']) #finding out the strenght adjustment
                hitroll = roll_dice(1,20,strength_adjustment) #thorwing the dice for hitroll
                if hitroll == 20: #if hitroll is 20, critical hit
                    print ("Critical damages by the enemy! Ouch!!")
                    damage = roll_dice(1,4,0) #roll a dice with 4 sides, no adjustment
                    hit_sucess = True #successful hit
                elif hitroll == 1: #if hitroll is 1, automatic miss
                    print ("The "+turn[0]['turn']+" fumbles and misses!")
                else: #if not 20 nor 1, we need to check if the hitrool is successful by comparing to the AC
                    print ("checking if hitroll "+str(hitroll)+" is higher than your AC: "+str(player['card']['AC']))
                    if hitroll >= player['card']['AC']: #if hitroll is higher than the player's 'AC'
                        hit_sucess = True #successful hit
                if hit_sucess: #If successful deal the damages
                    #calculate the damages generates, taking into account the critical damages if there are any
                    damage = damage + roll_dice(turn[0]['damage_dice'], turn[0]['dice_rolls'], strength_adjustment)
                    print ("You receive "+colors['red']+str(damage)+colors['end']+" damages from the enemy")
                    player['card']['HP'] = player['card']['HP'] - damage #deal damage to the player
                    if player['card']['HP'] <= 0: #if the player is out of Health Point (inferior of equal to 0)
                        print (colors['red']+"You are dead.. Defeated by the enemy!"+colors['end'])
                        story.dungeon[the_room]['next_step'] = 'move' #not more fighting
                        story.dungeon[the_room]['next_room'] = 'death' #will depend on the choices
                        player_alive = False
                        break #that will stop the fight
                    else:
                        print ("HP remaining: "+str(player['card']['HP']))
                else: #if hitroll is not high enough
                    print ("The enemy misses.")
            time.sleep(2)

#Initialize where the player starts, which is 'intro'. We will create a variable
#to store that information an retrieve it when we need it.
player_location = 'intro'
#Initialize a variable that will tell the loop when to stop or keep going in
#the game. Let's call it "keep_going".
keep_going = True
#Start a 'while' loop that will say that as long as the variable stop is not
#false (meaning we will introduce a Loop (check out lesson 2 again if you need)
#that will go from room to room until keep_going becomes false.
while keep_going:
    #In the loop, we display the description for the room by looking into
    #the dictionary
    #Adding a separation between each piece of text
    print ("----------------------------------------------------------------")
    if story.dungeon[player_location]['type'] == 'room':
        if story.dungeon[player_location]['visited'] == 'no':
            #The room was never visited so we display the full description
            print (colors['blue']+story.dungeon[player_location]['desc']+colors['end'])
            #we also update the story to save that the player has visited the room
            story.dungeon[player_location]['visited'] = 'yes'
        else:
            #The player has visited this room already, do we display the short description
            print (colors['blue']+story.dungeon[player_location]['desc_visited']+colors['end'])
    elif story.dungeon[player_location]['type'] == 'action':
        print (colors['blue']+story.dungeon[player_location]['desc']+colors['end'])
    #If the next step is empty (we found two single quotes),
    if story.dungeon[player_location]['next_step'] == '':
        #we change the value of keep_going to False
        #the loop will stop
        keep_going = False
    #if 'next_step' is not empty
    else:
        #we need to check if next_step is 'move' or 'choices'
        if story.dungeon[player_location]['next_step'] == 'move':
            #we update the player location with the value of next_step
            player_location = story.dungeon[player_location]['next_room']
        elif story.dungeon[player_location]['next_step'] == 'choices':
            #call a function that will display the choices to the player
            #and return the choice
            list_of_choices = list_choices(player_location)
            player_choice = get_player_choice(list_of_choices)
            if player_choice != False:
                player_location = list_of_choices[player_choice-1]['route_key']
        elif story.dungeon[player_location]['next_step'] == 'combat':
            print (colors['green']+"You enter combat with the enemy!!"+colors['end'])
            #We need to check if the player is in a location that is not a room
            if story.dungeon[player_location]['type'] == 'action': #if that is the case
                    #the player_location is updated to the actual room the player is in
                    player_location = story.dungeon[player_location]['next_room']
            #Calling the function that will handle the fight
            enter_battle(player_location)
            #once the fight is done we update the player location back to the room
            player_location = story.dungeon[player_location]['next_room']
