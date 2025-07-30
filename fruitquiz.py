import random

class FruitQuiz:
    #create a constructor
    def __init__(self):
        #create a dicitonary of fruits as keys and color as values
        self.fruits={'apple': 'red',
                     
                     'orange':'orange',
                     'watermelon' : 'green',
                     'banana' : 'yellow'
        }
        
        #function for the quiz
        
    def quiz(self):
         while(True):
                
            fruit, color = random.choice(list(self.fruits.items()))
            print("What is the color of {}".format(fruit))
                
            user_answer = input()
                
            if(user_answer.lower() == color):
                print("Correct answer")
                    
            else:
                print("Wrong answer")
                    
            option = int(input("Enter 0,if you want to play again, otherwise enter 1: "))
            if(option):
                break
                
print("Welcome to fruit quuiz")
fq = FruitQuiz()
fq.quiz()