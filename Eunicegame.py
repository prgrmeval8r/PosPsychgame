#all imports should be at top of file
import sys
#import dictionary of story text
from all_text_dicts import *

import random
import time

jokes = ['\nQ: What did one wall say to the other wall? A: I\'ll meet you at the corner.\n',
        '\nQ: What gets wetter the more it dries? A: A towel.\n', 
        '\nQ: Why do you go to bed every night? A: Because the bed won\'t come to you!\n',
        '\nQ: Where do animals go when their tales fall off? A: A retail store.\n',
        '\nQ: Why can\'t you hear a pterodactyl going to the bathroom? A: Because the P is silent.\n',
        '\nQ: A magician was driving down the street, what went wrong? A: He turned into a driveway!\n',
        '\nQ: How do you make tissue dance? A: You put a little boogie in it!\n',
        '\nQ: What did the 0 say to the 8? A: Nice belt.\n',
        '\nQ: Who earns a living driving their customers away? A: Taxi drivers.\n',
        '\nQ: What bow can\'t be tied? A: A rainbow.\n',
        ]
gratitude = ['\nToday I am grateful for snuggling kittens, rollercoasters, chocolate. \nThinking of these things makes me smile.\n',
            '\nToday I am grateful for smiles from strangers, dragon gold, my job. \nThinking of these things I feel secure, positive.\n',
            '\nToday I am grateful for a first date, pizza, my faviorite show. \nThinking of these things I feel excited, comfortable, hopeful.\n',
            '\nToday I am grateful for hikes in the woods, new restuarant, upcoming vacation. \nThinking of these things I fell peaceful, excited.\n',
            '\nToday I am grateful for my health, sunsets, meditation. \nThinking of these things I feel calm, satisfied, lucky.\n',
            '\nToday I am grateful for picnics, loving family, silly jokes. \n Thinking of these things I feel supported, loved.\n',
            '\nToday I am grateful for new boots, shiny armour, next jousting competition. \nThinking of these things I feel fabulous.\n'
        ]
        
#http://www.ducksters.com/jokes/silly.php and others

#Saving Debug feature for when I figure out how I want to use it
DEBUG = False
if len(sys.argv) > 1:
    DEBUG = True  
#creates pause with time.s;eep
def countdown(count):
    while (count > 0):
        print (count)
        count -= 1
        time.sleep(1)
        
#create message function
#message takes two arguments, those arguments can change or even be different strings
def message(text, current_loc):
  print text
  if DEBUG:
    print "CURRENT LOCATION:", location

#this creates a simple prompt like in Zork
prompt = '>'
print descript['intro']

#Gift global variables

flute = 0
paper_bird = 0
butterfly_wing = 0
key = 0

#Non-gift global variables
reach = 0
happy_fruit = 1

#location variable is a context state. This starts game at 'front_yard'
location = 'front_yard'

#its better to specifically pass in the the variables you need in given function
#use message not print because print is *very* specific and 
    #we created message to have flexibility
    #we pass the same name for an argument below because its going to take 'front_yard' and print 'front_yard'
def look(loc_to_describ):
    message (descript[loc_to_describ], loc_to_describ)
    
def inventory(flute, paper_bird, butterfly_wing, key):
    if flute is 1:
        print 'Flute'
    if paper_bird >= 1:
        print 'Paper bird: ', paper_bird
    if butterfly_wing >= 1:
        print 'Butterfly wing: ', butterfly_wing
    if key is 1:
        print 'Front door key'
    

def process_front_yard(command, flute, key):
    l = 'front_yard'   
    if command in ['investigate garden', 'investigate yard', 'investigate front yard', 
                    'investigate plants', 'investigate lavender', 'investigate lavender bush',
                    'investigate rose', 'investigate rose bush']:
        l = 'front_yard'
        message (curiosity['garden'], l)
    elif command in ['clean trash', 'clean up trash', 'clean up', 'pick up trash', 'pick up',
                    'clean yard', 'clean garden', 'clean plants', 'clean']:
        l = 'front_yard2'
        message (descript['clean_yard'], l)
                #flute count     
        flute = 1
        print '\nFlute: ', flute    
    elif command in ['investigate flute']:
        if flute >= 1:
            l = 'front_yard'
            message (curiosity['flute'], l)
        else:
            l = 'front_yard'
            message ('\nWhat flute?', l)
    elif command in ['play flute', 'play flute again', 'use flute']:
        if flute >= 1:
            l = 'front_yard'
            message (curiosity['play_flute'], l)
        else:
            l = 'front_yard'
            message ('\nWhat flute?', l)
    elif command in ['read note', 'look at note', 'pick up note', 'take note', 'investigate note']:
        l = 'front_yard'
        message (descript['yard_note'], l)
    elif command in ['go inside', 'go in house', 'go in the house', 'go in', 'enter house', 
                    'open door', 'walk inside', 'walk inside house']:
        l = 'front_yard'
        message ('\nYou are too far from the house\n', l)
    elif command in ['read board', 'read paper', 'read papers', 'read notice', 'read notes',
                    'read notice board']:
        l = 'front_yard'
        message ('\nYou are too far to read any notes on any board\n', l)
    elif command in ['go to door', 'go to the door', 'walk to door', 'walk to the door',
                    'walk to front door', 'walk to the front door', 'walk toward front door',
                    'go to front door', 'go front door', 'go to the front door',
                    'walk closer to house', 'walk to house', 'walk toward house', 
                    'walk toward door', 'walk north', 'go north', 'north', 'n', 'go to porch', 
                    'go to the porch', 'walk to porch', 'walk to the porch']:
        if key is 1:
            l = 'front_door2'
            message('\n You walk up the swept staircase to the old but clean front porch\n', l)
        else:
            l = 'front_door'
            message ('\nYou walk to the front door, picking your way gingerly across the ' +
                 'rusted nails and broken glass.\n', l)  
    elif command in ['walk west', 'go west', 'west', 'w']:
        l = 'west_field'
        message ('\nYou walk into the dusty western field. \nThe land becomes hilly. ' +
                    '\nYou notice a dark object ahead but cant make out what it is.\n', l) 
    elif command in ['go east', 'walk east', 'east', 'e']:
        l = 'east_field'
        message ('\nThe grasses become taller as you walk east.\n', l)
    elif command in ['go south', 'walk south', 'south', 's']:
        l = 'south_field'
        message ('\nThe field stretches on and on before you.\n', l)
    else:
        message ('\nI do not know how to apply that word here.\n', l)
    return l, flute, key
 
 
