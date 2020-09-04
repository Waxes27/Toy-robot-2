import sys
def name_of_the_robot():
    name =  input("What do you want to name your robot? ")
    return name


def help(name):
    print("I can understand these commands:\nOFF  - Shut down robot\nHELP - provide information about commands\n")

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
    


    while command != "off" and command in commands:
        command = user_command(name)
    if command == "off":
        print("Shutting down..")
        return
    if command == "help":
        help()

    while command not in commands:
        print("Sorry I did not understand '{}'. ".format(command))
        command = user_command(name).lower()
        command_switcher(command, yaxis, xaxis,coords, name)


def direction(command):
    cardinals = ["n", "s", "e", "w"]

    if command == "left" and cardinals:
        pass


def movement(command, yaxis, xaxis,coords,name):
    command, steps = command.split()

    if command == "forward":
        yaxis = yaxis + int(steps)
        coords = (xaxis, yaxis)
        print("> {} moved forward by {} steps".format(name,steps))
        print("> {} is now at {}".format(name, coords))
        command = user_command(name).lower()
        result_switcher = command_switcher(command, yaxis, xaxis, coords, name)
    if command == "back":
        yaxis = yaxis - int(steps)
        coords = (xaxis, yaxis)
        print("> {} moved forward by {} steps".format(name,steps))
        print("> {} is now at {}".format(name, coords))
        command = user_command(name).lower()
        result_switcher = command_switcher(command, yaxis, xaxis, coords, name)
    if command == "left":
        pass
        


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
