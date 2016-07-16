import sys

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
Now it stands silent and empty, with its windows boarded up. The yard around you is filled 
with rotten wooden boards, twisted metal, and old tires.

Around you, the field stretches out in all directions. To the west, you see a public notice board. 

You decide its time to begin making a change.
"""

#this creates a simple prompt like in Zork
prompt = '>'
print intro

#this should work - why doesnt it work? 
paper_bird = None

#location variable is a context state. This starts game at 'front_yard'
location = 'front_yard'

#create dictionary of place descriptions
descript = dict()
    
descript['front_yard'] = """
A few desperate weeds struggle in the dusty ground. You look closer and recognize 
ragged lavender plant, a tired rose bush, and realize that this was once a beautiful garden. 
Now there is more trash here than plants. 
"""
descript['notice_board'] = """
A large public notice board stands in the middle of the wide field. You wonder why the builder 
decided to put it out here far from any road or town.
Clearly a few people once came here, because there are a few colorful pages pinned to the board.
You also notice extra pins, and a pad of blank paper with a pencil on a thin green ribbon 
next to the board.
"""
descript['front_door'] = """
The porch is slanting away from the house, it's likely some of the floor boards are rotten.
You step carefully and notice there is an old mailbox next to a very large front door. 
The windows are boarded up. You cannot see in.
"""
descript['south_field'] = """
The field stretches out before you.
"""
descript['inside_house'] = """
Thick dust covers everything. You cough as your eyes slowly accustom to the dim room.

A table with a broken leg and knocked over chair were abandoned in the western corner. 
A sink and cabinet sits along the north - east wall, and you can hear scrabbling of 
some small animals.
In the south corner is a large, dirty steamer trunk. Sitting on the trunk is a huge troll.
"""
descript['front_yard2'] = """
Green flowering herbs and bushes wave in the slight breeze. You can smell the light fragrance
of many flowers and hear the industrious buzzing of bees around you.
Many more notes have been added to yours on the public gratitude board!
"""
descript['front_door2'] = """
The front door is painted deep green with little carvings of ivy and berries in the corner.
"""

descript['inside_house2'] = """
You look around an notice that the boards have disappeared from the window and you are
now in a tiny home.

A polished oak table and chair with a blue cushion fits into the west corner. 
There is a bowl of fruit by  sink and cabinets are bright yellow. 

And in the south corner the steamer trunk has been polished. Its leather gleams a rich dark
brown, and its brass fittings sparkle in the sunlight.

"""

#create look function that accesses dictionary
#its better to specifically pass in the the variables you need in given function
def look(loc_to_describ):
    #use message not print because print is *very* specific and 
    #we created message to have flexibility
    #we pass the same name for an argument below because its going to take 'front_yard' and print 'front_yard'
    message(descript[loc_to_describ],loc_to_describ)

def process_front_yard(command):
    l = 'front_yard'   
    if command in ['go inside', 'go in house', 'go in the house', 'go in', 'enter house', 
                    'open door', 'walk inside', 'walk inside house']:
        l = 'front_yard'
        message ('You are too far from the house', l)
    elif command in ['read board', 'read paper', 'read papers', 'read notice', 'read notes',
                    'read notice board']:
        l = 'front_yard'
        message ('You are too far to read the notes on the board', l)
    elif command in ['go to door', 'go to the door', 'walk to door', 'walk to the door',
                    'walk closer to house', 'walk to house', 'walk toward house', 'walk toward door', 
                    'walk north', 'go north']:
        l = 'front_door'
        message ('You walk to the front door, picking your way gingerly across the ' +
                 'rusted nails and broken glass.', l)  
    elif command in ['go to board', 'go to the board', 'go to the notice board', 
                    'walk to the board', 'walk to board', 'walk to notice board', 
                    'walk towards board', 'walk west', 'go west']:
        l = 'notice_board'
        message ('You walk to the notice board. It has a handful of brightly colored papers' + 
                'with different handwriting. The pages look old and weather stained.', l)      
    elif command in ['go south', 'walk field', 'walk south', 'walk to the south']:
        l = 'south_field'
        message ('The field stretches on and on before you.', l)
    else:
        message ('We could not parse that. You cannot ' + command, l)
    return l
    
        
def process_notice_board(command, paper_bird):
    l = 'notice_board'
    if command in ['read board', 'read the board', 'read notes', 'read the notes', 'read a note',
                    'read notice board', 'read the notice board', 'read notes on board', 
                    'read the notes on board', 'read note']:
        l = 'notice_board'
        message ("""You move closer to read the colorful notes. They are pages of a 
