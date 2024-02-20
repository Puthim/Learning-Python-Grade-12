todo = []

def printer():
    print(todo)

def add(name):
    todo.append(name)

def dis():
    ind = input('please write your list: ')
    return ind

def dis2():
    ind = input('please remove your list: ')
    return ind
def remove(name):
    todo.remove(name)

#use int(input()) to make input an integer
while True:
    command = input("Use 1 to add to list, 2 to remove from list, 3 to view all lists, and \"q\" to exit the program: ")
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
        print("goodbye")
        break
    else: 
        print("you wrote the wrong command")