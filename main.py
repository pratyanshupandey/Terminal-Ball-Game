from screen import *
import playsound
import os
path = "sad_trom.m4a"
# os.system("ffplay -nodisp -autoexit -loglevel quiet " + path + " &")
os.system("aplay -q taunt.wav > /dev/null &")
while True:

    print("\nIN GAME INSTRUCTIONS")
    print("a for moving paddle left")
    print("d for moving paddle right")
    print("x for launching the ball")
    print("READ THE README BEFORE FOR MORE DETAILS\n\n")

    print("START INSTRUCTIONS")
    print("p for starting the game")
    print("q for exiting the game")

    val = input("Option: ")
    if val == 'p':
            Game.run_game()
    elif val == 'q':
        break
    else:
        print("Invalid Input")
