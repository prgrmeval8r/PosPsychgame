import sys

#Saving Debug feature for when I figure out how I want to use it
#DEBUG = False
#if len(sys.argv) > 1:
    #DEBUG = True  

#create message function
def message(m, location):
  print m, location
  #I decided that I want the current location ALWAYS printed
  #if DEBUG:
    #print "CURRENT LOCATION:", location



intro = """
Welcome to Eunice.

You are standing in a field just south of an old wood house. At one time it was a dearly
loved home, a place of comfort and laughter.
Now it stands silent and empty, with its windows boarded up. The yard around you is filled 
with rotten wooden boards, twisted metal, and old tires.

Next to you is a public notice board. Different colored pieces of paper with handwritten notes
are posted on the board. The paper rustles in the light breeze.

You decide now its time to begin making a change.
"""

#this creates a simple prompt like in Zork
prompt = '>'
print intro

#location variable is a context state. This starts game at 'front_yard'
location = 'front_yard'

#create dictionary of place descriptions
descript = dict()
    
descript['front_yard'] = """
A few desperate weeds struggle in the dusty ground. You look closer and recognize 
ragged lavender plant, a tired rose bush, and realize that this was once a beautiful garden. 
Now there is more trash here than plants. 
The only cheerful thing is the public notice board.
"""

descript['front_door'] = """
The porch is slanting away from the house, it's likely some of the porch has rotten away.
You step carefully and notice there is an old mailbox next to a very large front door. 
The windows are boarded up and you cannot see in.
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
def look(location):
    #use message not print because print is *very* specific and 
    #we created message to have flexibility
    message(descript[location], location)

# All the things you can do in the front yard, then do for each location 
# except that defining this as a function messes all sorts of things up?!?   
def process_front_yard(command):
    #my guess for how to create a loop in a function that will have a break
    while l is'front_yard'
        if command in ['go inside', 'go in house', 'go in the house', 'go in', 'enter house', 
                    'open door', 'walk inside', 'walk inside house']:
            l = 'front_yard'
            message ('You are too far from the house', location)
        elif command in ['read board', 'read paper', 'read papers', 'read notice', 'read notes',
                    'read notice board']:
            l = 'front_yard'
            message ("""You move closer to read the colorful notes. They are pages of a 
gratitude journal. One yellow note reads:
        
Three things I am grateful for today: 
    my cats, quiet time to sip tea, laughing on the phone with a friend
I feel these emotions when I think of these things: 
    loved, content, joyful
One thing I am frustrated with today: 
    missed deadline on a work project
I feel these emotions when I think of this thing: 
    embarassed, lonely
                    
Another rose-colored paper reads:

Three things I am grateful for today: 
    a seat on the train during morning commute, a painting my son made me at school, sunny weather
I feel these emotions when I think of these things: 
    comfortable, inspired, happy
One thing I am frustrated with today: 
    messy kitchen
I feel these emotions when I think of this thing: 
    angry, tired
                    
As you return the notes to the board, you notice a pad of blank paper and a pencil on a 
thin green ribbon next to the board.""", location) 
   
        elif command in ['write note', 'write gratitude note', 'write gratitude', 'add note']:
            l = 'front_yard'
            print 'Three things I am grateful for today:',
            grat = raw_input()
            print 'When I think of these things, I feel:',
            feelgrat = raw_input()
            print 'One thing I am frustrated with today:',
            frust = raw_input()
            print 'When I think of this thing, I feel:', 
            feelfrust = raw_input()
            print """ 
    Today, you feel grateful for %r. 
    
    Some emotions related to gratitude are %r.          
    
    You feel frustrated with %r.
    
    Some emotions related to frustrations are %r. 
    
Thank you for sharing.""" % (grat, feelgrat, frust, feelfrust)         
        elif command in ['go to door', 'go to the door', 'walk to door', 'walk to the door',
                    'walk closer to house', 'walk to house', 'walk north', 'go north']:
            l = 'front_door'
            message ('You walk to the front door, picking your way gingerly across the ' +
                 'rusted nails and broken glass.', location)
        elif command in ['exit', 'quit']:
        break 
        else:
        return l



#while True is True - forever loop
while True:
    command = raw_input(prompt)
#creating look command. 
    if command in ['look', 'look around']:
        look(location)
    elif location == 'front_yard':
        location = process_front_yard(command)
    elif location == 'front_door':
        location = process_front_door(command)
    elif location == 'inside_house':
        location = process_inside_house(command)
    else:
        message ('Where did you go?' + command, location) 

#https://positivepsychologyprogram.com/positive-psychology-exercises/
#https://characterlab.org



  