def process_front_yard2(command, flute, key):
    l = 'front_yard2'   
    if command in ['investigate garden', 'investigate yard', 'investigate front yard', 
                    'investigate plants', 'investigate lavender', 'investigate lavender bush',
                    'investigate rose', 'investigate rose bush']:
        l = 'front_yard2'
        message (curiosity['garden2'], l)
    elif command in ['clean trash', 'clean up trash', 'clean up', 'pick up trash', 'clean yard', 'clean garden']:
        l = 'front_yard2'
        message (descript['clean_yard2'], l)
                #flute count     
        flute = 1
        print '\nFlute: ', flute    
    elif command in ['investigate flute']:
        if flute >= 1:
            l = 'front_yard'
            message (curiosity['flute'], l)
        else:
            l = 'front_yard'
            message ('\nWhat flute?\n', l)
    elif command in ['play flute', 'play flute again', 'use flute']:
        if flute >= 1:
            l = 'front_yard'
            message (curiosity['play_flute'], l)
        else:
            l = 'front_yard'
            message ('\nWhat flute?', l)
    elif command in ['investigate rosebush', 'investigate rose bush', 'investigate rose', 
                    'investigate bush']:
        l = 'front_yard2'
        message ('\nThe rosebush is busy making buds and doesn\'t have time to chat', l)
    elif command in ['read note', 'look at note', 'pick up note', 'take note', 'investigate note']:
        l = 'front_yard2'
        message (descript['yard_note'], l)
    elif command in ['go inside', 'go in house', 'go in the house', 'go in', 'enter house', 
                    'open door', 'walk inside', 'walk inside house']:
        l = 'front_yard2'
        message ('\nYou are too far from the house', l)
    elif command in ['read board', 'read paper', 'read papers', 'read notice', 'read notes',
                    'read notice board']:
        l = 'front_yard2'
        message ('\nYou are too far to read any notes on any board', l)
    elif command in ['go to door', 'go to the door', 'walk to door', 'walk to the door',
                    'walk to front door', 'walk to the front door', 'walk toward front door',
                    'go to front door', 'go front door', 'go to the front door',
                    'walk closer to house', 'walk to house', 'walk toward house', 
                    'walk toward door', 'walk north', 'go north', 'north', 'n', 'go to porch', 
                    'go to the porch', 'walk to porch', 'walk to the porch']:
        if key is 1:
            l = 'front_door2'
            message('\n You walk up the swept staircase to the old but clean front porch\n', l)
        else:
            l = 'front_door'
            message ('\nYou walk through the garden to the dirty, old front porch.\n', l)  
    elif command in ['walk west', 'go west', 'west', 'w']:
        l = 'west_field'
        message ('\nYou walk into the dusty western field. \nThe land becomes hilly. ' +
                    '\nYou notice a dark object ahead but cant make out what it is.\n', l) 
    elif command in ['go east', 'walk east', 'east', 'e']:
        l = 'east_field'
        message ('\nThe grasses become taller as you walk east.\n', l)
    elif command in ['go south', 'walk south', 'south', 's']:
        l = 'south_field'
        message ('\nThe field stretches on and on before you.\n', l)
    else:
        message ('\nI do not know how to apply that word here.\n', l)
    return l, flute, key
  

def process_east_field(command):
    l = 'east_field'
    if command in ['investigate field', 'investigate grasses', 'investigate grass']:
        l = 'east_field'
        message ('\nNot much here to investigate\n', l)
    elif command in ['go inside', 'go in house', 'go in the house', 'go in', 'enter house', 
                    'open door', 'walk inside', 'walk inside house', 'go to door', 
                    'go to the door', 'walk to door', 'walk to the door']:
        l = 'east_field'
        message ('\nYou are too far from the house\n', l)
    elif command in ['read board', 'read paper', 'read papers', 'read notice', 'read notes',
                    'read notice board', 'go to board', 'go to the board', 'go to the notice board', 
                    'walk to the board', 'walk to board', 'walk to notice board']:
        l = 'east_field'
        message ('\nYou do not see a notice board nearby\n', l)
    elif command in ['walk west', 'go west', 'west', 'w']:
        l = 'front_yard'
        message ('\nYou arrive at the yard in front of the house\n', l)             
    elif command in ['walk south', 'go south', 'south', 's']:
        l = 'south_field'
        message ('\nThe field stretches on and on before you.\n', l)
    elif command in ['walk north','go north', 'north', 'n']:
        l = 'north_field_east'
        message ('\nYou walk past the house through scraggly grasses. A dark wall is ahead of you\n', l)
    elif command in ['go east', 'walk east', 'east', 'e']:
        l = 'easteast_field'
        message ('\nThe ground becomes soggy and grasses become taller as you walk east.\n', l)
    else:
        message ('\nI do not know how to apply that word here.\n', l)
    return l
        
        
def process_easteast_field(command):
    l = 'easteast_field'
    if command in ['investigate mud', 'investigate plants', 'investigate flies', 
                    'investigate grasses', 'investigate shimmer', 'investigate grass'
                    'investigate shimmering', 'investigate drop', 'investigate water',
                    'investigate drops of water']:
        l = 'easteast_field'
        message ('\nNot much to see from here. The mud squelches. The flies buzz away.\n', l)
    elif command in ['go inside', 'go in house', 'go in the house', 'go in', 'enter house', 
                    'open door', 'walk inside', 'walk inside house', 'go to door', 
                    'go to the door', 'walk to door', 'walk to the door']:
        l = 'easteast_field'
        message ('\nYou are too far from the house\n', l)
    elif command in ['read board', 'read paper', 'read papers', 'read notice', 'read notes',
                    'read notice board', 'go to board', 'go to the board', 'go to the notice board', 
                    'walk to the board', 'walk to board', 'walk to notice board', 'investigate notice board']:
        l = 'easteast_field'
        message ('\nYou do not see a notice board nearby\n', l)
    elif command in ['walk west', 'go west', 'west', 'w']:
        l = 'east_field'
        message ('\nYou walk through tall grasses\n', l)             
    elif command in ['go north', 'walk north', 'north', 'n']:
        l = 'maze_entrance'
        message ('\nYou are standing at the corner of the huge rock wall.' 
                'To the left, the wall stretches on seemingly forever. You peer around the corner, '
                'and see a doorway in the rock just up ahead!\n', l)
    elif command in ['go south','walk south', 'south', 's']:
        l = 'south_field'
        message ('\nThe field stretches on and on before you.\n', l)
    elif command in ['go east', 'walk east', 'east', 'e']:
        l = 'quaking_bog'
        message ('\nYou wander into marshy lands. Small pools shimmer in the sun.\n', l)
    else:
        message ('I do not know how to apply that word here.\n', l)
    return l

