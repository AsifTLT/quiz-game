print("welcome to my computer quiz! ")

playing = input("do you wnat to play? ")

if playing != "yes":
    quit()
print("Okey, Let's play")

answer = input("what does CPU stand for? :  ") 
if answer == "central processing unit":
    print("correct answer")
else:
    print("wrong answer")    