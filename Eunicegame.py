#all imports should be at top of file
import sys
#import dictionary of story text
from all_text_dicts import *

#Saving Debug feature for when I figure out how I want to use it
#DEBUG = False
#if len(sys.argv) > 1:
    #DEBUG = True  

#create message function
#message takes two arguments, those arguments can change or even be different strings
def message(text, current_loc):
  print text, current_loc
  #I decided that I want the current location ALWAYS printed
  #if DEBUG:
    #print "CURRENT LOCATION:", location


intro = """
Welcome to Eunice.

You are standing in a field just south of an old wood house. At one time it was a dearly
loved home, a place of comfort and laughter.
Now it stands silent and empty, with its windows boarded up. The yard in front of you is filled 
with rotten wooden boards, twisted metal, and old tires.

You decide its time to begin making a change.
"""

#this creates a simple prompt like in Zork
prompt = '>'
print intro

#Global variable for paper birds  
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
    if command in ['clean trash', 'clean up trash', 'look through trash', 'clean up',
                    'clean yard']:
        l = 'front_yard'
        message ('Its a huge job, but you organize some of the broken objects into piles ' +
                'and clear some space around the plants. Beneath the trash you find ' +
                'a delicate butterfly wing. You keep it for later.', l)
                #butterfly wing count     
        butterfly_wing = butterfly_wing + 1
        print 'Butterfly wings: ', butterfly_wing    
        
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
                    'walk toward door', 'walk north', 'go north']:
        l = 'front_door'
        message ('You walk to the front door, picking your way gingerly across the ' +
                 'rusted nails and broken glass.', l)  
    elif command in ['walk west', 'go west']:
        l = 'west_field'
        message ('You walk into the dusty western field. The land becomes hilly, and ' +
                    'you notice a dark object but cant make out what it is.', l) 
    elif command in ['go south', 'walk south']:
        l = 'south_field'
        message ('The field stretches on and on before you.', l)
    else:
        message ('We could not parse that. You cannot ' + command, l)
    return l, butterfly_wing
    
        
def process_west_field(command):
    l = 'west_field'
    if command in ['go south', 'walk south']:
        l = 'south_field'
        message ('The field stretches on and on before you.', l)
    elif command in ['go west', 'walk west', 'go to notice board', 'walk to board']:
        l = 'notice_board'
        message ('You progress further west through the dusty field of rocks and ' +
                'forgotten food wrappers. Plastic bags drift by in the breeze. ' +
                'You stop walking when you reach an old public notice board.', l)
    elif command in ['go east', 'walk east']:
        l = 'front_yard'
        message ('You arrive at the front yard of the house.', l)
    else:
        message ('We could not parse that. You cannot ' + command, l)
        
def process_notice_board(command, paper_bird):
    l = 'notice_board'
    if command in ['read board', 'read the board', 'read notes', 'read the notes', 'read a note',
                    'read notice board', 'read the notice board', 'read notes on board', 
                    'read the notes on board', 'read note']:
        l = 'notice_board'
        message (gratitude_notes['note1'], l)
    elif command in ['read another', 'read another note', 'another', 'read another gratitude',
                    'read another gratitude note']:
            l = 'notice_board'
            message (gratitude_notes['note2'], l) 
    elif command in ['write note', 'write a note', 'write gratitude note', 'write a gratitude note',
                    'write gratitude', 'add note', 'add a note', 'add a gratitude note', 
                    'post gratitude note']:
        l = 'notice_board'
        print 'Three things I am grateful for today: ',
        grat = raw_input()
        print 'When I think of these things, I feel: ',
        feelgrat = raw_input()
        print """ 
    Today, you feel grateful for %r. 
    
    Some emotions related to gratitude are %r.          
    
Thank you for sharing. 
When you post your gratitude note on the board, a tiny folded paper bird
flutters down from above you. You keep it for later. """ % (grat, feelgrat) 
#origami count       
        paper_bird = paper_bird + 1
        print 'Origami birds: ', paper_bird    
    elif command in ['walk east', 'go east']:
        l = 'west_field'
        message ('You are wandering through the dusty west field.', l)
    elif command in ['go south', 'walk south']:
        l = 'south_field'
        message ('The field stretches on and on before you.', l)
    else:
        message ('We could not parse that. You cannot ' + command, l)
    return l, paper_bird
    