def process_quaking_bog(command, butterfly_wing):
    l = 'quaking_bog'
    if command in ['go south', 'walk south', 'south', 's']:
        l = 'south_field'
        message ('\nThe field stretches on and on before you.\n', l)
    elif command in ['go east','walk east', 'walk east', 'east', 'e']:
        l = 'bog_heart'
        message ('\nYou walk past marshy lands toward the heart of the bog.\n', l)
    elif command in ['go north', 'walk north', 'north', 'n']:
        l = 'quaking_bog'
        message ('\nYou wander through the marshy land.\n', l)
    elif command in ['walk west', 'go west', 'west', 'w']:
        l = 'easteast_field'
        message ('\nGrasses become taller as you turn west away from the bog\n', l)
    elif command in ['investigate mud', 'investigate smell', 'investigate sulphur',
                    'investigate marsh', 'investigate moss', 'investigate grasses', 
                    'investigate pools']:
        l = 'quaking_bog'
        message (curiosity['bog'],l)
    elif command in['investigate croak', 'investigate sparkle']:
        l = 'quaking_bog'
        message ('\nYou are too far away to investigate\n', l)
    elif command in ['read board', 'read sign', 'read rules', 'investigate rules', 
                    'read Quaking Bog Rules and Regulations','read note', 'read rules', 
                    'read Quaking Bog Rules', 'investigate note', 'investigate sign']:
        l = 'quaking_bog'
        message (bog_text['bog_rules'], l)
    elif command in ['appreciate nature', 'appreciate bog', 'appreciate']:
        l = 'quaking_bog'
        print bog_text['bog_a0'],
        time.sleep(5)
        print bog_text['bog_a1'],
        time.sleep(7)
        print bog_text['bog_a2'],
        time.sleep(9)
        print bog_text['bog_a3'],
        time.sleep(10)
        print bog_text['bog_a4'],
        time.sleep(10)
        print bog_text['bog_a5']
        butterfly_wing = butterfly_wing + 1
        print 'Butterfly wings: ', butterfly_wing 
    elif command in ['investigate butterfly wind', 'investigate wing', 'investigate butterfly']:
        if butterfly_wing >= 1:
            l = 'quaking_bog'
            message (curiosity['butterfly_wing'], l)
        else:
            l = 'quaking_bog'
            message ('\nWhat butterfly wing?\n', l)
    elif command in ['eat butterfly wing', 'taste butterfly wing']:
        l = 'front_yard'
        message ('\nA butterfly wing is not a good snack for you.\n', l)
    else:
        message ('\nI do not know how to apply that word here.\n', l)
    return l, butterfly_wing

def process_bog_heart(command, butterfly_wing):
    l = 'bog_heart'
    if command in ['go south', 'walk south', 'south', 's']:
        l = 'south_field'
        message ('\nThe field stretches on and on before you.\n', l)
    elif command in ['tear moss', 'pull moss', 'move moss', 'tear at moss', 'pull at moss',
                    'cut moss' 'destroy moss', 'cut through moss']:
        l = 'bog_heart'
        message ('\nYou can not do that. It would hurt the moss.\n', l)
    elif command in ['go east','walk east', 'walk east', 'east', 'e', 'go north', 
                    'walk north', 'north', 'n', 'walk west', 'go west', 'west', 'w']:
        l = 'quaking_bog'
        message ('\nYou leave the heart of the bog.\n', l)
    elif command in ['investigate toad']:
        l = 'bog_heart'
        message (curiosity['toad'], l)
    elif command in ['give butterfly wing to toad', 'give toad butterfly wing', 'give butterfly wing',
                    'give toad butterfly', 'give butterfly', 'give wing', 'give toad butterfly wing',
                    'give wing to toad', 'give butterfly to toad', 'give toad wing', 'feed toad butterfly wing',
                    'give frog butterfly wing', 'give butterfly wing to frog', 'give butterfly to frog', 
                    'give wing to frog', 'give frog wing']:
        if butterfly_wing >= 1:
            l = 'bog_heart2'
            message (bog_text['bog_toad'], l)
            butterfly_wing = butterfly_wing - 1
            print 'Butterfly wings: ', butterfly_wing 
        else:
            l = 'bog_heart'
            message ('\nWhat butterfly wing?\n', l)    
    elif command in ['talk to toad', 'talk to frog', 'talk']:
        l = 'bog_heart'
        message ('\nThe toad is either asleep or pretending to sleep and does not reply.\n', l)
    elif command in ['reach deep', 'reach for key', 'search for key', 'search for key', 
                    'find key', 'find house key', 'look for key']:
        l = 'bog_heart'
        message ('\nYou look around but don\'t see anything resembling a key.\n', l)
    else:
        message ('\nI do not know how to apply that word here.\n', l)
    return l, butterfly_wing


