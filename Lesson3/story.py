# -*- coding: utf-8 -*-
dungeon = {
  'intro' : {
   'desc' :
      "You explored some of the caves before, and you are trying to \
      \nfind a new one to venture into this time. \
      \nAfter finding a suitable cave, you pause to be sure you are\
      \nready. The caves are dark and dready like you remember \
      \nfrom the last time, so you pull out your lantern and light \
      \nthe wick using your tinkerbox. Then carefully, you step \
      \ninto the first \"room\"",
    'next_step' : 'move',
    'next_room' : 'room1'
  },
  'room1' : {
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
    'next_step' : 'choices',
    'next_move' : '',
   },
  'touch_statue_room1' : {
      'desc' : "With hesitation you get closer and touch the statue. \
           \nEven though you feel a little tingling in your finger,\
           \nnothing happens, no magic or anything special",
      'next_step' : 'move',
      'next_room' : 'room1'
  },
}