gratitude journal. One yellow note reads:
        
Three things I am grateful for today: 
    my cats, quiet time to sip tea, laughing on the phone with a friend
I feel these emotions when I think of these things: 
    loved, content, joyful
""", l)
    elif command in ['read another', 'read another note', 'another', 'read another gratitude',
                    'read another gratitice note']:
            l = 'notice_board'
            message ("""An rose-colored paper reads:

Three things I am grateful for today: 
    morning commute without meeting any trolls or dragons, my children, sunny weather
I feel these emotions when I think of these things: 
    comfortable, inspired, happy
""", l) 
    elif command in ['write note', 'write a note', 'write gratitude note', 'write a gratitude note',
                    'write gratitude', 'add note', 'add a note', 'add a gratitude note', 
                    'post gratitude note']:
        l = 'notice_board'
        print 'Three things I am grateful for today:',
        grat = raw_input()
        print 'When I think of these things, I feel:',
        feelgrat = raw_input()
        print """ 
    Today, you feel grateful for %r. 
    
    Some emotions related to gratitude are %r.          
    
Thank you for sharing. 
When you post your gratitude note on the board, a tiny folded paper bird
flutters down from above you. You keep it for later. """ % (grat, feelgrat) 
#origami count
    #count in the if statement every time there is an origami bird and save that number
    #something to do with return?         
        if paper_bird is None:
            paper_bird = 1
        else:
            paper_bird = paper_bird + 1
        print paper_bird    
    elif command in ['walk to front_yard', 'walk to the front_yard', 'walk east',
                    'walk to the east', 'walk back to house', 'walk back to the house']:
        l = 'front_yard'
        message ('You return to the yard in front of the house.', l)
    elif command in ['go south', 'walk field', 'walk south', 'walk to the south']:
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
        message ('You arrive in the yard in front of the house', l)             
    elif command in ['go south', 'go the the south', 'walk field', 'walk on', 'walk to the south', 
                    'walk south']:
        l = 'south_field'
        message ('The field stretches on and on before you.', l)
    else:
        message ('We could not parse that. You cannot ' + command, l)
    return l

def process_front_door(command):
    l = 'front_door'
    if command in ['open mailbox']:
        l = 'front_door'
        message ('You gingerly open the mailbox and peer inside. There is a sudden rustling' +
                'and a pair of beady eyes glare at you from a tiny wrinkled face. The elf,' +
                'for it has narrow pionty ears, is not happy to see you and screeches loudly' +
                'BAAAAAAAA', l) 
    #activity with elf
    #open door - is it locked first?
    #use key on door - how can a program 'have' a key or 'have' origami bird?
    else:
        message ('We could not parse that. You cannot ' + command, l)
    return l
        
def process_inside_house(command):
    l = 'inside_house'
    if command in ['leave', 'go to door', 'go to porch', 'go outide']:
        l = 'front_door'
        message ('You leave the house closing the door behind you', l)

#while True is True - forever loop
while True:
    command = raw_input(prompt)
#creating look command. 
    if command in ['look', 'look around']:
        look(location)
    elif command in ['exit', 'quit']:
        break
    elif location == 'front_yard':
        location = process_front_yard(command)
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

#https://positivepsychologyprogram.com/positive-psychology-exercises/
#https://characterlab.org



  




