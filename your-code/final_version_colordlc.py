
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
    "message": 'strange words are written on the whiteboard: "fork, clone, add, commit, push, merge". you are confused but'
}

carlos = {
    "name": "carlos",
    "type": "teacher",
    "message": "carlos asks if you filled in the support form."
}

door_a = {
    "name": "door_a",
    "type": "door",
    "message": "\033[36m good job you have mastered github ;) \033 "
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
    "message": 'you pick up a piece of paper from the floor. it says the same message over and over again:"i shall not append".'
}

mattia = {
    "name": "mattia",
    "type": "teacher",
    "message": "mattia reminds you that you still haven't filled the support form."
}

door_b = {
    "name": "door_b",
    "type": "door",
    "message": "\033[36m good job! on to the next challenge. \033 "
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

coffee_machine = {
    "name": "coffee_machine",
    "type": "furniture",
    "message": "the coffee machine doesn't work. you add water. still doesn't work. you clean the tray."
}

apple = {
    "name": "apple",
    "type": "furniture",
    "message": "it's an apple. you eat it. it tastes super weird."
}

####-----TEACHERS---------####

jo = {
    "name": "jo",
    "type": "teacher",
    "message": "jo says she can help! oh but she doesn't see your support form."
}

cristina = {
    "name": "cristina",
    "type": "teacher",
    "message": "cristina says you should ask your TAs."
}


door_c = {
    "name": "door_c",
    "type": "door",
    "message": "\033[36m nice one! almost there... \033 "
}

key_c = {
    "name": "key_c",
    "type": "key",
    "target": door_c,
}


door_d = {
    "name": "door_d",
    "type": "door",
    "message": "\033[36m well done! there's light behind this door... \033 "
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



all_doors = [door_a, door_b, door_c, door_d]

# define which items/rooms are related

object_relations = {
    "ironhack_classroom": [whiteboard, carlos, door_a],
    "whiteboard": [key_a],
    "outside": [door_d],
    "door_a": [ironhack_classroom, list_comprehension_room],
    "list_comprehension_room": [piece_of_paper, mattia, door_a, door_b],
    "piece_of_paper": [key_b],
    "string_room": [coffee_machine, jo, door_b, door_c],
    "coffee_machine": [key_c],
    "door_b": [list_comprehension_room, string_room],
    "function_room": [apple, cristina, door_c, door_d],
    "door_d": [function_room, outside],
    "apple": [key_d],
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
        message=" “\033[1;32;40m Do you want to go in? \033 ",
        choices=['yes', 'no'],
        ),
    ]

question_a = [
inquirer.List('question_a',
        message=" “\033[1;32;40m In GitHub, what is the first thing you do after forking a repository?",
        choices=['Clone', 'Push', 'Merge'],
        ),
    ]

question_b = [
inquirer.List('question_b',
        message="“\033[1;32;40m What option gives the following output? [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] \033 ",
        choices=['#- print([str(who_knows) for who_cares in list_with_numbers])', '#- print([i for i in range(10)]', '#- print([i for i in range(1,11)])'],
        ),
    ]

question_c = [
inquirer.List('question_c',
        message="“\033[1;32;40m How do you change every letter in 'THIS IS THE STRING ROOM' to lower case? \033 ",
        choices=['str.title()', 'str.lower()', 'str.down()'],
        ),
    ]

question_d = [
inquirer.List('question_d',
        message="“\033[1;32;40m Will the following function produce an output? lambda x: y * y \033 ",
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
    print("You wake up in a freezing room that is full of people you have never seen before. \n There are windows, but I don't think they open. \n You actually do remember why you are here and what has happened before. But still you feel insecure and embarrassed. \n You must keep moving forward!")
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
        print("\033[36m You can’t believe it’s true, you can smell the fresh air and hear the birds! \n You step outside and all your classmates are having a beer! \n They look at you and they shout you MADE IT!!! \n Have a beer, go home, sleep and do your labs! \033 ")
    else:
        print("You are now in the " + room["name"])
        linebreak()
        #first inquirer
        question1 = [
  inquirer.List('action',
                message="“\033[1;32;40m What would you like to do? \033 ",
                choices=['explore', 'examine', "dance", "chill", "look at your labs' backlog"],
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
                        message="“\033[1;32;40m What would you like to examine? \033 " ,
                        choices= [dic['name'] for dic in object_relations[game_state["current_room"]['name']]],
                        ), 
                ]
            answer = inquirer.prompt(question2)
            examine_action = answer['examine']
            examine_item(examine_action)
        elif intended_action == "dance" :
            print(" “\033[1;34;40m Congratulations, everyone finds your moves unintersting, you just made a fool out of yourself \033 ")
            play_room(room)
        elif intended_action == "chill" :
            print(" “\033[1;34;40m You decided to take a break but you remember that you need to go back to your computer to go finnish your Labs, you jump up \033 ")
            play_room(room)
        elif intended_action == "look at your labs' backlog" :
            print("“\033[1;34;40m You break down and start to cry compulsively, you need to leave this room and go back to work ASAP \033 ")
            play_room(room)
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
                    print("“\033[1;35;40m You use the key. The door didin't open. A message appears: \033" )
                    linebreak()
                    
                    if(item["name"] == "door_a"):

                        answer_a = inquirer.prompt(question_a)
                        answer_question_a = answer_a['question_a']

                        if answer_question_a == 'Clone' :    
                            next_room = get_next_room_of_door(item, current_room)
                            output = item['message']

                        else:
                            output = "“\033[1;31;40m Sorry Try Again \033 ”)"
                    
                    if(item["name"] == "door_b"):
                        
                        answer_b = inquirer.prompt(question_b)
                        answer_question_b = answer_b['question_b']
                        
                        if answer_question_b == '#- print([i for i in range(10)]' :    
                            next_room = get_next_room_of_door(item, current_room)
                            output = item['message']
                        else:
                            output = "“\033[1;31;40m Sorry Try Again \033 ”)"
                    
                    if(item["name"] == "door_c"):
                    
                        answer_c = inquirer.prompt(question_c)
                        answer_question_c = answer_c['question_c']
                    
                        if answer_question_c == 'str.lower()' : 
                            next_room = get_next_room_of_door(item, current_room)
                            output = item['message']
                        else:
                            output = "“\033[1;31;40m Sorry Try Again \033 ”)"
                    
                    if(item["name"] == "door_d"):
                    
                        answer_d = inquirer.prompt(question_d)
                        answer_question_d = answer_d['question_d']
                    
                        if answer_question_d == 'No' :    
                            next_room = get_next_room_of_door(item, current_room)
                            output = item['message']
                        else:
                            output = "Sorry try again"
                    

                else:
                    output += "“\033[1;31;40m It is locked but you don't have the key. \033 "
            
            elif(item['type'] == 'teacher'):
                output = item['message']
            
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += item['message'] + " You find " + item_found["name"] + "."
                else:
                    output += "“\033[1;33;40m There isn't anything interesting about it. But you've found the key already \033 "
            print(output)
            linebreak()
            break

    if(output is None):
        print("The item you requested is not found in the current room.")


    if (next_room) and inquirer.prompt(question_yn)['yes/no'] == 'yes': 
        play_room(next_room)
    else:
        play_room(current_room)


# In[ ]:


game_state = INIT_GAME_STATE.copy()

start_game()

