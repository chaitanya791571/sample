started = False

while True:
    command = input(">>")
    
    if (command == 'start'):
        if started:
            print("the car is already started")
        else:
            started = True
            print("started")
    elif (command == 'stop'):
        if not started:
            print("the car is already stopped")
        else:
            started = False
            print("the car is stopped")
    elif (command == 'help'):
        print('''
        start : to start the car
        stop : to stop the car
        quit : to quit the game
        ''')
    elif (command == 'quit'):
        print("quit")
        break
    else:
        print(" i dont understand")