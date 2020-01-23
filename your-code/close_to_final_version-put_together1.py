
# coding: utf-8

# In[1]:


import inquirer 

# define rooms and items

# ROOM 1 - IRONHACK CLASSROM

ironhack_classroom = {
    "name": "ironhack_classroom",
    "type": "room",
}


whiteboard = {
    "name": "whiteboard",
    "type": "furniture",
}

carlos = {
    "name": "carlos",
    "type": "teacher",
}

door_a = {
    "name": "door_a",
    "type": "door",
}

key_a = {
    "name": "key_a",
    "type": "key",
    "target": door_a,
}

# ROOM 2 - LIST COMPREHENSION ROOM


list_comprehension_room = {
    "name": "list_comprehension_room",
    "type": "room",
}

piece_of_paper = {
    "name": "piece_of_paper",
    "type": "furniture",
}

mattia = {
    "name": "mattia",
    "type": "teacher",
}

door_b = {
    "name": "door_b",
    "type": "door",
}

key_b = {
    "name": "key_b",
    "type": "key",
    "target": door_b,
}

####-----NEW ROOMS ----------####
string_room = {
    "name": "string_room",
    "type": "room",
}

function_room = {
    "name": "function_room",
    "type": "room",
}


####-----NEW OBJECTS IN ROOMS---------####

lamp = {
    "name": "lamp",
    "type": "furniture",
}

apple = {
    "name": "apple",
    "type": "furniture",
}

####-----TEACHERS---------####

jo = {
    "name": "jo",
    "type": "teacher",
}

cristina = {
    "name": "cristina",
    "type": "teacher",
}



door_a = {
    "name": "door_a",
    "type": "door",
}

key_a = {
    "name": "key_a",
    "type": "key",
    "target": door_a,
}


door_b = {
    "name": "door_b",
    "type": "door",
}

key_b = {
    "name": "key_b",
    "type": "key",
    "target": door_b,
}

door_c = {
    "name": "door_c",
    "type": "door",
}

key_c = {
    "name": "key_c",
    "type": "key",
    "target": door_c,
}


door_d = {
    "name": "door_d",
    "type": "door",
}


key_d = {
    "name": "key_d",
    "type": "key",
    "target": door_d,
}

outside = {
  "name": "outside",
}

all_rooms = [ironhack_classroom, list_comprehension_room, string_room, function_room, outside]

puzzle_answers = ['bla', 'blu']

all_doors = [door_a, door_b, door_c, door_d]

# define which items/rooms are related

object_relations = {
    "ironhack_classroom": [whiteboard, carlos, door_a],
    "carlos": [key_a],
    "outside": [door_d],
    "door_a": [ironhack_classroom, list_comprehension_room],
    "list_comprehension_room": [piece_of_paper, mattia, door_a, door_b],
    "mattia": [key_b],
    "string_room": [lamp, jo, door_b, door_c],
    "jo": [key_c],
    "door_b": [list_comprehension_room, string_room],
    "function_room": [apple, cristina, door_c, door_d],
    "door_d": [function_room, outside],
    "cristina": [key_d],
    "door_c": [string_room, function_room],
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": ironhack_classroom,
    "keys_collected": [],
    "target_room": outside
    
}


# In[ ]:


question_yn = [
inquirer.List('yes/no',
        message="Do you want to go in?",
        choices=['yes', 'no'],
        ),
    ]

question_a = [
inquirer.List('question_a',
        message="In GitHub, what is the first thing you do after forking a repository?",
        choices=['Clone', 'Push', 'Merge'],
        ),
    ]

question_b = [
inquirer.List('question_b',
        message="What option gives the following output? [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]",
        choices=['a) print([str(who_knows) for who_cares in list_with_numbers])', 'b) print([i for i in range(10)]', 'c) print([i for i in range(1,11)])'],
        ),
    ]

question_c = [
inquirer.List('question_c',
        message="How do you change every letter in 'THIS IS THE STRING ROOM' to lower case?",
        choices=['str.title()', 'str.lower()', 'str.down()'],
        ),
    ]

question_d = [
inquirer.List('question_d',
        message="Will the following function produce an output? lambda x: y * y",
        choices=['Yes', 'No'],
        ),
    ]

def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    """
    print("You wake up in a freezing room that is full of people you have never seen before. There are windows, but I don't think they open. You actually do remember why you are here and what has happened before. But still you feel insecure and embarrassed. You must keep moving forward!")
    linebreak()
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        print("You can’t believe it’s true, you can smell the fresh air and hear the birds! You step outside and all your classmates are having a beer! They look at you and they shout you MADE IT!!!")
    else:
        print("You are now in " + room["name"])
        linebreak()
        #first inquirer
        question1 = [
  inquirer.List('action',
                message="What would you like to do?",
                choices=['explore', 'examine',],
            ),
        ]
        answer = inquirer.prompt(question1)
        intended_action = answer['action']
        
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            #second inquirer

            question2 = [
                inquirer.List('examine',
                        message="What would you like to examine?" ,
                        choices= [dic['name'] for dic in object_relations[game_state["current_room"]['name']]],
                        ), 
                ]
            answer = inquirer.prompt(question2)
            examine_action = answer['examine']
            examine_item(examine_action)
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'.")
            play_room(room)
        linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))
    linebreak()

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room

def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been 
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None
    
    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = "You examine " + item_name + ". "
            if(item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    print("You use the key. The door didin't open. A message appears:")
                    linebreak()
                    
                    if(item["name"] == "door_a"):

                        answer_a = inquirer.prompt(question_a)
                        answer_question_a = answer_a['question_a']

                        if answer_question_a == 'Clone' :    
                            next_room = get_next_room_of_door(item, current_room)
                            output = "You opened door! Good job and good luck"

                        elif answer_question_a == 'Push':
                            output = "Sorry try again"
                        
                        elif answer_question_a == 'Merge':
                            output = "Sorry try again"
                        else:
                            output = "Sorry try again"
                    
                    if(item["name"] == "door_b"):
                        
                        answer_b = inquirer.prompt(question_b)
                        answer_question_b = answer_b['question_b']
                        
                    
                        if (answer_question_b == "b) print([i for i in range(10)]") :    
                            next_room = get_next_room_of_door(item, current_room)
                            output = "You opened door! Good job and good luck"
                        else:
                            output = "Sorry try again"
                    
                    if(item["name"] == "door_c"):
                    
                        answer_c = inquirer.prompt(question_c)
                        answer_question_c = answer_c['question_c']
                    
                        if answer_question_c == 'str.lower()' : 
                            next_room = get_next_room_of_door(item, current_room)
                            output = "You opened door! Good job and good luck"
                        else:
                            output = "Sorry try again"
                    
                    if(item["name"] == "door_d"):
                    
                        answer_d = inquirer.prompt(question_d)
                        answer_question_d = answer_d['question_d']
                    
                        if answer_question_d == 'No' :    
                            next_room = get_next_room_of_door(item, current_room)
                            output = "You opened door! Good job and good luck"
                        else:
                            output = "Sorry try again"
                    

                else:
                    output += "It is locked but you don't have the key."
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                else:
                    output += "There isn't anything interesting about it."
            print(output)
            linebreak()
            break

    if(output is None):
        print("The item you requested is not found in the current room.")


 #   if(next_room) and answer_yn == 'yes'):
 #       play_room(next_room)


    if (next_room) and inquirer.prompt(question_yn)['yes/no'] == 'yes': 
        play_room(next_room)
    else:
        play_room(current_room)


# In[ ]:


game_state = INIT_GAME_STATE.copy()

start_game()

