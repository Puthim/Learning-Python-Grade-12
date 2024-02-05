# file name quiz_app.py
# input is used to ask questions
name = input('what is your name?')
monouk = "what is your name?"
print("Hello!", name)
#when it runs and you interact with the terminal what you input will come with an answer
question = input("2 + 2?")

total_point = 0

if question == "4":
    total_point = total_point + 1
    print("correct")
else: 
    print("wrong")
#there is a difference between = == and ===
#indentation is part of the line of code