def process_bog_heart2(command, butterfly_wing, reach, key):
    l = 'bog_heart2'
    if command in ['go south', 'walk south', 'south', 's']:
        l = 'south_field'
        message ('\nThe field stretches on and on before you.\n', l)
    elif command in ['tear moss', 'pull moss', 'move moss', 'tear at moss', 'pull at moss',
                    'cut moss' 'destroy moss', 'cut through moss']:
        l = 'bog_heart2'
        message ('\nYou can not do that. It would hurt the moss.\n', l)
    elif command in ['go east','walk east', 'walk east', 'east', 'e', 'go north', 
                    'walk north', 'north', 'n', 'walk west', 'go west', 'west', 'w']:
        l = 'quaking_bog'
        message ('\nYou leave the heart of the bog\n', l)
    elif command in ['give butterfly wing to toad', 'give toad butterfly wing', 'give butterfly wing',
                    'give toad butterfly', 'give butterfly', 'give wing', 'give toad butterfly wing',
                    'give wing to toad', 'give frog butterfly wing', 'give butterfly wing to frog', 
                    'give butterfly to frog','give wing to frog', 'give frog wing']:
        if butterfly_wing >= 1:
            l = 'bog_heart2'
            message (bog_text['bog_toad'], l)
            butterfly_wing = butterfly_wing - 1
            print 'Butterfly wings: ', butterfly_wing 
        else:
            l = 'bog_heart2'
            message ('\nWhat butterfly wing?\n', l)    
        print 'Butterfly wings: ', butterfly_wing 
    elif command in ['talk to toad','investigate toad', 'ask for riddle', 
                    'investigate riddle', 'what riddle', 'ask for riddle', 'answer riddle', 
                    'talk to frog']:
        l = 'bog_heart2'
        if key is 1:
            message(bog_text['toad_talk2'], l)
        else:
            message (bog_text['toad_talk0'], l)
    elif command in ['water', 'water, ice, steam', 'the answer is water', 'you are water']:
        l = 'bog_heart2'
        message(bog_text['toad_talk1'], l)
    elif command in ['reach deep', 'reach deep into bog', 'reach deep into the bog', 
                    'reach deep in bog', 'reach in bog', 'reach into bog', 'reach deeper',
                    'reach deeper into bog', 'reach deeper into the bog', 'reach further']:
        l = 'bog_heart2'
        if reach is 0:
            reach = reach + 1
            message(bog_text['bog_reach0'], l)
        elif reach is 1:
            reach = reach + 1
            message(bog_text['bog_reach1'], l)
        elif reach is 2:
            reach = reach + 1
            message(bog_text['bog_reach2'], l)
        elif reach is 3:
            reach = reach + 1
            key = 1
            message(bog_text['bog_reach3'], l)
        else:
            reach >= 4
            message('\nReaching further won\'t help you now\n', l)
    elif command in ['investigate key']:
        l = 'bog_heart2'
        message(curiosity['key'], l)
    else:
        message ('\nI do not know how to apply that word here.\n', l)
    return l, butterfly_wing, reach, key

def process_north_field_east(command):
    l = 'north_field_east'
    if command in ['investigate field', 'investigate grass']:
        l = 'north_field_east'
        message ('\nNot much here to investigate\n', l)
    elif command in ['investigate wall', 'investigate stone wall', 'investigate stone']:
        l = 'north_field_east'
        message (curiosity['wall'], l)
    elif command in ['go north', 'walk north', 'north', 'n']:
        l = 'north_field_east'
        message ('\nThe huge stone wall blocks your way further north\n', l)
    elif command in ['go east', 'walk east', 'east', 'e']:
        l = 'maze_entrance'
        message ('\nYou walk along the stone wall for what feels like forever.' +
        '\nTo the left, the wall stretches on seemingly forever. \nYou peer around the corner, ' +
        'and see an carved doorway in the rock wall just up ahead!\n', l)
    elif command in ['go south', 'walk south', 'south', 's']:
        l = 'east_field'
        message ('\nYou walk through tall grasses.\n', l) 
    elif command in ['walk west', 'go west', 'west', 'w']:
        l = 'north_field_east'
        message ('\nThe little house blocks the path. You cannot go this way.\n', l)
    else:
        message ('\nI do not know how to apply that word here.\n', l)
    return l

def process_north_field_west(command):
    l = 'north_field_west'
    if command in ['investigate field', 'investigate grass']:
        l = 'north_field_west'
        message ('\nNot much here to investigate\n', l)
    elif command in ['investigate wall', 'investigate stone wall', 'investigate stone']:
        l = 'north_field_west'
        message (curiosity['wall'], l)
    elif command in ['go north', 'walk north', 'north', 'n']:
        l = 'north_field_west'
        message ('\nThe huge stone wall blocks your way further north\n', l)
    elif command in ['go east', 'walk east', 'east', 'e']:
        l = 'north_field_west'
        message ('\nThe little house blocks the path. You cannot go this way.\n', l)
    elif command in ['go south', 'walk south', 'south', 's']:
        l = 'west_field'
        message ('\nYou walk through a dusty field\n', l) 
    elif command in ['walk west', 'go west', 'west', 'w']:
        l = 'north_field_west'
        message ('\nYou walk along the stone wall for what feels like forever.\n', l)
    elif command in ['go to doorway', 'walk to door', 'enter door', 'go in door', 
                    'go to door', 'enter', 'enter door', 'go in', 'go through door']:
        l = 'north_field_west'
        message ('\nThere is no doorway through the stone wall here.\n', l)
    else:
        message ('\nI do not know how to apply that word here.\n', l)
    return l

def process_maze_entrance(command):
    l = 'maze_entrance'
    if command in ['go west', 'walk west', 'west', 'w']:
        l = 'north_field_east'
        message ('\nYou wander through the quiet field.\n', l)
    elif command in ['go east', 'walk east', 'east', 'e']:
        l = 'maze_entrance'
        message ('\nYou arrive at the edge of a quaking bog and can go no further.\n', l)
    elif command in ['go south', 'walk south', 'south', 's']:
        l = 'easteast_field'
        message ('\nYou wander through the quiet field.\n', l)
    elif command in ['enter', 'enter maze', 'go in', 'go north', 'walk north', 'north', 'n']:
        l = 'maze_entrance'
        message (descript ['maze_begin'], l)
    else:
        message ('\nI do not know how to apply that word here.\n', l)
    return l
    
#def process_maze(command):
 #   l = 'maze'
  #  if command in ['b', 'B']:
   #     l = 'maze_entrance' 
    #    message (descript['maze_begin'], l)
    #elif command in ['f', 'F']:
     #   l = 'maze'
      #  message ('\nYou walk a few hesitant steps forward, and the passage goes left (l) or right (r)', l\n)
    #elif command in  ['r', 'R']:
     #   l = 'maze'
      #  message ('\nYou enter a passageway the narrows as you walk forward, until on your hands and knees you hit a dead-end', l\n)
    #else:
     #   message ('\nI do not know how to apply that word here. Only Forward (f), Backward (b), Left (l), or Right (r) work here', l\n)
    #return l
    
def process_west_field(command):
    l = 'west_field'
    if command in ['investigate board', 'investigate notice board']:
        l = 'west_field'
        message (curiosity['notice_board'], l)
    elif command in ['investigate field']:
        l = 'west_field'
        message ('\nNot much here to investigate.\n', l)
    elif command in ['go south', 'walk south', 'south', 's']:
        l = 'south_field'
        message ('\nThe field stretches on and on before you.\n', l)
    elif command in ['go north', 'walk north', 'north', 'n']:
        l = 'north_field_west'
        message ('\nYou walk past the house. A dark wall looms before you.\n', l)
    elif command in ['go west', 'walk west', 'west', 'w','go to notice board', 'walk to board']:
        l = 'notice_board'
        message ('\nYou progress further west through the dusty field of rocks and ' +
                'forgotten food wrappers. \nPlastic bags drift by in the breeze. ' +
                '\nYou stop walking when you reach an old public notice board.\n', l)
    elif command in ['go east', 'walk east', 'east', 'e']:
        l = 'front_yard'
        message ('\nYou arrive at the front yard of the house.\n', l)
    else:
        message ('\nI do not know how to apply that word here.\n', l)
