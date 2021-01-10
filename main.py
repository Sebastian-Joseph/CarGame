command = ""

while command.lower() != 'quit':
    command = input("> ")
    if command.lower() == 'start':
        print("Car started...")
    elif command.lower() == 'stop':
        print('Car stopped...')
    elif command.lower() == 'help':
        print("""
        start - starts car
        stop - stops car
        quit - quits game
        """)
    elif command.lower() == 'quit':
        break
    else:
        print("Don't understand")