print("WELCOME TO MY QUIZ GAME!!!!!")

playing=input("Would you like to play the game ?  ")

if playing.lower()!="yes":
    quit()

print("Okay lets play!!!")
score=0
answer=input("What does CPU stand for ? ")
if answer.lower()=="central processing unit":
    print("CORRECT!!!")
    score+=1
else:
    print("INCORRECT")


answer=input("What does RAM stand for ? ")
if answer.lower()=="random access memory":
    print("CORRECT!!!")
    score+=1
else:
    print("INCORRECT")


answer=input("What does PSU stand for ? ")
if answer.lower()=="power supply":
    print("CORRECT!!!")
    score+=1
else:
    print("INCORRECT")


answer=input("What does GPU stand for ? ")
if answer.lower()=="graphics processing unit":
    print("CORRECT!!!")
    score+=1
else:
    print("INCORRECT")


print("you got " + str(score) + " questions correct. ")
print("you got " + str((score/4)*100) + " %. ")