#RULE: a function should always have a return. Even though it lets you not have one, ALWAYS have one
    return l
        
def process_notice_board(command, paper_bird):
    l = 'notice_board'
    if command in ['investigate notice board', 'investigate board', 'investigate notice']:
        l = 'notice_board'
        message (descript['notice_board'], l)
    elif command in ['read board', 'read the board', 'read notes', 'read the notes', 'read a note',
                    'read notice board', 'read the notice board', 'read notes on board', 
                    'read the notes on board', 'read note', 'read notice', 'read notices',
                    'investigate note', 'investigate notes', 'read first note']:
        l = 'notice_board'
        message (gratitude_notes['note1'], l)
    elif command in ['read another', 'read another note', 'read another gratitude',
                    'read another gratitude note', 'read a second page', 'read another page',
                    'read second note', 'investigate another', 'investigate another note']:
            l = 'notice_board'
            message (gratitude_notes['note2'], l) 
    elif command in ['write note', 'write a note', 'write gratitude note', 'write a gratitude note',
                    'write gratitude', 'add note', 'add a note', 'add a gratitude note', 
                    'post gratitude note', 'post note']:
        l = 'notice_board2'
        print '\nThree things I am grateful for today: \n',
        grat = raw_input(prompt)
        print '\nWhen I think of these things, I feel: \n',
        feelgrat = raw_input(prompt)
        print """ 
    Today, you feel grateful for %r. 
    
    Some emotions related to gratitude are %r.""" % (grat, feelgrat) 
        time.sleep(5)
        print gratitude_notes['note_bird'],
#paper count       
        paper_bird = paper_bird + 1
        time.sleep(5)
        print 'paper birds: ', paper_bird    
    elif command in ['investigate paper bird', 'investigate bird', 'investigate paper']:
        l = 'notice_board'
        if paper_bird >= 1:
            l = 'notice_board'
            message (curiosity['paper_bird'], l)
        else:
            l = 'notice_board'
            message ('\nWhat paper bird?\n', l)
    elif command in ['walk east', 'go east', 'east', 'e']:
        l = 'west_field'
        message ('\nYou are wandering through the dusty west field.\n', l)
    elif command in ['walk west', 'go west', 'west', 'w']:
        l = 'notice_board'
        message (gratitude_notes['end'], l)
    elif command in ['go south', 'walk south', 'south', 's']:
        l = 'south_field'
        message ('\nThe field stretches on and on before you.\n', l)
    elif command in ['go north', 'walk north', 'north', 'n']:
        l = 'north_field_west'
        message ('\nYou walk past the house. A dark wall looms before you.\n', l)
    else:
        message ('\nI do not know how to apply that word here.\n', l)
    return l, paper_bird
    
        
def process_notice_board2(command, paper_bird):
    l = 'notice_board2'
    if command in ['investigate notice board', 'investigate board', 'investigate notice']:
        l = 'notice_board2'
        message (descript['notice_board2'], l)
    elif command in ['read board', 'read the board', 'read notes', 'read the notes', 'read a note',
                    'read notice board', 'read the notice board', 'read notes on board', 
                    'read the notes on board', 'read note', 'read notice', 'read notices',
                    'investigate note', 'investigate notes', 'read another', 'read more',
                    'read another note']:
        l = 'notice_board2'
        print(random.choice(gratitude)) 
    elif command in ['write note', 'write a note', 'write gratitude note', 'write a gratitude note',
                    'write gratitude', 'add note', 'add a note', 'add a gratitude note', 
                    'post gratitude note', 'post note']:
        l = 'notice_board2'
        print '\nThree things I am grateful for today: \n',
        grat = raw_input(prompt)
        print '\nWhen I think of these things, I feel: \n',
        feelgrat = raw_input(prompt)
        print """ 
    Today, you feel grateful for %r. 
    
    Some emotions related to gratitude are %r.""" % (grat, feelgrat) 
        time.sleep(5)
        print gratitude_notes['note_bird'],
#paper count       
        paper_bird = paper_bird + 1
        time.sleep(5)
        print 'paper birds: ', paper_bird    
    elif command in ['investigate paper bird', 'investigate bird', 'investigate paper']:
        l = 'notice_board2'
        if paper_bird >= 1:
            l = 'notice_board2'
            message (curiosity['paper_bird'], l)
        else:
            l = 'notice_board2'
            message ('\nWhat paper bird?\n', l)
    elif command in ['walk east', 'go east', 'east', 'e']:
        l = 'west_field'
        message ('\nYou are wandering through the dusty west field.\n', l)
    elif command in ['walk west', 'go west', 'west', 'w']:
        l = 'notice_board2'
        message (gratitude_notes['end'], l)
    elif command in ['go south', 'walk south', 'south', 's']:
        l = 'south_field'
        message ('\nThe field stretches on and on before you.\n', l)
    elif command in ['go north', 'walk north', 'north', 'n']:
        l = 'north_field_west'
        message ('\nYou walk past the house. A dark wall looms before you.\n', l)
    else:
        message ('\nI do not know how to apply that word here.\n', l)
    return l, paper_bird

def process_south_field(command):
    l = 'south_field'   
    if command in ['investigate field', 'investigate south field']:
        l = 'south_field'
        message ('\nNot much here to investigate\n', l)
    elif command in ['go inside', 'go in house', 'go in the house', 'go in', 'enter house', 
                    'open door', 'walk inside', 'walk inside house']:
        l = 'south_field'
        message ('\nYou are too far from the house.\n', l)
    elif command in ['read board', 'read paper', 'read papers', 'read notice', 'read notes',
                    'read notice board', 'go to board', 'go to the board', 'go to the notice board', 
                    'walk to the board', 'walk to board', 'walk to notice board']:
        l = 'south_field'
        message ('\nYou do not see a notice board nearby.\n', l)
    elif command in ['walk towards board', 'walk west', 'go west', 'west', 'w']:
        l = 'west_field'
        message ('\nYou are wandering through the dusty west field.\n', l) 
    elif command in ['go to door', 'go to the door', 'walk to door', 'walk to the door']:
        l = 'south_field'
        message ('\nYou too far from the door.\n', l)
    elif command in ['walk north', 'go north', 'north', 'n']:
        l = 'front_yard'
        message ('\nYou arrive at the yard in front of the house.\n', l)             
    elif command in ['go south', 'walk south', 'south', 's']:
        l = 'southsouth_field'
        message ('\nAs you walk further, you come upon a towering apple tree\n', l)
    elif command in ['go east', 'walk east', 'east', 'e']:
        l = 'east_field'
        message ('\nThe ground becomes soggy and grasses become taller as you walk east.\n', l)
    else:
        message ('\nI do not know how to apply that word here.\n', l)
    return l


