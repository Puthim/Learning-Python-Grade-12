todo = []

def printer():
    for i in todo:
        print(i)

def add(x):
    todo.append(x)

def dis():
    x = input('Add: ')
    return x

def dis2():
    x = input('Remove: ')
    return x

def remove(x):
    if x in todo:
        todo.remove(x)
    else:
        line()
        print("THIS ITEM IS NOT IN THE LIST!!!")

def line():
    print("-"*37)

def instructions():
    print('"q" => Quit the program.')
    print('"1" => Add to list.')
    print('"2" => Remove from list.')
    print('"3" => To view list.')

#use int(input()) to make input an integer
line()
instructions()

while True:
    line()
    command = input("Plesae input a command: ")
    line()
    if command == "1":
        add(dis())
        continue
    elif command == "2":
        remove(dis2())
        continue
    elif command == "3":
        printer()
        continue
    elif command == "q":
        print("Goodbye :)")
        break
    else: 
        print("YOU WROTE THE WRONG COMMAND!!!")
        line()
        print("Please instead use:")
        line()
        instructions()
#CRUD creat remove update and 
#use print("2"*20) to print 20 line of 2
