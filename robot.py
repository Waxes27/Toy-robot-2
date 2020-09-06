import sys
def name_of_the_robot():
    name =  input("What do you want to name your robot? ")
    return name


def help_(command, yaxis, xaxis,coords, name):
    command_list = ["OFF  - Shut down robot",
    "HELP - provide information about commands",
    "FORWARD - Moves robot forward",
    "BACK - Moves robot backwards",
    "LEFT - Turns the robot to  the left",
    "RIGHT - Turns the robot to the right"]
    print("I can understyand these commands:")
    for commands in command_list:
        print(commands)
    command = user_command(name)
    command_switcher(command, yaxis, xaxis,coords, name)
    

def command_switcher(command, yaxis, xaxis,coords, name):
    commands = ["off", "help", "forward", "back", "left", "right"]
    
    if "forward" in command:
        movement(command, yaxis, xaxis, coords,name)
    if "back" in command:
        movement(command, yaxis, xaxis, coords,name)
    if "left" in command:
        movement(command, yaxis, xaxis, coords,name)
    if "right" in command:
        movement(command, yaxis, xaxis, coords,name)
    
    if command == "help":
        help_(command, yaxis, xaxis,coords, name)

    while command != "off" and command in commands:
        command = user_command(name)
    if command == "off":
        print("Shutting down..")
        return
    
    while command not in commands:
        print("Sorry I did not understand '{}'. ".format(command))
        command = user_command(name).lower()
        command_switcher(command, yaxis, xaxis,coords, name)


def movement(command, yaxis, xaxis,coords,name):
    north_south = True
    east_west = False


    if command == "forward" and north_south is True:
        command, steps = command.split()
        yaxis = yaxis + int(steps)
        coords = (xaxis, yaxis)
        print("> {} moved forward by {} steps".format(name,steps))
        print("> {} is now at {}".format(name, coords))
        command = user_command(name).lower()
        result_switcher = command_switcher(command, yaxis, xaxis, coords, name)
    if command == "back":
        command, steps = command.split()
        yaxis = yaxis - int(steps)
        coords = (xaxis, yaxis)
        print("> {} moved forward by {} steps".format(name,steps))
        print("> {} is now at {}".format(name, coords))
        command = user_command(name).lower()
        result_switcher = command_switcher(command, yaxis, xaxis, coords, name)
    if command == "left":
        print("> {} turned left.".format(name))

        if north_south is True:
            north_south = False
            east_west = True
        else:
            north_south = True
            east_west = False




def user_command(name):
    return input("{}: what must I do next? ".format(name)).lower()

def robot_start():
    commands = ["off", "help", "forward", "back", "left", "right"]
    name = name_of_the_robot()

    yaxis = 0
    xaxis = 0
    coords = (xaxis, yaxis)

    print("Hello kiddo!")

    command = user_command(name).lower()
    while True:
        result_switcher = command_switcher(command, yaxis, xaxis, coords, name)
        break
    



if __name__ == "__main__":

    robot_start()