def process_southsouth_field(command, happy_fruit):
    l = 'southsouth_field'   
    if command in ['investigate field', 'investigate tree', 'investigate apple tree']:
        l = 'southsouth_field'
        message (curiosity['appletree'], l)
        if happy_fruit is 1:
            print '\nThere is one ripe apple shining in the bare tree.\n'
        else:
            print '\nThere are ripe apples shining in the bare tree.\n'
            print 'Apples: ', happy_fruit
    elif command in ['investigate apple', 'investigate fruit', 'investigate apples']:
        l = 'southsouth_field'
        message (curiosity['apple'], l)
        if happy_fruit > 1:
            print '\n Now there are more apples shining in the tree\n'
            print 'Apples: ', happy_fruit
    elif command in ['pick apple', 'pick fruit', 'take apple', 'take fruit', 'eat apple',
                    'eat fruit']:
        l = 'southsouth_field'
        message (curiosity['apple0'], l)
    elif command in ['yes', 'add fruit', 'add happy fruit', 'add fruit of happiness', 
                    'add a fruit', 'add apple', 'add an apple']:
        l = 'southsouth_field'
        print '\nWhat makes you happy? \n',
        happy = raw_input(prompt)
        print '\nWhat do you enjoy doing? \n',
        enjoy = raw_input(prompt)
        print """ 
    Today, your happiness fruits are %r, %r.""" % (happy, enjoy) 
        time.sleep(5)
        print curiosity['happy_tree']
        happy_fruit = happy_fruit + 1
        print 'Apples: ', happy_fruit
    elif command in ['no', 'refuse']:
        l = 'southsouth_field'
        message ('The song ends. You stand in the quiet field.', l)
    elif command in ['walk towards board', 'walk west', 'go west', 'west', 'w']:
        l = 'west_field'
        message ('\nYou are wandering through the dusty west field.\n', l) 
    elif command in ['walk north', 'go north', 'north', 'n']:
        l = 'south_field'
        message ('\nYou walk through the waving prairie grasses.\n', l)             
    elif command in ['go south', 'walk south', 'south', 's']:
        l = 'southsouth_field'
        message ('\nThe field stretches on and on before you.\n', l)
    elif command in ['go east', 'walk east', 'east', 'e']:
        l = 'east_field'
        message ('\nThe ground becomes soggy and grasses become taller as you walk east.\n', l)
    else:
        message ('\nI do not know how to apply that word here.\n', l)
    return l, happy_fruit

def process_front_door(command):
    l = 'front_door'
    if command in ['open mailbox', 'check mail', 'open the mailbox', 'check the mail', 
                    'open mail box', 'look in mailbox', 'look inside mailbox', 'investigate mailbox',
                    'investigate old mailbox', 'investigate mail box']:
        l = 'front_door'
        message (elf_speak['meet_elf'], l) 
    elif command in ['yell at elf', 'scream', 'scream at elf', 'give elf trash', 
                    'give elf some trash', 'give elf sock', 'give elf an old sock', 
                    'give elf sock', 'yell' 'screech', 'screech at elf', 'screech back',
                    'screech back at elf', 'scream back', 'yell back', 'growl']:
        l = 'front_door'
        message (elf_speak['elf_tongue'], l)
    elif command in ['give elf paper bird', 'give elf a paper bird', 'give elf paper',
                    'give paper bird to elf', 'give elf bird', 'give bird to elf', 
                    'give paper bird to elf', 'give bird', 'give elf butterfly wing', 'give elf a butterfly wing', 'give elf wing',
                    'give wing to elf', 'give butterfly', 'give elf butterfly', 
                    'give butterfly wing to elf','give a butterfly wing to elf', 
                    'give elf flute', 'give flute to elf']:
        l = 'front_door'
        message (elf_speak['no_gift'], l)
    elif command in ['investigate elf', 'talk to elf', 'speak to elf']:
        l = 'front_door'
        message (elf_speak['elf_talk0'], l)
    elif command in ['no', 'dont help', 'refuse', 'refuse to help']:
        l = 'front_yard'
        message (elf_speak['elf_refuse'], l)
    elif command in ['help', 'agree to help', 'yes', 'offer to help', 'help elf']:
        l = 'front_door2'
        print elf_speak['elf_talk1'],
        time.sleep(2)
        print '\nWhat strengths do you have? \n'
        time.sleep(2)
        expected = raw_input(prompt)
        print '\nHow do you feel thinking about your strengths? \n'
        expected = raw_input(prompt)
        print elf_speak['elf_talk2']    
    elif command in ['look at mat', 'look under welcome mat', 'look under mat', 
                    'investigate welcome mat', 'take mat', 'lift mat', 'move mat', 'investigate mat']:
        l = 'front_door'
        message ('\nYou peer under the dusty mat to find more dust and dirt.\n', l)
    elif command in ['pull up boards', 'pull up floor boards', 'look under boards', 
                    'look under floor boards', 'look under floor boards', 'investigate porch',
                    'investigate floorboards']:
        l = 'front_door'
        message ('\nYou hear some rodent-like sounds when you try to pull up the floor' +
                ' boards. \nThe floor boards will not move, probably just as well.\n', l)
    elif command in ['open door', 'open the door', 'go inside', 'go inside the house',
                    'go inside the house', 'investigate door', 'unlock door', 'use key']:
            l = 'front_door'
            message (elf_speak['elf_door'], l)
    elif command in ['go south', 'walk south', 'south', 's']:
        l = 'front_yard'
        message ('\nYou arrive in the yard in front of the house.\n', l)
    elif command in ['go north', 'walk north', 'north', 'n', 'go west', 'walk west', 'west',
                    'w', 'go east', 'walk east', 'east', 'e']:
        l = 'front_door'
        message ('\nYou can not go there from the porch.\n', l)
    else:
        message ('\nI do not know how to apply that word here.\n', l)
    return l  
    