def process_south_field(command):
    l = 'south_field'   
    if command in ['go inside', 'go in house', 'go in the house', 'go in', 'enter house', 
                    'open door', 'walk inside', 'walk inside house']:
        l = 'south_field'
        message ('You are too far from the house', l)
    elif command in ['read board', 'read paper', 'read papers', 'read notice', 'read notes',
                    'read notice board']:
        l = 'south_field'
        message ('You are too far to read the notes on the board', l)
    elif command in ['go to board', 'go to the board', 'go to the notice board', 
                    'walk to the board', 'walk to board', 'walk to notice board', 
                    'walk towards board', 'walk west', 'go west']:
        l = 'notice_board'
        message ('You walk to the notice board. It has a handful of brightly colored papers' + 
                'with different handwriting.', l) 
    elif command in ['go to door', 'go to the door', 'walk to door', 'walk to the door']:
        l = 'south_field'
        message ('You too far from the door', l)
    elif command in ['walk north', 'go north', 'walk to the north', 'walk to front_yard',
                    'walk to the front_yard', 'go back']:
        l = 'front_yard'
        message ('You arrive at the yard in front of the house', l)             
    elif command in ['go south', 'go the the south', 'walk field', 'walk on', 'walk to the south', 
                    'walk south']:
        l = 'south_field'
        message ('The field stretches on and on before you.', l)
    else:
        message ('We could not parse that. You cannot ' + command, l)
    return l

def process_front_door(command):
    l = 'front_door'
    if command in ['open mailbox', 'check mail', 'open the mailbox', 'check the mail']:
        l = 'front_door'
        message ('You open the mailbox and peer inside. There is a sudden rustling ' +
                'and a pair of beady eyes glare at you from a tiny wrinkled face. The elf,'  +
                'for it has narrow pointy ears, is not happy to see you and screeches loudly ' +
                'BAAAAAAAA!!', l) 
    elif command in ['yell at elf', 'scream', 'scream at elf', 'give elf trash', 
                    'give elf some trash', 'give elf sock', 'give elf an old sock', 
                    'give elf sock']:
        message ('The little house elf sticks out his tongue and turns his back on you', l)
        #activity with elf
        #give elf butter fly wing or paper bird
        #lose on butterfly wing or paper bird
        #elf gives key to the house - or is this too easy?
        #additional conversation with elf. Maybe he tells something useful?
    #maybe there can be something else to interact with too?
        #doormat or...?
    elif command in ['look at mat', 'look under welcome mat', 'look under mat', 
                    'investigate mat', 'take mat', 'lift mat', 'move mat']:
        l = 'front_door'
        message ('You peer under the dusty welcome mat to find more dust and dirt.', l)
    elif command in ['pull up boards', 'pull up floor boards', 'look under boards', 
                    'look under floor boards', 'look under floor boards']:
        l = 'front_door'
        message ('You hear some rodent-like sounds when you try to pull up the floor' +
                ' boards. The floor boards wont move, probably just as well.')
    elif command in ['go south', 'walk south', 'walk to the south']:
        l = 'front_yard'
        message ('You arrive in the yard in front of the house', l)
    else:
        message ('We could not parse that. You cannot ' + command, l)
    return l
        
def process_inside_house(command):
    l = 'inside_house'
    if command in ['leave', 'go to door', 'go to porch', 'go outide']:
        l = 'front_door'
        message ('You leave the house closing the door behind you', l)
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
    elif location == 'west_field':
        location = process_west_field(command)
    elif location == 'notice_board':
        (location, paper_bird) = process_notice_board(command, paper_bird)
    elif location == 'south_field':
        location = process_south_field(command)
    elif location == 'front_door':
        location = process_front_door(command)
    elif location == 'inside_house':
        location = process_inside_house(command)
    else:
        message ('Where did you go?' + command, location) 



#common words: look, inventory, drop, throw



  




