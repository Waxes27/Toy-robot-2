def safe_zone(name,coords):
    """incomplete"""
    print("{}: Sorry, I cannot go outside my safe zone.".format(name))
    print(" > {} now at position {}.".format(name,coords))
    return


def sprint(command, name,coords,xaxis,yaxis,direction):
    command,steps = command
    coords = (str(xaxis)+","+str("15"))
    for i in reversed(range(int(steps))):
        print(" > {} moved forward by {} steps.".format(name,(i+1)))
    print(" > {} now at position ({}).".format(name,coords))
    return coords


def name_of_the_robot():
    return input("What do you want to name your robot? ")


def command_switcher(command, yaxis, xaxis,coords, name, direction):
    command,steps = command
    steps = int(steps)
    if "forward" in command:
        print(" > {} moved forward by {} steps.".format(name,steps))
        xaxis,yaxis = movement(command,yaxis,xaxis,coords,name, steps, direction)
        #print(xaxis)
        if xaxis in range(-100,100) and yaxis in range (-200,200):
            return xaxis,yaxis
        else:
            safe_zone(name,coords)
        return xaxis, yaxis

    elif "back" in command:
        print(" > {} moved back by {} steps.".format(name,steps))
        movement(command,yaxis,xaxis,coords,name, steps, direction)
        return        
    elif "left" in command:
        direction = left(name, direction, coords, yaxis, xaxis)
        return direction            
    elif "right" in command:
        direction = right(name, direction, coords, yaxis, xaxis)
        return direction
            

def left(name,direction,coords, yaxis, xaxis):
    coord = (str(xaxis)+","+str(yaxis))
    print(" > {} turned left.".format(name))
    print(" > {} now at position ({}).".format(name,coord))
    if direction == "north":
        direction = "west"
    elif direction == "west":
        direction = "south"
    elif direction =="south":
        direction = "east"
    elif direction == "east":
        direction = "north"
    return direction


def right(name, direction, coords, yaxis, xaxis):
    coord = (str(xaxis)+","+str(yaxis))
    print(" > {} turned right.".format(name))
    print(" > {} now at position ({}).".format(name, coord))
    if direction == "north":
        direction = "east"
    elif direction == "west":
        direction = "north"
    elif direction =="south":
        direction = "west"
    elif direction == "east":
        direction = "south"
    return direction


def movement(command, yaxis, xaxis,coords,name,steps,direction):
    if "forward" in command and direction == "north":
        yaxis = yaxis + steps
        coord = (str(xaxis)+","+str(yaxis))
        print(" > {} now at position ({}).".format(name, coord))
        return xaxis,yaxis

    if "forward" in command and direction == "east":
        xaxis = xaxis + steps
        coord = (str(xaxis)+","+str(yaxis))
        print(" > {} now at position ({}).".format(name, coord))
        return xaxis,yaxis

    if "forward" in command and direction == "south":
        yaxis = yaxis - steps
        coord = (str(xaxis)+","+str(yaxis))
        print(" > {} now at position ({}).".format(name, coord))
        return xaxis,yaxis
    
    if "forward" in command and direction == "west":
        xaxis = xaxis - steps
        if xaxis  in range(-100,100):
            coord = (str(xaxis)+","+str(yaxis))
            print(" > {} now at position ({}).".format(name, coord))
        else:
            safe_zone(name,coords)
        return xaxis,yaxis
    
    if "back" in command and direction == "north":
        yaxis = yaxis - steps
        coord = (str(xaxis)+","+str(yaxis))
        print(" > {} now at position ({}).".format(name, coord))
        return xaxis,yaxis

    if "back" in command and direction == "east":
        xaxis = xaxis - steps
        coord = (str(xaxis)+","+str(yaxis))
        print(" > {} now at position ({}).".format(name, coord))
        return xaxis,yaxis

    if "back" in command and direction == "south":
        yaxis = yaxis + steps
        coord = (str(xaxis)+","+str(yaxis))
        print(" > {} now at position ({}).".format(name, coord))
        return xaxis,yaxis
    
    if "back" in command and direction == "west":
        xaxis = xaxis + steps
        coord = (str(xaxis)+","+str(yaxis))
        print(" > {} now at position ({}).".format(name, coord))
        return xaxis,yaxis


def help_():
    commands = ["OFF  - Shut down robot","HELP - provide information about commands",
    "FORWARD - Moves the robot forward"]
    print("I can understand these commands:")
    for command in commands:
        print(command)
    return


def off(name):
    print("{}: Shutting down..".format(name))
    return off is True


def user_command(name):
    command = input("{}: What must I do next? ".format(name))
    return command


def sorry(name, command, commands, command1):
    if command not in commands:
        print("{}: Sorry, I did not understand '{}'.".format(name,command1))


def robot_start():
    direction = "north"
    xaxis = 0
    yaxis = 0
    coords = (xaxis, yaxis)
    robot_on = True
    commands = ["off","help","forward","back","left","right","sprint"]
    name =  name_of_the_robot()
    while len(name) == 0:
        name =  name_of_the_robot()
    print("{}: Hello kiddo!".format(name))
    command = user_command(name)
    while len(command) == 0:
        command = user_command(name)
    while robot_on == True:
        command1 = command
        command = command.lower().split()
        while command[0] not in commands:
            sorry(name, command, commands, command1)
            command[0] = user_command(name)
            
        if "off" in command:
            off(name)
            robot_on = False

        elif "help" in command:
            help_()
            command = user_command(name)
            continue
        
        elif "forward" in command:
            xaxis,yaxis = command_switcher(command, yaxis, xaxis, coords, name, direction)
            command = user_command(name)
            continue
        
        elif "back" in command:
            command_switcher(command, yaxis, xaxis, coords, name, direction)
            command = user_command(name)
            continue
            
        elif "left" in command:
            direction = left(name, direction, coords, yaxis,xaxis)
            command = user_command(name)
            continue

        elif "right" in command:
            direction = right(name, direction, coords, yaxis,xaxis)
            command = user_command(name)
            continue
        
        elif "sprint" in command:
            coords = sprint(command, name,coords,xaxis,yaxis,direction)
            command = user_command(name)
            continue

        break           
if __name__ == "__main__":
    robot_start()