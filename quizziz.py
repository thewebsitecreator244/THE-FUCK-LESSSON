import random
import os
import time


score = 0
questions = [
    "which function allows you to get information from the console?",
    "which method allows you to add a list into another list",
    "What do you use to start a comment in Python?",
    "Which of the following is a valid way to print “Hello, World!” in Python?",
    "What is the output of the following Python code snippet: print(1 + 1)?"

]
answers = [
    "(a)print,(b)input,(c)int",
    "(a)extend,(b)insert,(c)append",
    "(a)//,(b)/*,(c)#",
    "(a) print(Hello world),(b)echo Hello world,(c)printf""(Hello, World!)",
    "(a)11,(b)2,(c)Error"

]
correct_answers = ["b", "a", "c", "a", "b"]
random_pool=[0,1,2,3,4]
input("welcome to quizziz press ENTER to continue")
while len(random_pool)>0:
    random_pool_Choice= random.choice(random_pool)
    random_pool.remove(random_pool_Choice)
    print(questions[random_pool_Choice])
    print(answers[random_pool_Choice])
    if input("enter letter without (): ") == correct_answers[random_pool_Choice]:
        print(f"congrats the answer was {correct_answers[random_pool_Choice]}")
        score+=1
        print(f"your score is now {score}")
    else:
        print(f"too bad the answer was {correct_answers[random_pool_Choice]}")
        print(f"your score remains {score}")
    time.sleep(2)
    os.system('cls')
if score >= 3:
    print("you're a pro in python")
elif score >= 1:
    print("you still need to learn a bit")
else:
    print("you need to take python classes")
input("press enter to close the program")


