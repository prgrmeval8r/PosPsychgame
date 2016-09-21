#all imports should be at top of file
import sys
#import dictionary of story text
from all_text_dicts import *

import random
import time

jokes = ['Q: What did one wall say to the other wall? A: I\'ll meet you at the corner.',
        'Q: What gets wetter the more it dries? A: A towel.', 
        'Q: Why do you go to bed every night? A: Because the bed won\'t come to you!',
        'Q: Where do animals go when their tales fall off? A: A retail store',
        'Q: Why can\'t you hear a pterodactyl going to the bathroom? A: Because the P is silent.',
        'Q: A magician was driving down the street, what went wrong? A: He turned into a driveway!',
        'Q: How do you make tissue dance? A: You put a little boogie in it!',
        'Q: What did the 0 say to the 8? A: Nice belt.',
        'Q: Who earns a living driving their customers away? A: Taxi drivers.',
        'Q: What bow can\'t be tied? A: A rainbow.',
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

#Global variable for gifts  
paper_bird = 0
butterfly_wing = 0

#location variable is a context state. This starts game at 'front_yard'
location = 'front_yard'

#its better to specifically pass in the the variables you need in given function
#use message not print because print is *very* specific and 
    #we created message to have flexibility
    #we pass the same name for an argument below because its going to take 'front_yard' and print 'front_yard'
def look(loc_to_describ):
    message (descript[loc_to_describ], loc_to_describ)

def process_front_yard(command, butterfly_wing):
    l = 'front_yard'   
    if command in ['inspect garden', 'inspect yard', 'inspect front yard', 'inspect plants']:
        l = 'front_yard'
        message (curiosity['garden'], l)
    elif command in ['clean trash', 'clean up trash', 'clean up', 'pick up trash', 'clean yard', 'clean garden']:
        l = 'front_yard2'
        message (descript['clean_yard'], l)
                #butterfly wing count     
        butterfly_wing = butterfly_wing + 1
        print 'Butterfly wings: ', butterfly_wing    
    elif command in ['inspect butterfly wind', 'inspect wing']:
        if butterfly_wing >= 1:
            l = 'front_yard'
            message (curiosity['butterfly_wing'], l)
        else:
            l = 'front_yard'
            message ('What butterfly wing?', l)
    elif command in ['eat butterfly wind', 'taste butterfly wing']:
        l = 'front_yard'
        message ('No, a butterfly wing is not a good snack for you.', l)
    elif command in ['read note', 'look at note', 'pick up note', 'take note', 'inspect note']:
        l = 'front_yard'
        message (descript['yard_note'], l)
    elif command in ['go inside', 'go in house', 'go in the house', 'go in', 'enter house', 
                    'open door', 'walk inside', 'walk inside house']:
        l = 'front_yard'
        message ('You are too far from the house', l)
    elif command in ['read board', 'read paper', 'read papers', 'read notice', 'read notes',
                    'read notice board']:
        l = 'front_yard'
        message ('You are too far to read any notes on any board', l)
    elif command in ['go to door', 'go to the door', 'walk to door', 'walk to the door',
                    'walk to front door', 'walk to the front door', 'walk toward front door',
                    'go to front door', 'go front door', 'go to the front door',
                    'walk closer to house', 'walk to house', 'walk toward house', 
                    'walk toward door', 'walk north', 'go north', 'north', 'n', 'go to porch', 
                    'go to the porch', 'walk to porch', 'walk to the porch']:
        l = 'front_door'
        message ('You walk to the front door, picking your way gingerly across the ' +
                 'rusted nails and broken glass.', l)  
    elif command in ['walk west', 'go west', 'west', 'w']:
        l = 'west_field'
        message ('You walk into the dusty western field. The land becomes hilly, and ' +
                    'you notice a dark object ahead but cant make out what it is.', l) 
    elif command in ['go east', 'walk east', 'east', 'e']:
        l = 'east_field'
        message ('The grasses become taller as you walk east.', l)
    elif command in ['go south', 'walk south', 'south', 's']:
        l = 'south_field'
        message ('The field stretches on and on before you.', l)
    else:
        message ('I do not know how to apply that word here', l)
    return l, butterfly_wing
 
 
def process_front_yard2(command, butterfly_wing):
    l = 'front_yard2'   
    if command in ['inspect garden', 'inspect yard', 'inspect front yard', 'inspect plants']:
        l = 'front_yard2'
        message (curiosity['garden2'], l)
    elif command in ['clean trash', 'clean up trash', 'clean up', 'pick up trash', 'clean yard', 'clean garden']:
        l = 'front_yard2'
        message (descript['clean_yard'], l)
                #butterfly wing count     
        butterfly_wing = butterfly_wing + 1
        print 'Butterfly wings: ', butterfly_wing    
    elif command in ['inspect butterfly wind', 'inspect wing']:
        if butterfly_wing >= 1:
            l = 'front_yard2'
            message (curiosity['butterfly_wing'], l)
        else:
            l = 'front_yard'
            message ('What butterfly wing?', l)
    elif command in ['eat butterfly wind', 'taste butterfly wing']:
        l = 'front_yard2'
        message ('No, a butterfly wing is not a good snack for you.', l)
    elif command in ['read note', 'look at note', 'pick up note', 'take note', 'inspect note']:
        l = 'front_yard2'
        message (descript['yard_note'], l)
    elif command in ['go inside', 'go in house', 'go in the house', 'go in', 'enter house', 
                    'open door', 'walk inside', 'walk inside house']:
        l = 'front_yard2'
        message ('You are too far from the house', l)
    elif command in ['read board', 'read paper', 'read papers', 'read notice', 'read notes',
                    'read notice board']:
        l = 'front_yard2'
        message ('You are too far to read any notes on any board', l)
    elif command in ['go to door', 'go to the door', 'walk to door', 'walk to the door',
                    'walk to front door', 'walk to the front door', 'walk toward front door',
                    'go to front door', 'go front door', 'go to the front door',
                    'walk closer to house', 'walk to house', 'walk toward house', 
                    'walk toward door', 'walk north', 'go north', 'north', 'n', 'go to porch', 
                    'go to the porch', 'walk to porch', 'walk to the porch']:
        l = 'front_door'
        message ('You walk to the front door, picking your way gingerly across the ' +
                 'rusted nails and broken glass.', l)  
    elif command in ['walk west', 'go west', 'west', 'w']:
        l = 'west_field'
        message ('You walk into the dusty western field. The land becomes hilly, and ' +
                    'you notice a dark object ahead but cant make out what it is.', l) 
    elif command in ['go east', 'walk east', 'east', 'e']:
        l = 'east_field'
        message ('The grasses become taller as you walk east.', l)
    elif command in ['go south', 'walk south', 'south', 's']:
        l = 'south_field'
        message ('The field stretches on and on before you.', l)
    else:
        message ('I do not know how to apply that word here', l)
    return l, butterfly_wing
  

def process_east_field(command):
    l = 'east_field'
    if command in ['inspect field', 'inspect grasses']:
        l = 'east_field'
        message ('Not much here to inspect', l)
    elif command in ['go inside', 'go in house', 'go in the house', 'go in', 'enter house', 
                    'open door', 'walk inside', 'walk inside house', 'go to door', 
                    'go to the door', 'walk to door', 'walk to the door']:
        l = 'east_field'
        message ('You are too far from the house', l)
    elif command in ['read board', 'read paper', 'read papers', 'read notice', 'read notes',
                    'read notice board', 'go to board', 'go to the board', 'go to the notice board', 
                    'walk to the board', 'walk to board', 'walk to notice board']:
        l = 'east_field'
        message ('You do not see a notice board nearby', l)
    elif command in ['walk west', 'go west', 'west', 'w']:
        l = 'front_yard'
        message ('You arrive at the yard in front of the house', l)             
    elif command in ['walk south', 'go south', 'south', 's']:
        l = 'south_field'
        message ('The field stretches on and on before you.', l)
    elif command in ['walk north','go north', 'north', 'n']:
        l = 'north_field_east'
        message ('You walk past the house through scraggly grasses. A dark wall is ahead of you', l)
    elif command in ['go east', 'walk east', 'east', 'e']:
        l = 'easteast_field'
        message ('The ground becomes soggy and grasses become taller as you walk east.', l)
    else:
        message ('I do not know how to apply that word here', l)
    return l
        
        
def process_easteast_field(command):
    l = 'easteast_field'
    if command in ['inspect mud', 'inspect plants', 'inspect flies', 'inspect shimmer']:
        l = 'easteast_field'
        message ('Not much to see from here. The mud squelches. The flies buzz away.', l)
    elif command in ['go inside', 'go in house', 'go in the house', 'go in', 'enter house', 
                    'open door', 'walk inside', 'walk inside house', 'go to door', 
                    'go to the door', 'walk to door', 'walk to the door']:
        l = 'easteast_field'
        message ('You are too far from the house', l)
    elif command in ['read board', 'read paper', 'read papers', 'read notice', 'read notes',
                    'read notice board', 'go to board', 'go to the board', 'go to the notice board', 
                    'walk to the board', 'walk to board', 'walk to notice board', 'inspect notice board']:
        l = 'easteast_field'
        message ('You do not see a notice board nearby', l)
    elif command in ['walk west', 'go west', 'west', 'w']:
        l = 'east_field'
        message ('You walk through tall grasses', l)             
    elif command in ['go north', 'walk north', 'north', 'n']:
        l = 'maze_entrance'
        message ('You are standing at the corner of the huge rock wall.' 
                'To the left, the wall stretches on seemingly forever. You peer around the corner, '
                'and see a doorway in the rock just up ahead!', l)
    elif command in ['go south','walk south', 'south', 's']:
        l = 'south_field'
        message ('The field stretches on and on before you.', l)
    elif command in ['go east', 'walk east', 'east', 'e']:
        l = 'quaking_bog'
        message ('You wander into marshy lands. Something shines off to the east.', l)
    else:
        message ('I do not know how to apply that word here', l)
    return l

def process_quaking_bog(command, butterfly_wing):
    l = 'quaking_bog'
    if command in ['go south', 'walk south', 'south', 's']:
        l = 'south_field'
        message ('The field stretches on and on before you.', l)
    elif command in ['go east','walk east', 'walk east', 'east', 'e']:
        l = 'bog_heart'
        message ('You walk past marshy lands toward the watery east.', l)
    elif command in ['go north', 'walk north', 'north', 'n']:
        l = 'quaking_bog'
        message ('You wander through the marshy land.', l)
    elif command in ['walk west', 'go west', 'west', 'w']:
        l = 'easteast_field'
        message ('Grasses become taller as you turn west away from the bog', l)
    elif command in ['read board', 'read posting', 'read rules', 'inspect rules', 'read Park Rules and Regulations','read note', 'read park rules', 'read Park Rules']:
        l = 'quaking_bog'
        message (bog_text['bog_rules'], l)
    elif command in ['appreciate nature', 'appreciate bog', 'appreciate']:
        l = 'quaking_bog'
        print bog_text['bog_a0'],
        time.sleep(5)
        print bog_text['bog_a1'],
        time.sleep(5)
        print bog_text['bog_a2'],
        time.sleep(5)
        print bog_text['bog_a3'],
        time.sleep(5)
        print bog_text['bog_a4'],
        time.sleep(5)
        print bog_text['bog_a5']
        butterfly_wing = butterfly_wing + 1
        print 'Butterfly wings: ', butterfly_wing 
    elif command in ['inspect butterfly wind', 'inspect wing']:
        if butterfly_wing >= 1:
            l = 'quaking_bog'
            message (curiosity['butterfly_wing'], l)
        else:
            l = 'quaking_bog'
            message ('What butterfly wing?', l)
    else:
        message ('I do not know how to apply that word here', l)
    return l, butterfly_wing

def process_bog_heart(command, butterfly_wing):
    l = 'bog_heart'
    if command in ['go south', 'walk south', 'south', 's']:
        l = 'south_field'
        message ('The field stretches on and on before you.', l)
    elif command in ['tear moss', 'pull moss', 'move moss', 'tear at moss', 'pull at moss',
                    'cut moss' 'destroy moss', 'cut through moss']:
        l = 'bog_heart'
        message ('Of course you can not do that. It would hurt the moss.', l)
    elif command in ['go east','walk east', 'walk east', 'east', 'e', 'go north', 
                    'walk north', 'north', 'n', 'walk west', 'go west', 'west', 'w']:
        l = 'quaking_bog'
        message ('You leave the heart of the bog', l)
    elif command in ['inspect toad']:
        l = 'bog_heart'
        message (curiosity['toad'], l)
    elif command in ['give butterfly wing to toad', 'give toad butterfly wing']:
    #maybe this should go to bog_heart2, so that look can describe the toad as awake
    #and interested to talk!!!
        l = 'bog_heart2'
        message (bog_text['bog_toad'], l)
        butterfly_wing = butterfly_wing - 1
        print 'Butterfly wings: ', butterfly_wing 
    #talk to frog, and then he will tell you the correct with to use to get treasure
    #that is using the computer system to work appropriately as PART of the game!
    #negative self talk toad - http://www.depressiontoolkit.org/download/positive_self_talk_facts_umdc.pdf
    elif command in ['talk to toad']:
        l = 'bog_heart'
        message ('The toad is either asleep or pretending to sleep and does not reply.', l)
    else:
        message ('I do not know how to apply that word here', l)
    return l, butterfly_wing


def process_bog_heart2(command, butterfly_wing):
    l = 'bog_heart2'
    if command in ['go south', 'walk south', 'south', 's']:
        l = 'south_field'
        message ('The field stretches on and on before you.', l)
    elif command in ['tear moss', 'pull moss', 'move moss', 'tear at moss', 'pull at moss',
                    'cut moss' 'destroy moss', 'cut through moss']:
        l = 'bog_heart2'
        message ('Of course you can not do that. It would hurt the moss.', l)
    elif command in ['go east','walk east', 'walk east', 'east', 'e', 'go north', 
                    'walk north', 'north', 'n', 'walk west', 'go west', 'west', 'w']:
        l = 'quaking_bog'
        message ('You leave the heart of the bog', l)
    elif command in ['inspect toad']:
        l = 'bog_heart2'
        message (curiosity['toad'], l)
    elif command in ['give butterfly wing to toad', 'give toad butterfly wing']:
    #maybe this should go to bog_heart2, so that look can describe the toad as awake
    #and interested to talk!!!
        l = 'bog_heart2'
        message (bog_text['bog_toad'], l)
        butterfly_wing = butterfly_wing - 1
        print 'Butterfly wings: ', butterfly_wing 
    #talk to frog, and then he will tell you the correct way to use to get treasure through a riddle!
    #that is using the computer system to work appropriately as PART of the game!
    #negative self talk toad - http://www.depressiontoolkit.org/download/positive_self_talk_facts_umdc.pdf
    elif command in ['talk to toad']:
        l = 'bog_heart2'
        message (bog_text['toad_talk'], l)
    else:
        message ('I do not know how to apply that word here', l)
    return l, butterfly_wing

def process_north_field_east(command):
    l = 'north_field_east'
    if command in ['inspect field', 'inspect grass']:
        l = 'north_field_east'
        message ('Not much here to inspect', l)
    elif command in ['go north', 'walk north', 'north', 'n']:
        l = 'north_field_east'
        message ('The huge stone wall blocks your way further north', l)
    elif command in ['go east', 'walk east', 'east', 'e']:
        l = 'maze_entrance'
        message ('You walk along the stone wall for what feels like forever.' 
        'To the left, the wall stretches on seemingly forever. You peer around the corner, '
        'and see an carved doorway in the rock wall just up ahead!', l)
    elif command in ['go south', 'walk south', 'south', 's']:
        l = 'east_field'
        message ('You walk through tall grasses', l) 
    elif command in ['walk west', 'go west', 'west', 'w']:
        l = 'north_field_east'
        message ('The little house blocks the path. You cannot go this way', l)
    else:
        message ('I do not know how to apply that word here', l)
    return l

def process_north_field_west(command):
    l = 'north_field_west'
    if command in ['inspect field', 'inspect grass']:
        l = 'north_field_west'
        message ('Not much here to inspect', l)
    elif command in ['go north', 'walk north', 'north', 'n']:
        l = 'north_field_west'
        message ('The huge stone wall blocks your way further north', l)
    elif command in ['go east', 'walk east', 'east', 'e']:
        l = 'north_field_west'
        message ('The little house blocks the path. You cannot go this way', l)
    elif command in ['go south', 'walk south', 'south', 's']:
        l = 'west_field'
        message ('You walk through a dusty field', l) 
    elif command in ['walk west', 'go west', 'west', 'w']:
        l = 'north_field_west'
        message ('You walk along the stone wall for what feels like forever.', l)
    elif command in ['go to doorway', 'walk to door', 'enter door', 'go in door', 'go to door', 'enter', 'enter door', 'go in', 'go through door']:
        l = 'north_field_west'
        message ('There is no doorway through the stone wall here', l)
    else:
        message ('I do not know how to apply that word here', l)
    return l

def process_maze_entrance(command):
    l = 'maze_entrance'
    if command in ['go west', 'walk west', 'west', 'w']:
        l = 'north_field_east'
        message ('You wander through the quiet field', l)
    elif command in ['go east', 'walk east', 'east', 'e']:
        l = 'maze_entrance'
        message ('You arrive at the edge of a quaking bog and can go no further', l)
    elif command in ['go south', 'walk south', 'south', 's']:
        l = 'easteast_field'
        message ('You are in the east east field', l)
    elif command in ['enter', 'enter maze', 'go in']:
        l = 'maze'
        message (descript ['maze_begin'], l)
    else:
        message ('I do not know how to apply that word here.', l)
    return l
    
def process_maze(command):
    l = 'maze'
    if command in ['b', 'B']:
        l = 'maze_entrance' 
        message (descript['maze_begin'], l)
    elif command in ['f', 'F']:
        l = 'maze'
        message ('You walk a few hesitant steps forward, and the passage goes left (l) or right (r)', l)
    elif command in  ['r', 'R']:
        l = 'maze'
        message ('You enter a passageway the narrows as you walk forward, until on your hands and knees you hit a dead-end', l)
    else:
        message ('I do not know how to apply that word here. Only Forward (f), Backward (b), Left (l), or Right (r) work here', l)
    return l
    
def process_west_field(command):
    l = 'west_field'
    if command in ['inspect board', 'inspect notice board']:
        l = 'west_field'
        message (curiosity['notice_board'], l)
    elif command in ['inspect field']:
        l = 'west_field'
        message ('Not much here to inspect', l)
    elif command in ['go south', 'walk south', 'south', 's']:
        l = 'south_field'
        message ('The field stretches on and on before you.', l)
    elif command in ['go north', 'walk north', 'north', 'n']:
        l = 'north_field_west'
        message ('You walk past the house. A dark wall looms before you.',l)
    elif command in ['go west', 'walk west', 'west', 'w','go to notice board', 'walk to board']:
        l = 'notice_board'
        message ('You progress further west through the dusty field of rocks and ' +
                'forgotten food wrappers. Plastic bags drift by in the breeze. ' +
                'You stop walking when you reach an old public notice board.', l)
    elif command in ['go east', 'walk east', 'east', 'e']:
        l = 'front_yard'
        message ('You arrive at the front yard of the house.', l)
    else:
        message ('I do not know how to apply that word here', l)
#RULE: a function should always have a return. Even though it lets you not have one, ALWAYS have one
    return l
        
def process_notice_board(command, paper_bird):
    l = 'notice_board'
    if command in ['inspect notice board', 'inspect board', 'inspect notice']:
        l = 'notice_board'
        message (descript['notice_board'], l)
    elif command in ['read board', 'read the board', 'read notes', 'read the notes', 'read a note',
                    'read notice board', 'read the notice board', 'read notes on board', 
                    'read the notes on board', 'read note', 'read notice', 'read notices',
                    'inspect note', 'inspect notes']:
        l = 'notice_board'
        message (gratitude_notes['note1'], l)
    elif command in ['read another', 'read another note', 'read another gratitude',
                    'read another gratitude note', 'read a second page', 'read another page'
                    'inspect another', 'inspect another note']:
            l = 'notice_board'
            message (gratitude_notes['note2'], l) 
    elif command in ['write note', 'write a note', 'write gratitude note', 'write a gratitude note',
                    'write gratitude', 'add note', 'add a note', 'add a gratitude note', 
                    'post gratitude note', 'post note']:
        l = 'notice_board'
        print 'Three things I am grateful for today: ',
        grat = raw_input()
        print 'When I think of these things, I feel: ',
        feelgrat = raw_input()
        print """ 
    Today, you feel grateful for %r. 
    
    Some emotions related to gratitude are %r.""" % (grat, feelgrat) 
        time.sleep(5)
        print gratitude_notes['note_bird'],
#origami count       
        paper_bird = paper_bird + 1
        time.sleep(5)
        print 'Origami birds: ', paper_bird    
    elif command in ['walk east', 'go east', 'east', 'e']:
        l = 'west_field'
        message ('You are wandering through the dusty west field.', l)
    elif command in ['walk west', 'go west', 'west', 'w']:
        l = 'notice_board'
        message (gratitude_notes['end'], l)
    elif command in ['go south', 'walk south', 'south', 's']:
        l = 'south_field'
        message ('The field stretches on and on before you.', l)
    elif command in ['go north', 'walk north', 'north', 'n']:
        l = 'north_field_west'
        message ('You walk past the house. A dark wall looms before you.', l)
    else:
        message ('I do not know how to apply that word here', l)
    return l, paper_bird
    

def process_south_field(command):
    l = 'south_field'   
    if command in ['inspect field', 'inspect south field']:
        l = 'south_field'
        message ('Not much here to inspect', l)
    elif command in ['go inside', 'go in house', 'go in the house', 'go in', 'enter house', 
                    'open door', 'walk inside', 'walk inside house']:
        l = 'south_field'
        message ('You are too far from the house', l)
    elif command in ['read board', 'read paper', 'read papers', 'read notice', 'read notes',
                    'read notice board', 'go to board', 'go to the board', 'go to the notice board', 
                    'walk to the board', 'walk to board', 'walk to notice board']:
        l = 'south_field'
        message ('You do not see a notice board nearby', l)
    elif command in ['walk towards board', 'walk west', 'go west', 'west', 'w']:
        l = 'west_field'
        message ('You are wandering through the dusty west field.', l) 
    elif command in ['go to door', 'go to the door', 'walk to door', 'walk to the door']:
        l = 'south_field'
        message ('You too far from the door', l)
    elif command in ['walk north', 'go north', 'north', 'n']:
        l = 'front_yard'
        message ('You arrive at the yard in front of the house', l)             
    elif command in ['go south', 'walk south', 'south', 's']:
        l = 'south_field'
        message ('The field stretches on and on before you.', l)
    elif command in ['go east', 'walk east', 'east', 'e']:
        l = 'east_field'
        message ('The ground becomes soggy and grasses become taller as you walk east.', l)
    else:
        message ('I do not know how to apply that word here', l)
    return l

def process_front_door(command, paper_bird):
    l = 'front_door'
    if command in ['open mailbox', 'check mail', 'open the mailbox', 'check the mail', 
                    'open mail box', 'look in mailbox', 'look inside mailbox', 'inspect mailbox']:
        l = 'front_door'
        message (elf_speak['meet_elf'], l) 
    elif command in ['yell at elf', 'scream', 'scream at elf', 'give elf trash', 
                    'give elf some trash', 'give elf sock', 'give elf an old sock', 
                    'give elf sock', 'yell' 'screech', 'screech at elf', 'screech back'
                    'screech back at elf', 'scream back', 'yell back', 'growl']:
        l = 'front_door'
        message (elf_speak['elf_tongue'], l)
    elif command in ['give elf paper bird', 'give elf a paper bird', 'give elf origami',
                    'give elf origami bird', 'give elf an origami bird', 
                    'give paper bird to elf', 'give elf bird', 'give bird to elf', 
                    'give paper bird to elf', 'give bird']:
        if paper_bird >= 1:
            l = 'front_door2'
            paper_bird = paper_bird - 1
            print 'Origami birds: ', paper_bird 
            message (elf_speak['get_bird'], l)
            print 'Three things I enjoy doing: ',
            enjoy = raw_input()
            print 'When I do these things, I feel: ',
            feelenjoy = raw_input()
            print """ 
    Today, you enjoy %r. 
    
    Those things make you feel %r.          
    
Veeeeerrrrrrry interesting, he says.

He looks at you expectantly, now willing to talk. """ % (enjoy, feelenjoy) 
        else:
            l = 'front_door'
            print 'Bird? What bird?'   
    elif command in ['talk to elf', 'talk with elf', 'speak to elf', 'speak with elf', 
                    'speak', 'talk']:
        l = 'front_door'
        message ('The elf refuses to talk to you', l)
    elif command in ['offer to help', 'ask to help', 'help elf', 'offer help', 'help']:
        l = 'front_door'
        message ('The elf refuses your offer of help', l)
    elif command in ['give elf butterfly wing', 'give elf a butterfly wing', 'give elf wing'
                    'give wing to elf', 'give butterfly', 'give elf butterfly', 
                    'give butterfly wing to elf','give a butterfly wing to elf']:
        l = 'front_door'
        message (elf_speak['no_butterfly'], l)
    elif command in ['look at mat', 'look under welcome mat', 'look under mat', 
                    'investigate mat', 'take mat', 'lift mat', 'move mat', 'inspect mat']:
        l = 'front_door'
        message ('You peer under the dusty mat to find more dust and dirt.', l)
    elif command in ['pull up boards', 'pull up floor boards', 'look under boards', 
                    'look under floor boards', 'look under floor boards', 'inspect porch',
                    'inspect floorboards']:
        l = 'front_door'
        message ('You hear some rodent-like sounds when you try to pull up the floor' +
                ' boards. The floor boards will not move, probably just as well.')
    elif command in ['open door', 'open the door', 'go inside', 'go inside the house',
                    'go inside the house', 'inspect door']:
        l = 'front_door'
        message ('The door is locked. You cannot enter', l)
    elif command in ['go south', 'walk south', 'walk to the south', 'south', 's']:
        l = 'front_yard'
        message ('You arrive in the yard in front of the house', l)
    elif command in ['go north', 'walk north', 'north', 'n', 'go west', 'walk west', 'west'
                    'w', 'go east', 'walk east', 'east', 'e']:
        l = 'front_door'
        message ('You can not go there from the porch', l)
    else:
        message ('I do not know how to apply that word here', l)
    return l, paper_bird   
        
#NEW FRONT_DOOR LOC
def process_front_door2(command, paper_bird):
    l = 'front_door2'
    if command in ['open mailbox', 'check mail', 'open the mailbox', 'check the mail', 
                    'open mail box']:
        l = 'front_door2'
        message ('The mailbox is already open') 
    elif command in ['yell at elf', 'scream', 'scream at elf', 'give elf trash', 
                    'give elf some trash', 'give elf sock', 'give elf an old sock', 
                    'give elf sock', 'yell' 'screech', 'screech at elf', 'screech back'
                    'screech back at elf', 'scream back', 'yell back', 'growl']:
        l = 'front_door2'
        message ('The elf laughs at your antics', l)
    elif command in ['give elf paper bird', 'give elf a paper bird', 'give elf origami',
                    'give elf origami bird', 'give elf an origami bird', 
                    'give paper bird to elf', 'give elf bird', 'give bird to elf', 
                    'give paper bird to elf', 'give bird']:
        if paper_bird >= 1:
            l = 'front_door2'
            paper_bird = paper_bird - 1
            print 'Origami birds: ', paper_bird 
            message (elf_speak['get_bird'], l)
            print 'Three things I enjoy doing: ',
            enjoy = raw_input()
            print 'When I do these things, my body feels: ',
            feelenjoy = raw_input()
            print """ 
    Today, you enjoy %r. 
    
    Those things make you feel %r.          
    
Veeeeerrrrrrry interesting, he says. 

He looks at you expectantly, now willing to talk.""" % (enjoy, feelenjoy) 
        else:
            l = 'front_door'
            print 'Bird? What bird?'   
    elif command in ['talk to elf', 'talk with elf', 'speak to elf', 'speak with elf', 
                    'ask elf question', 'speak', 'talk']:
        l = 'front_door2'
        message (elf_speak['elf_talk'], l)
    elif command in ['offer to help', 'ask to help', 'help elf', 'offer help', 'help']:
        l = 'inside_house'
        message (elf_speak['elf_help'], l)
    elif command in ['give elf butterfly wing', 'give elf a butterfly wing', 'give elf wing'
                    'give wing to elf', 'give butterfly', 'give elf butterfly', 
                    'give butterfly wing to elf','give a butterfly wing to elf']:
        l = 'front_door2'
        message (elf_speak['no_butterfly'], l)
    elif command in ['look at mat', 'look under welcome mat', 'look under mat', 
                    'investigate mat', 'take mat', 'lift mat', 'move mat']:
        l = 'front_door2'
        message ('You peer under the dusty mat to find more dust.', l)
    elif command in ['pull up boards', 'pull up floor boards', 'look under boards', 
                    'look under floor boards', 'look under floor boards']:
        l = 'front_door2'
        message ('You hear some rodent-like sounds when you try to pull up the floor' +
                ' boards. The floor boards will not move, probably just as well.')
    elif command in ['open door', 'open the door', 'go inside', 'go inside the house',
                    'go inside the house']:
        l = 'front_door2'
        message ('The door is locked. You cannot enter', l)
    elif command in ['go south', 'walk south', 'walk to the south']:
        l = 'front_yard'
        message ('You arrive in the yard in front of the house', l)
    elif command in ['go north', 'walk north', 'north', 'n', 'go west', 'walk west', 'west'
                    'w', 'go east', 'walk east', 'east', 'e']:
        l = 'front_door2'
        message ('You can go there from the porch', l)
    else:
        message ('I do not know how to apply that word here', l)
    return l, paper_bird        

def process_inside_house(command):
    l = 'inside_house'
    if command in ['leave', 'go to door', 'go to porch', 'go outside', 'leave house']:
        l = 'front_door'
        message ('You leave the house closing the door behind you', l)
    elif command in ['read paper', 'read pamphlet', 'read piece of paper', 'pick up paper',
                    'take paper', 'grab paper', 'look at paper', 'take paper', 'look at paper']:
        l = 'inside_house'
        message (troll_speak['anxiety_info'], l)
    elif command in ['talk', 'talk to troll', 'chat', 'chat with troll']:
        l = 'inside_house2'
        message (troll_speak['troll_talk'], l)
    elif command in ['tell joke', 'tell a joke', 'tell troll a joke', 'tell troll joke',
                    'tell joke to troll', 'tell another', 'joke', 'tell another joke'
                    'tell troll another joke']:
        l = 'inside_house2'
        message (troll_speak['troll_joke'], l)
        print (random.choice(jokes))
        print "The troll's belly shakes and he makes a barking-burping noise. He is laughing!"
    elif command in ['take a deep breath', 'take deep breath', 'try a deep breath', 'breathe',
                    'try a deep breath', 'inhale slowly', 'slow down breathing','breathe slowly',
                    'try breathe deep with troll', 'suggest deep breathing to troll', 
                    'suggest deep breath', 'suggest troll breathes deeply',
                    'take deep breath with troll', 'take breath']:
        l = 'inside_house2'
        message (troll_speak['troll_breath'], l)  
        print 'Inhale deeply for'
        countdown(5)
        print ("Exhale deeply for")
        countdown(5)
        print 'You both can feel a calm spreading through you.'
    else:
        message ('I do not know how to apply that word here', l)
    return l
    
def process_inside_house2(command):
    l = 'inside_house2'
    if command in ['leave', 'go to door', 'go to porch', 'go outside', 'leave house']:
        l = 'front_door2'
        message ('You leave the house closing the door behind you', l)
    elif command in ['read paper', 'read pamphlet', 'read piece of paper', 'pick up paper',
                    'take paper', 'grab paper', 'look at paper', 'take paper', 'look at paper']:
        l = 'inside_house2'
        message (troll_speak['anxiety_info'], l)
    elif command in ['talk', 'talk to troll', 'chat', 'chat with troll']:
        l = 'inside_house2'
        message (troll_speak['troll_talk'], l)
    elif command in ['tell joke', 'tell a joke', 'tell troll a joke', 'tell troll joke',
                    'tell joke to troll', 'tell another', 'joke', 'tell another joke'
                    'tell troll another joke']:
        l = 'inside_house2'
        message (troll_speak['troll_joke'], l)
        print (random.choice(jokes))
        print "The troll's belly shakes and he makes a barking-burping noise. He is laughing!"
    elif command in ['take a deep breath', 'take deep breath', 'try a deep breath', 'breathe',
                    'try a deep breath', 'inhale slowly', 'slow down breathing','breathe slowly',
                    'try breathe deep with troll', 'suggest deep breathing to troll'
                    'suggest deep breath', 'suggest troll breathes deeply',
                    'take deep breath with troll', 'take breath']:
        l = 'inside_house2'
        message (troll_speak['troll_breath'], l)  
        print 'Inhale deeply for'
        countdown(5)
        print ("Exhale deeply for")
        countdown(5)
        print 'You both can feel a calm spreading through you.'
    else:
        message ('I do not know how to apply that word here', l)
    return l

#while True is True - forever loop
while True:
    command = raw_input(prompt)
#creating look command. 
    if command in ['look', 'look around']:
        look(location)
    elif command in ['exit', 'quit']:
        break
    elif location == 'front_yard':
        (location, butterfly_wing) = process_front_yard(command, butterfly_wing)
    elif location == 'front_yard2':
        (location, butterfly_wing) = process_front_yard2(command, butterfly_wing)
    elif location == 'west_field':
        location = process_west_field(command)
    elif location == 'notice_board':
        (location, paper_bird) = process_notice_board(command, paper_bird)
    elif location == 'east_field':
        location = process_east_field(command)
    elif location == 'easteast_field':
        location = process_easteast_field(command)
    elif location == 'quaking_bog':
        (location, butterfly_wing) = process_quaking_bog(command, butterfly_wing)
    elif location == 'bog_heart':
        (location, butterfly_wing) = process_bog_heart(command, butterfly_wing)
    elif location == 'bog_heart2':
        (location, butterfly_wing) = process_bog_heart2(command, butterfly_wing)
    elif location == 'south_field':
        location = process_south_field(command)
    elif location == 'north_field_west':
        location = process_north_field_west(command)
    elif location == 'north_field_east':
        location = process_north_field_east(command)
    elif location == 'maze_entrance':
        location = process_maze_entrance(command)
    elif location == 'maze':
        location = process_maze(command)
    elif location == 'front_door':
        (location, paper_bird) = process_front_door(command, paper_bird)
    elif location == 'front_door2':
        (location, paper_bird) = process_front_door2(command, paper_bird)
    elif location == 'inside_house':
        location = process_inside_house(command)
    elif location == 'inside_house2':
        location = process_inside_house2(command)
    else:
        message ('Where did you go?' + command, location) 



#common words: look, inventory, drop, throw



  