def process_front_door2(command, key):
    l = 'front_door2'
    if command in ['open mailbox', 'check mail', 'open the mailbox', 'check the mail', 
                    'open mail box', 'look in mailbox', 'look inside mailbox', 'investigate mailbox',
                    'investigate elf', 'talk to elf', 'speak to elf', 'talk to elf more',
                    'talk to elf again', 'talk more']:
        l = 'front_door2'
        message (elf_speak['elf_talk3'], l) 
    elif command in ['yell at elf', 'scream', 'scream at elf', 'give elf trash', 
                    'give elf some trash', 'give elf sock', 'give elf an old sock', 
                    'give elf sock', 'yell' 'screech', 'screech at elf', 'screech back',
                    'screech back at elf', 'scream back', 'yell back', 'growl']:
        l = 'front_door2'
        message (elf_speak['elf_tongue'], l)
    elif command in ['give elf paper bird', 'give elf a paper bird', 'give elf paper',
                    'give paper bird to elf', 'give elf bird', 'give bird to elf', 
                    'give paper bird to elf', 'give bird', 'give elf butterfly wing', 'give elf a butterfly wing', 'give elf wing',
                    'give wing to elf', 'give butterfly', 'give elf butterfly', 
                    'give butterfly wing to elf','give a butterfly wing to elf', 
                    'give elf flute', 'give flute to elf']:
        l = 'front_door2'
        message (elf_speak['no_gift'], l)
    elif command in ['look at mat', 'look under welcome mat', 'look under mat', 
                    'investigate welcome mat', 'take mat', 'lift mat', 'move mat', 'investigate mat']:
        l = 'front_door'
        message ('\nYou peer under the dusty mat to find more dust and dirt.\n', l)
    elif command in ['pull up boards', 'pull up floor boards', 'look under boards', 
                    'look under floor boards', 'look under floor boards', 'investigate porch',
                    'investigate floorboards']:
        l = 'front_door'
        message ('\nYou hear some rodent-like sounds when you try to pull up the floor' +
                ' boards. \nThe floor boards will not move, probably just as well.\n', l)
    elif command in ['open door', 'open the door', 'go inside', 'go inside the house',
                    'go inside the house', 'investigate door', 'unlock door', 'use key']:
        if key is 1:
            l = 'inside_house'
            message (curiosity['open_door'], l)
        else:
            l = 'front_door'
            message (elf_speak['elf_door'], l)
    elif command in ['go south', 'walk south', 'south', 's']:
        l = 'front_yard'
        message ('\nYou arrive in the yard in front of the house.\n', l)
    elif command in ['go north', 'walk north', 'north', 'n', 'go west', 'walk west', 'west'
                    'w', 'go east', 'walk east', 'east', 'e']:
        l = 'front_door'
        message ('\nYou can not go there from the porch.\n', l)
    else:
        message ('\nI do not know how to apply that word here.\n', l)
    return l, key  
       
       
def process_inside_house(command):
    l = 'inside_house'
    if command in ['leave', 'go to door', 'go to porch', 'go outside', 'leave house', 'go south',
                    'walk south', 'south', 's']:
        l = 'front_door'
        message ('\nYou leave the house closing the door behind you.\n', l)
    elif command in ['go east', 'go west', 'walk east', 'walk west', 'east', 'west', 'e', 'w']:
        l = 'inside_house'
        message ('\nThe house is too small to go that way.\n', l)
    elif command in ['investigate troll']:
        l = 'inside_house'
        message (curiosity['troll1'], l)
    elif command in ['investigate trunk', 'investigate steamer trunk', 'investigate steamer']:
        l = 'inside_house'
        message (curiosity['trunk1'], l)
    elif command in ['read paper', 'read pamphlet', 'read piece of paper', 'pick up paper',
                    'take paper', 'grab paper', 'look at paper', 'take paper', 'look at paper',
                    'investigate paper']:
        l = 'inside_house'
        message (troll_speak['anxiety_info'], l)
    elif command in ['investigate table and chairs', 'investigate table', 'investigate chairs',
                    'investigate room', 'investigate chair', 'investigate room']:
        l = 'inside_house'
        message (curiosity['house'], l)
    elif command in ['talk', 'talk to troll', 'chat', 'chat with troll']:
        l = 'inside_house2'
        message (troll_speak['troll_talk'], l)
    elif command in ['tell joke', 'tell a joke', 'tell troll a joke', 'tell troll joke',
                    'tell joke to troll', 'tell another', 'joke', 'tell another joke'
                    'tell troll another joke']:
        l = 'inside_house2'
        message (troll_speak['troll_joke'], l)
        print (random.choice(jokes))
        print "\nThe troll's belly shakes and he makes a barking-burping noise. He is laughing!\n"
    elif command in ['take a deep breath', 'take deep breath', 'try a deep breath', 'breathe',
                    'try a deep breath', 'inhale slowly', 'slow down breathing','breathe slowly',
                    'try breathe deep with troll', 'suggest deep breathing to troll', 
                    'suggest deep breath', 'suggest troll breathes deeply',
                    'take deep breath with troll', 'take breath']:
        l = 'inside_house2'
        message (troll_speak['troll_breath'], l)  
        print '\nInhale deeply for'
        countdown(5)
        print ('\nExhale deeply for')
        countdown(5)
        print '\nYou both can feel a calm spreading through you.\n'
    else:
        message ('\nI do not know how to apply that word here.\n', l)
    return l
    
