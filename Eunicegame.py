#all imports should be at top of file
import sys
#import dictionary of story text
from all_text_dicts import *

import random

jokes = ['Q: What did one wall say to the other wall? A: I\'ll meet you at the corner.',
        'Q: What gets wetter the more it dries? A: A towel.', 
        'Q: Why do you go to bed every night? A: Because the bed won\'t come to you!',
        'Q: Where do animals gowhen their tales fall off? A: A retail store',
        'Q: Why can\'t you hear a pterodactyl going to the bathroom? A: Because the P is silent.',
        'Q: A magician was driving down the street, what went wrong? A: He turned into a driveway!',
        'Q: How do you make tissue dance? A: You put a little boogie in it!',
        'Q: What did the 0 say to the 8? A: Nice belt.',
        'Q: Who earns a living driving their customers away? A: Taxi drivers.',
        'Q: What bow can\'t be tied? A: A rainbow.',
        ]
#http://www.ducksters.com/jokes/silly.php and others

print (random.choice(jokes))
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

You are standing in a field just south of an old, wood house. 
At one time it was a dearly loved home, a place of comfort and laughter.
Now it stands silent and empty, with its windows boarded up. 
The yard in front of you is filled with trash: 
rotten wooden boards, twisted metal, and old tires.

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
    if command in ['clean trash', 'clean up trash', 'clean up',
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
                    'walk toward door', 'walk north', 'go north', 'go to porch', 
                    'go to the porch', 'walk to poch', 'walk to the porch']:
        l = 'front_door'
        message ('You walk to the front door, picking your way gingerly across the ' +
                 'rusted nails and broken glass.', l)  
    elif command in ['walk west', 'go west']:
        l = 'west_field'
        message ('You walk into the dusty western field. The land becomes hilly, and ' +
                    'you notice a dark object ahead but cant make out what it is.', l) 
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
#RULE: a function should always have a return. Even though it lets you not have one, ALWAYS have one
    return l
        
def process_notice_board(command, paper_bird):
    l = 'notice_board'
    if command in ['read board', 'read the board', 'read notes', 'read the notes', 'read a note',
                    'read notice board', 'read the notice board', 'read notes on board', 
                    'read the notes on board', 'read note', 'read notice', 'read notices']:
        l = 'notice_board'
        message (gratitude_notes['note1'], l)
    elif command in ['read another', 'read another note', 'read another gratitude',
                    'read another gratitude note', 'read a second page', 'read another page']:
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
                    'read notice board', 'go to board', 'go to the board', 'go to the notice board', 
                    'walk to the board', 'walk to board', 'walk to notice board']:
        l = 'south_field'
        message ('You do not see a notice board nearby', l)
    elif command in ['walk towards board', 'walk west', 'go west']:
        l = 'west_field'
        message ('You are wandering through the dusty west field.', l) 
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

def process_front_door(command, paper_bird):
    l = 'front_door'
    if command in ['open mailbox', 'check mail', 'open the mailbox', 'check the mail', 
                    'open mail box', 'look in mailbox', 'look inside mailbox']:
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
    
    Some physical feelings related to enjoyment are %r.          
    
Veeeeerrrrrrry interesting, he says.

He looks at you expectantly, now willing to talk. """ % (enjoy, feelenjoy) 
        else:
            l = 'front_door'
            print 'Bird? What bird?'   
    elif command in ['talk to elf', 'talk with elf', 'speak to elf', 'speak with elf', 
                    'speak', 'talk']:
        l = 'front_door'
        message ('The elf refuses to talk to you', l)
    elif command in ['offer to help', 'ask to help', 'help elf', 'offer help']:
        l = 'front_door'
        message ('The elf refuses your offer of help', l)
    elif command in ['give elf butterfly wing', 'give elf a butterfly wing', 'give elf wing'
                    'give wing to elf', 'give butterfly', 'give elf butterfly', 
                    'give butterfly wing to elf','give a butterfly wing to elf']:
        l = 'front_door'
        message (elf_speak['no_butterfly'], l)
    elif command in ['look at mat', 'look under welcome mat', 'look under mat', 
                    'investigate mat', 'take mat', 'lift mat', 'move mat']:
        l = 'front_door'
        message ('You peer under the dusty mat to find more dust and dirt.', l)
    elif command in ['pull up boards', 'pull up floor boards', 'look under boards', 
                    'look under floor boards', 'look under floor boards']:
        l = 'front_door'
        message ('You hear some rodent-like sounds when you try to pull up the floor' +
                ' boards. The floor boards will not move, probably just as well.')
    elif command in ['open door', 'open the door', 'go inside', 'go inside the house',
                    'go inside the house']:
        l = 'front_door'
        message ('The door is locked. You cannot enter', l)
    elif command in ['go south', 'walk south', 'walk to the south']:
        l = 'front_yard'
        message ('You arrive in the yard in front of the house', l)
    else:
        message ('We could not parse that. You cannot ' + command, l)
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
    
    Some physical feelings related to enjoyment are %r.          
    
Veeeeerrrrrrry interesting, he says. 

He looks at you expectantly, now willing to talk.""" % (enjoy, feelenjoy) 
        else:
            l = 'front_door'
            print 'Bird? What bird?'   
    elif command in ['talk to elf', 'talk with elf', 'speak to elf', 'speak with elf', 
                    'ask elf question', 'speak', 'talk']:
        l = 'front_door2'
        message (elf_speak['elf_talk'], l)
    elif command in ['offer to help', 'ask to help', 'help elf', 'offer help']:
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
    else:
        message ('We could not parse that. You cannot ' + command, l)
    return l, paper_bird        

def process_inside_house(command):
    l = 'inside_house'
    if command in ['leave', 'go to door', 'go to porch', 'go outide']:
        l = 'front_door'
        message ('You leave the house closing the door behind you', l)
    elif command in ['read paper', 'read pamphlet', 'read piece of paper', 'pick up paper',
                    'take paper', 'grab paper', 'look at paper', 'take paper']:
        l = 'inside_house'
        message (troll_speak['anxiety_info'], l)
    elif command in ['talk', 'talk to troll', 'chat', 'chat with troll']:
        l = 'inside_house'
        message (troll_speak['troll_talk'], l)
    elif command in ['tell joke', 'tell a joke', 'tell troll a joke', 'tell troll joke',
    'tell joke to troll', 'tell another', 'joke']:
        l = 'inside_house'
        message (troll_speak['troll_joke'], l)
        print (random.choice(jokes))
    else:
        message ('We could not parse that. You cannot ' + command, l)
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
        (location, paper_bird) = process_front_door(command, paper_bird)
    elif location == 'front_door2':
        (location, paper_bird) = process_front_door2(command, paper_bird)
    elif location == 'inside_house':
        location = process_inside_house(command)
    else:
        message ('Where did you go?' + command, location) 



#common words: look, inventory, drop, throw



  




