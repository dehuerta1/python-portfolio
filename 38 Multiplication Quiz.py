#Multiplication Quiz

#Init
import random


#Function
def mathQuiz():
    print("Hello student and prepare to take the math quiz!")
    global score
    score = 0
    for i in range(5):
        print(f"Question {i + 1} of 5")
        number1 = random.randint(1,10)
        number2 = random.randint(1,10)
        answer = number1 * number2
        print("What is " + str(number1) + " x " + str(number2))
        studentanswer = int(input("What is " + str(number1) + " x " + str(number2)))
        print("The correct answer was " + str(answer))
        if studentanswer == answer:
            print("You are correct!")
            score = score + 1
        else:
            print("You are incorrect!")
            score = score + 0
            print("Current score: " + str(score) + " out of 5")
    print("Final Score: " + str(score) + " out of 5")



#Main
mathQuiz()
