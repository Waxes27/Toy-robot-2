
PosNeg = 1

def name_of_the_robot():
    name = input("What do you want to name your robot? ")
    return name

def command_switcher(command, yaxis, xaxis,coords, name, direction):
    if len(command) == 2:
        command, steps = command
        steps = int(steps)
        if steps > 200:
            coords = (str(xaxis)+","+str(yaxis))
            print("{}: Sorry, I cannot go outside my safe zone.".format(name))
            print(" > {} now at position ({})".format(name,coords))
            return
            
    if "forward" in command:
        print(" > {} moved forward by {} steps.".format(name,steps))
        movement(command,yaxis,xaxis,coords,name, steps, direction)
        return  
    if "back" in command:
        print(" > {} moved back by {} steps.".format(name,steps))
        movement(command,yaxis,xaxis,coords,name, steps, direction)
        return        
    if "left" in command:
        direction = left(name, direction, coords, yaxis, xaxis)
        return direction
            
    if "right" in command:
        direction = right(name, direction, coords, yaxis, xaxis)
        return direction
            

def left(name,direction,coords, yaxis, xaxis):
    coord = (str(xaxis)+","+str(yaxis))
    print(" > {} turned left.".format(name))
    print(" > {} now at position {}.".format(name,coords))
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
    #direction = "east"
    if "forward" in command and direction == "north":
        yaxis = yaxis + steps
        coord = (str(xaxis)+","+str(yaxis))
        print(" > {} now at position ({}).".format(name, coord))

    if "forward" in command and direction == "east":
        xaxis = xaxis + steps
        coord = (str(xaxis)+","+str(yaxis))
        print(" > {} now at position ({}).".format(name, coord))

    if "forward" in command and direction == "south":
        yaxis = yaxis - steps
        coord = (str(xaxis)+","+str(yaxis))
        print(" > {} now at position ({}).".format(name, coord))
    
    if "forward" in command and direction == "west":
        xaxis = xaxis - steps
        coord = (str(xaxis)+","+str(yaxis))
        print(" > {} now at position ({}).".format(name, coord))
    


    if "back" in command and direction == "north":
        yaxis = yaxis - steps
        coord = (str(xaxis)+","+str(yaxis))
        print(" > {} now at position ({}).".format(name, coord))

    if "back" in command and direction == "east":
        xaxis = xaxis - steps
        coord = (str(xaxis)+","+str(yaxis))
        print(" > {} now at position ({}).".format(name, coord))

    if "back" in command and direction == "south":
        yaxis = yaxis + steps
        coord = (str(xaxis)+","+str(yaxis))
        print(" > {} now at position ({}).".format(name, coord))
    
    if "back" in command and direction == "west":
        xaxis = xaxis + steps
        coord = (str(xaxis)+","+str(yaxis))
        print(" > {} now at position ({}).".format(name, coord))


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
    commands = ["off","help","forward","back","left","right"]
    directions = ["forward","back","left","right"]
    name =  name_of_the_robot()

    print("{}: Hello kiddo!".format(name))

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
            command_switcher(command, yaxis, xaxis, coords, name, direction)
            command = user_command(name)
            continue
        
        elif "back" in command:
            command_switcher(command, yaxis, xaxis, coords, name, direction)
            command = user_command(name)
            continue

        elif "left" in command:
            direction = left(name, direction, coords, yaxis,xaxis)
            command_switcher(command, yaxis, xaxis, coords, name, direction)
            command = user_command(name)
            continue

        elif "right" in command:
            direction = right(name, direction, coords, yaxis,xaxis)
            #command_switcher(command, yaxis, xaxis, coords, name, direction)
            command = user_command(name)
            continue


        break
            
    

if __name__ == "__main__":

    robot_start()
