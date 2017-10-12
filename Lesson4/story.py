# -*- coding: utf-8 -*-
dungeon = {
  'intro' : {
   'type' : 'room',
   'visited' : 'no',
   'desc' :
      "You explored some of the caves before, and you are trying to \
      \nfind a new one to venture into this time. \
      \nAfter finding a suitable cave, you pause to be sure you are\
      \nready. The caves are dark and dready like you remember \
      \nfrom the last time, so you pull out your lantern and light \
      \nthe wick using your tinkerbox. Then carefully, you step \
      \ninto the first \"room\"",
    'desc_visited' : "You are outside the cavern",
    'next_step' : 'move',
    'next_room' : 'room1'
  },
  'room1' : {
    'type' : 'room',
    'visited' : 'no',
    'desc' :
      "The room you stepped in is 50 feet square with 10 feet\
      \nwide exits in the west, north and east walls. \
      \nThe ceiling height is 15 feet tall but the exits are only\
      \n10 feet high.The walls and floors are made of rough rock.\
      \nThere are some cracks and crevice in the walls, all very small.\
      \nIn the center of the room is a stone statue of a woman in armor.",
    'choices' : [
       { 'route_key' : 'corridor_route_from_room1', 'text' : 'Take one of the corridors?' },
       { 'route_key' : 'touch_statue_room1','text' : 'Touch the statue?' },
       { 'route_key' : 'stop_and_listen_room1', 'text' : 'Stop and listen?' },
       { 'route_key' : 'search_room1', 'text' : 'Search the room?' },
       { 'route_key' : 'exit_the_dungeon', 'text' : 'Exit the dungeon?' },
     ],
    'desc_visited' : 'You are in the first room with the statue.',
    'next_step' : 'choices',
    'next_move' : '',
   },
  'touch_statue_room1' : {
      'type' : 'action',
      'desc' : "With hesitation you get closer and touch the statue. \
           \nEven though you feel a little tingling in your finger,\
           \nnothing happens, no magic or anything special",
      'next_step' : 'move',
      'next_room' : 'room1'
  },
  'stop_and_listen_room1' : {
     'type' : 'action',
     'desc' : "You hold your breadth to listen carefully and finally hear a \
     \nsqueaking noises coming from the east corridor. A bit scary..",
     'next_step' : 'move',
     'next_room' : 'room1',
   },
  'search_room1' : {
     'type' : 'action',
     'desc' : "You search the room carefully and find a small scarp of paper \
     \nin a small niche in one wall. Opening it you discover a note written \
     \nin common tongue\
     \n     RATS EAST!\
     \n     GOBLIN NORTH\
     \n     BEWARE WEST!!",
    'next_step' : 'move',
    'next_room' : 'room1',
  },
  'corridor_route_from_room1' : {
     'type' : 'action',
     'desc' : "From this room, you can go in many different directions:",
     'choices' : [
         { 'route_key' : 'west_corridor_from_room1', 'text' : 'Go into the West corridor?' } ,
         { 'route_key' : 'north_corridor_from_room1', 'text' : 'Go into the North corridor?' },
         { 'route_key' : 'east_corridor_from_room1', 'text' : 'Go into the East corridor?' },
         { 'route_key' : 'stay_room1', 'text' : 'Stay in the room?', }
     ],
    'next_step' : 'choices',
    'next_room' : '',
  },
  'west_corridor_from_room1' : {
     'type' : 'room',
     'visited' : 'no',
     'desc' : "The corridor goes 20' to the west and arrives in a small dark room. \
               \nThe room is empty except for a few small piles of reddish dust.",
     'desc_visited' : "You are in the West corridor from the first room",
     'choices' : [
             { 'route_key' : 'room2', 'text' : 'Go in the West room?' } ,
             { 'route_key' : 'turn_around_room1', 'text' : 'Go back to the first room?' },
     ],
     'next_step' : 'choices',
     'next_room' : '',
  },
  'north_corridor_from_room1' : {
     'type' : 'room',
     'visited' : 'no',
     'desc' : "The corridor goes 20' to the North then turns right. \
                 \nYou peek around the corner and notice the corridor keeps \
                 \ngoing east for another 20' and into a room.",
     'desc_visited' : "You are in the north corridor from the first room",
     'choices' : [
         { 'route_key' : 'room4', 'text' : 'Go into the room?' } ,
         { 'route_key' : 'go_to_room1_from_room4', 'text' : 'Turn around and go back to the first room quietly?' },
     ],
     'next_step' : 'choices',
     'next_room' : '',
  },
  'east_corridor_from_room1' : { #rats
     'type' : 'room',
     'visited' : 'no',
     'desc' : "The corridor goes 50' to the East and opens into a room.\
                 \nAs you approach the room, you hear more squeaks. You wisely \
                 \nshutter your lantern, leaving only a dim reddish glow, \
                 \nand peek into the room.",
     'desc_visited' : "You are in the East corridor",
     'choices' : [
         { 'route_key' : 'room3', 'text' : 'Go into the room?' } ,
         { 'route_key' : 'turn_around_room1', 'text' : 'Go back to the first room?' },
     ],
     'next_step' : 'choices',
     'next_room' : '',
  },
 'stay_room1' : {
     'type' : 'action',
     'desc' : "You decide to take more time to decide.\n",
     'next_step' : 'move',
     'next_room' : 'room1',
 },
 'turn_around_room1' : {
    'type' : 'action',
    'room_name' : 'west_corridor_from_room1',
    'desc' : "You decide to turn around and go back to the first room",
    'next_step' : 'move',
    'next_room' : 'room1',
 },
 'go_to_room1_from_room4' : {
    'type' : 'action',
    'desc' : "You decide to turn around and go back to the first room.",
    'next_step' : 'move',
    'next_room' : 'room1',
 },
 'room2' : {
    'type' : 'room',
    'visited' : 'no',
    'desc' : "You go into the room and look around. There is nothing here\
            \nbut reddish dust. When you look closely at the dust however, you realize \
            \nit's rust!\
            \n\
            \nYou hear a snort, and when you look up, you see a strange looking \
            \ncreature coming into the room from the west corridor. It looks like a \
            \nlong armadillo with a long tail, and has 2 feathery feelers on the front.\
            \nIt charges at you angrily!",
    'desc_visited' : "You are in the Rust monster room",
    'choices' : [
         { 'route_key' : 'talk_to_rust_monster_room2', 'text' : 'Talk to the monster?'  } ,
         { 'route_key' : 'run_away_room2', 'text' : 'Run for your life!?'  } ,
         { 'route_key' : 'attack_room2', 'text' : 'Fight!?'  },
     ],
    'ennemies' : [ 'rust_monster' ],
    'next_step' : 'choices',
    'next_room' : '',
 },
 'talk_to_rust_monster_room2' : {
    'type' : 'action',
    'desc' : "Talking to the creature doesn't do any good. You have to fight it!",
    'next_step' : 'combat',
    'next_room' : 'room2',
 },
 'run_away_room2' : {
    'type' : 'action',
    'desc' : "As you turn around to run away, the monster quickly attacks, and gets\
            \nin your way. You cannot retreat!",
    'next_step' : 'combat',
    'next_room' : 'room2',
 },
 'attack_room2' : {
    'type' : 'action',
    'desc' : "You draw your sword and jump on the monster!",
    'next_step' : 'combat',
    'next_room' : 'room2',
 },
 #Rats Room and Actions in the East corridor
    'east_corridor_from_room1' : { #To the rats
        'type' : 'room',
        'visited' : 'no',
        'desc' : "The corridor goes 50' to the East and opens into a room.\
                \nAs you approach the room, you hear more squeaks. You wisely shutter your lantern, leaving \
                \nonly a dim reddish glow, and peek into the room.",
        'desc_visited' : "You are in the East corridor",
        'choices' : [
             { 'route_key' : 'room3', 'text' : 'Go into the room?'  } ,
             { 'route_key' : 'turn_around_room1', 'text' : 'Go back to the first room?'  },
         ],
         'next_step' : 'choices',
         'next_room' : '',
    },
    'room3' : { #The rats room
        'type' : 'room',
        'visited' : 'no',
        'desc' : "You quietly enter the room, and you don't see anything. But as you step into the room,\
                \nsome giant rats leap out from the corner to your right and attack!\
                \nYou are suddenly in battle, and cannot escape.",
        'desc_visited' : "You are in the Rats room.",
        'ennemies' : [ 'rat', 'rat', 'rat' ],
        'next_step' : 'combat',
        'next_room' : 'room3',
    },
    'go_back_from_room3' : {
        'type' : 'action',
        'desc' : "You decide the squeaking are not a good sign and turn around quietly\
                \nThe things that are making the noises don't notice..",
        'next_step' : 'move',
        'next_room' : 'room1',
    },
    'go_to_room1_from_room3' : {
        'type' : 'action',
        'desc' : "You go back to the first room",
        'next_step' : 'move',
        'next_room' : 'room1',
    },
    'take_corridor_from_room3' : { #### TODO To add path to the other room
        'type' : 'action',
        'desc' : "[TODO - NOT CODED YET] - You go back to the first room ",
        'next_step' : 'move',
        'next_room' : 'room3',
    },
#Goblin Room and Actions in the North corridor
    'north_corridor_from_room1' : {  #to the globlins
        'type' : 'room',
        'visited' : 'no',
        'desc' : "The corridor goes 20' to the North then turns right. \
                \nYou peek around the corner and notice the corridor keeps going east for another 20' and into a room.",
        'desc_visited' : "You are in the north corridor from the first room",
        'choices' : [
             { 'route_key' : 'room4', 'text' : 'Go into the room?'  } ,
             { 'route_key' : 'go_to_room1_from_room4', 'text' : 'Turn around and go back to the first room quietly?'  },
         ],
         'next_step' : 'choices',
         'next_room' : '',
    },
    'room4' : { #Goblin room
        'type' : 'room',
        'visited' : 'no',
        'desc' : "You may have had a clue of what is up here, you are careful keep your lantern shuttered and sneak up\
                \nto pick into the room. You hear soft talking in a language you do not understand.\
                \nPeeking around the corner, you see two Goblins to your right, at the south end of the room.\
                \nThey seem to be talking about something and don\'t notice you",
        'desc_visited' : "You are in the Goblins room",
        'choices' : [
             { 'route_key' : 'go_to_room1_from_room4', 'text' : 'Turn around and go back to the first room quietly?'  } ,
             { 'route_key' : 'talk_to_goblins_room4', 'text' : 'Talk to the Goblins?'  } ,
             { 'route_key' : 'attack_goblins_room4', 'text' : 'Attack the Goblins by surprise?'  } ,
         ],
         'ennemies' : [ 'goblin', 'goblin', 'goblin', 'goblin_captain' ],
         'next_step' : 'choices',
         'next_room' : '',
    },
    'take_north_corridor_from_room4' : {
        'type' : 'action',
        'room_name' : 'north_corridor_from_room4',
        'desc' : "[TODO - NOT CODED YET] - You go back to the first room ",
        'next_step' : 'move',
        'next_room' : 'room4',
    },
    'take_east_corridor_from_room4' : {
        'type' : 'action',
        'desc' : "[TODO - NOT CODED YET] - You go back to the first room ",
        'next_step' : 'move',
        'next_room' : 'room4',
    },
    'go_to_room1_from_room4' : {
        'type' : 'action',
        'desc' : "You decide to turn around and go back to the first room.",
        'next_step' : 'move',
        'next_room' : 'room1',
    },
    'attack_goblins_room4' : {
        'type' : 'action',
        'desc' : "AS you jump on the 2 Goblins, they start yelling and 2 more show up\
                \nfrom the the North corridor. One of them looks stronger than the others!",
        'next_step' : 'combat',
        'next_room' : 'room4',
    },
    'talk_to_goblins_room4' : {
        'type' : 'action',
        'desc' : "You greet the Goblins in your own language, the Common Tongue. They look up, startled,\
                \nand one growls something in its own language. The other smiles at you, and says \"Why, hello there!\
                \nWhat can I do to help you?\" The growling Goblin start heading north, apparently going to leave the room.",
        'choices' : [
             { 'route_key' : 'keep_talk_goblins_room4', 'text' : 'Keep talking to the remaining Goblin?'  } ,
             { 'route_key' : 'attack_single_goblin_room4', 'text' : 'Attack the remaing Goblin?'  } ,
             { 'route_key' : 'leave_goblin_room1_from_room4', 'text' : 'Leave the room and go back to the first room?'  } ,
         ],
        'next_step' : 'choices',
        'next_room' : '',
    },
    'keep_talk_goblins_room4' : {
        'type' : 'action',
        'desc' : "You keep talking as the one Goblin leaves north and turns left. The other tries to \
                \nbe friendly but you can tell he doesn't like you. Suddenly, you see 3 more Goblins coming from the\
                \nnorth.",
        'choices' : [
             { 'route_key' : 'attack_all_goblins_room4', 'text' : 'Attack now?'  } ,
             { 'route_key' : 'run_away_from_room4', 'text' : 'Run away as fast as you can?'  } ,
             { 'route_key' : 'keep_talk_goblins_2_room4', 'text' : 'Keep talking to the Goblin?'  } ,
         ],
        'next_step' : 'choices',
        'next_room' : '',
    },
    'attack_single_goblin_room4' : {
        'type' : 'action',
        'desc' : "You decide to attack the Goblins before they go get more help. You leap out to block\
                \nthe second Goblin escape, and they both draw their swords and attack you in return. The shouting\
                \nseems to have attracted more though, and 2 other Goblins show up from the North corridor.\
                \nOne of them stronger than the others.",
        'next_step' : 'combat',
        'next_room' : 'room4',
    },
    'leave_goblin_room1_from_room4' : {
        'type' : 'action',
        'desc' : "You decide to leave the Goblins alone but as you try to leave, the Goblin you have been\
                \ntalking to draws his sword and attacks you. The other starts running north and escapes",
        'next_step' : 'choices',
        'next_room' : '',
        'choices' : [
            { 'route_key' : 'attack_all_goblins_room4', 'text' : 'Attack the Goblins?'  },
            { 'route_key' : 'run_away_from_room4', 'text' : 'Run away as fast as you can?'  },
            { 'route_key' : 'keep_talk_goblins_2_room4', 'text' : 'Keep talking to the Goblins?'  },
        ],
    },
    'attack_all_goblins_room4' : {
        'type' : 'action',
        'desc' : "You attack the Goblins. Your first swing misses and the Goblins misses you too.\
                \ntBut now you see the other Goblin come back with 2 more, swords drawn and yelling! One of them\
                \n is bigger than the others",
        'next_step' : 'combat',
        'next_room' : 'room4',
    },
    'run_away_from_room4' : {
        'type' : 'action',
        'desc' : "You try to run away but one of the Goblin hits you in the back, inflicting 2 points\
                \nof damages to you. You run back through the corridor and out of the first room, toward the sun\
                \nlight. You are safe here.\
                \nA group of Goblins follows you to the entrance with their swords drawn and yelling.\
                \nAfter a while they retreat inside, and the one you talked to yell: \"Don't come back here Human!\"\
                \nor we will kill you!\
                \nThis is the end of your adventure.",
        'next_step' : 'the_end',
        'next_room' : '',
    },
    'keep_talk_goblins_2_room4' : {
        'type' : 'action',
        'desc' : "As you keep talking to the Goblin. You see 3 more coming from the north, and they\
                \nlook mad! One of them is bigger than the others",
        'next_step' : 'choices',
        'next_room' : '',
        'choices' : [
            { 'route_key' : 'attack_all_goblins_room4', 'text' : 'Attack the Goblins?'  },
            { 'route_key' : 'run_away_from_room4', 'text' : 'Run away as fast as you can?' },
        ],
    },
    'attack_all_goblins_room4' : {
        'type' : 'action',
        'room_name' : 'room4',
        'desc' : "You attack the Goblins.",
        'next_step' : 'combat',
        'next_room' : 'room4',
    },
    'the_end' : {
        'type' : 'room',
        'visited' : 'no',
        'desc' : "Your adventure brought you excitments and experience\
                \nLet's look at what you earned",
        'desc_visited' : "",
        'next_step' : '',
        'next_room' : '',
    },
}
