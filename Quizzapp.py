name = input("please write your name: ")
print(f"Hello, {name} please proceed with the test.")

total_point = 0

q1 = input("give a name for a red fruit? ")
if q1.lower() == "apple": #you can also use .casefold() instead of .lower or .upper
    total_point = total_point + 1
    print("correct")
else: 
    print("you are wrong")

q2 = input("What country are we in right now? ")
if q2.lower() == "cambodia":
    total_point = total_point + 1
    print("correct")
else: 
    print("you are wrong")

q3 = input("What class are we in right now? ")
if q3.lower() == "computer":
    total_point = total_point + 1
    print("correct")
else: 
    print("you are wrong")

q4 = input("What is the color of your tie? ")
if q4.lower() == "red":
    total_point = total_point + 1
    print("correct")
else: 
    print("you are wrong")

q5 = input("What is the color of your shirt? ")
if q5.lower() == "white":
    total_point = total_point + 1
    print("correct")
else: 
    print("you are wrong")

print(total_point/5*100,"%")