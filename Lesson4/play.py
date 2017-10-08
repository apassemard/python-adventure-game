#this line is to import our story from the story.py file
import story
import monsters

#defining some colors
colors = {
   'blue' : '\033[96m',
   'red'  : '\033[91m',
   'yellow' : '\033[93m',
   'green' : '\033[92m',
   'end'  : '\033[0m'
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
# This function will handle fights
############################################################################
def enter_battle(the_room):
     print (colors['red']+"TO DO: "+colors['end']+"This is the function where we manage combat")

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
            list_of_choices = story.dungeon[player_location]['choices']
            player_choice = get_player_choice(list_of_choices)
            if player_choice != False:
                player_location = story.dungeon[player_location]['choices'][player_choice-1]['route_key']
        elif story.dungeon[player_location]['next_step'] == 'combat':
            print (colors['green']+"You enter combat with the ennemy!!"+colors['end'])
            #Calling the function that will handle the fight
            enter_battle(player_location)
            #once the fight is done we update the player location back to the room
            player_location = story.dungeon[player_location]['next_room']
