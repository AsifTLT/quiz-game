print("welcome to my computer quiz! ")

playing = input("do you want to play? ")

if playing.lower() != "yes":
    quit()
print("Okey, Let's play")
score = 0

answer = input(" what does CPU stand for? :  ") 
if answer.lower() == "central processing unit":
    print("correct answer")
    score += 1
    
else:
    print("wrong answer") 
# -----------------------------------------    
       
answer = input(" what does GPU stand for? :  ") 
if answer.lower() == "graphics processing unit":
    print("correct answer")
    score += 1
else:
    print("wrong answer")
# -----------------------------------------            
       
answer = input(" what does RAM stand for? :  ") 
if answer.lower() == "random access memory":
    print("correct answer")
    score += 1
else:
    print("wrong answer")
# -----------------------------------------    
      
answer = input(" what does PSU Stand for? :  ") 
if answer.lower() == "power supply unit":
    print("correct answer")
    score += 1
else:
    print("wrong answer")

print("You got  " + str(score)  +  "questions correct" )    
print("You got  " + str((score / 4) * 100)  +  "%." )    