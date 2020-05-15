from room import Room
from player import Player
from world import World

import random
from ast import literal_eval
from util import Stack

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


# dictionary to keep track of exits in each room:
room_dict ={}
# directional moves made:
traversal_path = []

# reverse directions when need to backtrack
rev_dir = {
                'n':'s',
                's':'n',
                'e':'w',
                'w':'e'
}


s = Stack()
# begin in starting room:
s.push([player.current_room.id])
print(f'starting ROOM {player.current_room.id}')
prev_room = None
curr_room = player.current_room.id
direction = None
# repeat until queue is empty
while s.size() > 0:
    path = s.pop()
    curr_room = path[-1]
    print(f'{curr_room}')
    if curr_room not in room_dict:
        print(f'check after {curr_room}')
        room_dict[curr_room] = {}
        exits = player.current_room.get_exits()
        print(f'exits {exits}')
        for dir in exits:
            room_dict[curr_room][dir] = '?'
            print(f'after adding exits {room_dict}')
            if room_dict[curr_room][dir] == '?':
                player.travel(dir)
                prev_room = curr_room
                print(f'prev_room = {curr_room}')
                curr_room = player.current_room.id
                print(f'curr_room = {curr_room}')
                direction = dir
                print(f'direction = {dir}')
                room_dict[prev_room][dir] = curr_room
                # room_dict[curr_room][rev_dir[exit]] = prev_room
                # print(f'dict after update {room_dict}')
                traversal_path.append(direction)
                print(f't path {traversal_path}')
                s.push(path + [curr_room])
            else:
                player.travel(rev_dir[dir])

        # exits for current room:
        # for exit in exits:
            # room_dict[last_room][exit] = None
            # if room_dict[last_room][exit] is None:
            #     player.travel(random.choice(exit))
            #     room_dict[last_room][exit] == player.current_room.id
            #     print(f'dict {room_dict}')


    # print(f'exits {exits}')
    # print(room_dict)
    # for each direction in room:
    # for dir in exits:
    # create dictionary entry for room exits if not there:
    # if bool(room_dict[player.current_room.id]) is False:
    #     room_dict[player.current_room.id][exits] = None
    # print(room_dict)
        # if dir not in room_dict[player.current_room.id]:
        #     room_dict[player.current_room.id][dir] = None
        #     print(f'dict {room_dict}')
        # if room_dict[player.current_room.id][dir] is None:
        #     player.travel(dir)
        #     traversal_path.append(dir)
        #     room_dict[last_room][dir] = player.current_room.id
        #     s.push(path + [player.current_room.id])
        #     print(f't path {traversal_path}')
        #     print(f'room after move {player.current_room.id}')
            # for next_exit in player.current_room.get_exits():
            #     if room_dict[player.current_room.id][dir] is None:
            #         player.travel(next_exit)
            #         s.push(path + [player.current_room.id])
            #         print(f'path after push {path}')
            #         print(f'next exit {next_exit}')
            #         print(f'dict3 {room_dict}')
        # else:
        #     travel_back(dir)
'''
Start at starting room 0
get exits for room
    if room is unvisited, add exits to room dictionary
    choose 1 direction to go
        move player
        add room id to room dict for that direction
    if room is visited:
        if there are unvisited exits:
            move player that direction
            add room id to room dict for that direction
        if no unvisited exits:
            move backward

'''


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
