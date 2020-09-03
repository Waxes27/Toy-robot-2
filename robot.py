import sys
def name_of_the_robot():
    name = input("What do you want to name your robot? ")
    print("{}: Hello kiddo! ".format(name))
    return name


def get_command_input(name):
    command = input(f"{name}: What must I do next? ")
    return command.lower()

def off():
    print("Shutting down..")
    return

def help_menu():
    print("I can understand these commands:\nOFF  - Shut down robot")
    print("HELP - provide information about commands")
    
def movement(direction, steps, y_axis, x_axis,coords):

    if direction == "forward":
        y_axis = y_axis + steps
        print("this is {} by {} steps".format(direction, steps))
    elif direction == "back":
        y_axis = y_axis - steps
        print("this is {} by {} steps".format(direction, steps))
    elif direction == "left":
        x_axis = x_axis - steps
        print("this is {} by {} steps".format(direction, steps))
    elif direction == "right":
        x_axis = x_axis + steps
        print("this is {} by {} steps".format(direction, steps))
    coords = (x_axis,y_axis)
    print(coords)
    return coords




def command_handling(command,steps,x_axis,y_axis, coords):
        if "off" in command:
            off()
            return quit()
        if "help" in command:
            help_menu()
            print()
        if "forward" in command:
            direction = command
            coords = movement(direction,steps, x_axis, y_axis,coords)
        if "back" in command:
            direction = command
            coords = movement(direction,steps, x_axis, y_axis,coords)
        if "left" in command:
            direction = command
            coords = movement(direction,steps, x_axis, y_axis,coords)
        if "right" in command:
            direction = command
            coords = movement(direction,steps, x_axis, y_axis,coords)
            return coords

        
                 


        


def robot_start():
    x = 0
    y = 0
    coords = (x,y)

    commands = ["off","help", "forward","back", "left","right"]

    name = name_of_the_robot()
    command = get_command_input(name)
    command, steps = command.split()
    steps = int(steps)

    while command not in commands:
        print("Sorry I did not understand '{}'".format(command))
        command = get_command_input(name)

    while command is not "off":
        coords = command_handling(command, steps, x, y, coords)
        command = get_command_input(name)

    
        
    



if __name__ == "__main__":
    robot_start()
