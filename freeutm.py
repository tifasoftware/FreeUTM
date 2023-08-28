import curses
import os
import create_machine
#stdscr = curses.initscr()

def capture():
    #stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    #stdscr.keypad(True)

def release():
    curses.nocbreak()
    #stdscr.keypad(False)
    curses.echo()
    curses.endwin()


def appliance_list():
    print ("Appliances:")
    for file in os.listdir(os.getcwd()):
        if (os.path.isdir(os.getcwd() + "/" + file) == True):
            print (file)

    print()

appliance_list()

gotMachine = False
machine = ""
while (machine != ":q"):
    print("Select Appliance or Command (:h for help): ")
    machine = input()
    if (os.path.isdir(os.getcwd() + "/" + machine) == True):
        print()
        print("Machine: " + machine)
        choice = ""
        while (choice != "C"):
            choice = input("(R)un, (E)dit, or (C)ancel: ")
            if (choice.upper() == "R"):
                create_machine.runMachine(machine)
            elif (choice.upper() == "E" or choice.upper() == "EE" or choice.upper() == "EN"):
                choice2 = ""
                if (choice == "E"):
                    choice2 = input("(E)dit Config, Create (N)ew Hard Drive, or (C)ancel: ")
                    
                if (choice ==  "EE" or choice2 == "E"):
                    create_machine.editConfig(machine)

                elif (choice == "EN" or choice2 == "N"):
                    hdname = create_machine.create_hdd(machine)
                    print("New Hard Drive FileName is: " + hdname)
    elif (machine == ":q"):
        print ("Quitting")
    elif (machine == ":h"):
        print (":q - Quit")
        print (":l - List")
        print (":n - New")
        print (":h - Help (this)")
    elif (machine == ":l"):
        appliance_list()
    elif (machine == ":n"):
        create_machine("")
    elif (machine == ":q"):
        break
    else:
        print("Appliance Doesn't Exist or Invalid Command")
    

        