def process_inside_house2(command):
    l = 'inside_house2'
    if command in ['leave', 'go to door', 'go to porch', 'go outside', 'leave house', 'go south',
                    'walk south', 'south', 's']:
        l = 'front_door'
        message ('\nYou leave the house closing the door behind you.\n', l)
    elif command in ['investigate troll']:
        l = 'inside_house2'
        message (curiosity['troll2'], l)
    elif command in ['investigate trunk', 'investigate steamer trunk', 'investigate steamer']:
        l = 'inside_house2'
        message (curiosity['trunk2'], l)
    elif command in ['investigate writing', 'investigate lock', 'read writing']:
        l = 'inside_house2'
        message ('\nYou are too far away to learn more\n', l)
    elif command in ['go north', 'walk north', 'north', 'n', 'go closer to trunk',
                    'walk to trunk', 'go to trunk', 'move closer', 'go closer', 'closer']:
        l = 'trunk_closeup'
        message (curiosity['trunk3'], l)
    elif command in ['go east', 'go west', 'walk east', 'walk west', 'east', 'west', 'e', 'w']:
        l = 'inside_house2'
        message ('\nThe house is too small to go that way.\n', l)
    elif command in ['read paper', 'read pamphlet', 'read piece of paper', 'pick up paper',
                    'take paper', 'grab paper', 'look at paper', 'take paper', 'look at paper']:
        l = 'inside_house2'
        message (troll_speak['anxiety_info'], l)
    elif command in ['investigate table and chairs', 'investigate table', 'investigate chairs',
                    'investigate room', 'investigate chair', 'investigate room']:
        l = 'inside_house2'
        message (curiosity['house2'], l)
    elif command in ['talk', 'talk to troll', 'chat', 'chat with troll']:
        l = 'inside_house2'
        message (troll_speak['troll_talk'], l)
    elif command in ['tell joke', 'tell a joke', 'tell troll a joke', 'tell troll joke',
                    'tell joke to troll', 'tell another', 'joke', 'tell another joke',
                    'tell troll another joke']:
        l = 'inside_house2'
        message (troll_speak['troll_joke'], l)
        print (random.choice(jokes))
        print '\nThe troll\'s belly shakes and he makes a barking-burping noise. He is laughing!\n'
    elif command in ['take a deep breath', 'take deep breath', 'try a deep breath', 'breathe',
                    'try a deep breath', 'inhale slowly', 'slow down breathing','breathe slowly',
                    'try breathe deep with troll', 'suggest deep breathing to troll',
                    'suggest deep breath', 'suggest troll breathes deeply',
                    'take deep breath with troll', 'take breath']:
        l = 'inside_house2'
        message (troll_speak['troll_breath'], l)  
        print '\nInhale deeply for'
        countdown(5)
        print ('\nExhale deeply for')
        countdown(5)
        print '\nYou both can feel a calm spreading through you.\n'
    else:
        message ('\nI do not know how to apply that word here.\n', l)
    return l

def process_trunk_closeup(command, flute):
    l = 'trunk_closeup'
    if command in ['stand up', 'Stand up']:
        l = 'inside_house2'
        message ('\nYou stand up and look around the house.\n', l)
    elif command in ['investigate trunk', 'investigate lock', 'investigate strange lock',
                    'investigate words', 'read words', 'investigate inscription', 
                    'read inscription', 'investigate writing']:
        l = 'trunk_closeup'
        message (curiosity['trunk_closeup'], l)
    elif command in ['open trunk', 'open']:
        l = 'trunk_closeup'
        message ('\nYou cannot just open the trunk.\n', l)
    elif command in ['play flute', 'play music', 'play flute for snake']:
        if flute >= 1:
            l = 'trunk_closeup2'
            message (curiosity['trunk_open'], l)
        else:
            l = 'trunk_closeup'
            message ('\nFlute? What flute?\n', l)
    else:
        message ('\nI do not know how to apply that word here.\n', l)
    return l, flute


def process_trunk_closeup2(command, paper_bird):
    l = 'trunk_closeup2'
    if command in ['stand up', 'Stand up']:
        l = 'inside_house2'
        message ('\nYou stand up and look around the house.\n', l)
    elif command in ['investigate trunk', 'look in trunk', 'look inside trunk']:
        l = 'trunk_closeup2'
        message (curiosity['trunk_inside'], l)
    elif command in ['investigate egg']:
        l = 'trunk_closeup2'
        message (curiosity['egg'], l)
    elif command in ['open egg', 'break egg', 'smash egg', 'crack egg']:
        l = 'trunk_closeup2'
        message ('\nYou can\'t open the egg that way.\n', l)
    elif command in ['put paper bird on egg', 'put bird on egg', 'put paper bird in nest',
                    'put bird in nest', 'hatch egg with paper bird', 'hatch egg with bird',
                    'bird on egg']:
        l = 'trunk_closeup2'
        message (curiosity['trunk_inside2'], l)
        time.sleep(5)
        print curiosity['egg1'],
        time.sleep(5)
        print curiosity['egg2'],
        time.sleep(5)
        print curiosity['egg3'],
        time.sleep(5)
        print curiosity['egg4'],
        time.sleep(5)
        print curiosity['egg5'],
        time.sleep(5)
        print curiosity['egg6'],
        time.sleep(5)
        print descript['the_end'],
        time.sleep(5)
        print descript['the_end1']
        sys.exit()
    else:
        message ('\nI do not know how to apply that word here.\n', l)
    return l, paper_bird






#while True is True - forever loop
while True:
    command = raw_input(prompt)
#creating look command. 
    if command in ['look', 'look around']:
        look(location)
    elif command in ['inventory', 'check inventory']:
        inventory(flute, paper_bird, butterfly_wing, key)
    elif command in ['exit', 'quit']:
        break
    elif location == 'front_yard':
        (location, flute, key) = process_front_yard(command, flute, key)
    elif location == 'front_yard2':
        (location, flute, key) = process_front_yard2(command, flute, key)
    elif location == 'west_field':
        location = process_west_field(command)
    elif location == 'notice_board':
        (location, paper_bird) = process_notice_board(command, paper_bird)
    elif location == 'notice_board2':
        (location, paper_bird) = process_notice_board2(command, paper_bird)
    elif location == 'east_field':
        location = process_east_field(command)
    elif location == 'easteast_field':
        location = process_easteast_field(command)
    elif location == 'quaking_bog':
        (location, butterfly_wing) = process_quaking_bog(command, butterfly_wing)
    elif location == 'bog_heart':
        (location, butterfly_wing) = process_bog_heart(command, butterfly_wing)
    elif location == 'bog_heart2':
        (location, butterfly_wing, reach, key) = process_bog_heart2(command, butterfly_wing, reach, key)
    elif location == 'south_field':
        location = process_south_field(command)
    elif location == 'southsouth_field':
        (location, happy_fruit) = process_southsouth_field(command, happy_fruit)
    elif location == 'north_field_west':
        location = process_north_field_west(command)
    elif location == 'north_field_east':
        location = process_north_field_east(command)
    elif location == 'maze_entrance':
        location = process_maze_entrance(command)
    #elif location == 'maze':
     #   location = process_maze(command)
    elif location == 'front_door':
        (location) = process_front_door(command)
    elif location == 'front_door2':
        (location, key) = process_front_door2(command, key)
    elif location == 'inside_house':
        location = process_inside_house(command)
    elif location == 'inside_house2':
        location = process_inside_house2(command)
    elif location == 'trunk_closeup':
        (location, flute) = process_trunk_closeup(command, flute)
    elif location == 'trunk_closeup2':
        (location, paper_bird) = process_trunk_closeup2(command, paper_bird)
    else:
        message ('\nWhere did you go?\n' + command, location) 







  




