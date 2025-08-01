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