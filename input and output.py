name = input("Please write your name: ")
print("Welcome,",name,"I hope you can pass this test.")

total_point = 0 

question1 = input("What has to be broken before you can use it?")
if question1 == "an egg":
    total_point = total_point + 1
    print("wow we are of to a good start, on to the next question.")
else: 
    print("your answer is not really right.")

question2 = input("I\'m tall when I\'m young, and I\'m short when I\'m old. What am I?")
if question2 == "A candle":
    total_point = total_point + 1
    print("Genius")
else: 
    print("your answer is not really right.")

question3 = input("What can you break, even if you never pick it up or touch it?")
if question3 == "A promise":
    total_point = total_point + 1
    print("I've never seen anyone this smart")
else: 
    print("your answer is not really right.")

question4 = input("What is always in front of you but can\'t be seen?")
if question4 == "The future":
    total_point = total_point + 1
    print("you were born for this.")
else: 
    print("your answer is not really right.")

question5 = input("What is full of holes but still holds water?")
if question5 == "a Sponge":
    total_point = total_point + 1
    print("can you help me with my test?")
else: 
    print("your answer is not really right.")


total_point = total_point/6*100
if total_point > 60:
    print("you got ",total_point[0:4],"%. You did great")
else: 
    print("you got ",total_point[0:4], "%. Try harder next time")
