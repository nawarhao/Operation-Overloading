#python program to overload equality
#and less than operators

class A:
    def __init__(self, a):
        self.a = a
    def __lt__(self, other):
        if(self.a<other.a):
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"
        
    def __eq__(self, other):
        if(self.a == other.a):
            return "Both are equal"
        else:
            return "Not equal"
        

ob1 = A(2)
ob2 = A(3)
print("passed values:", ob1.a, ob2.a)
print(ob1<ob2)

ob3 = A(4)
ob4 = A(4)
print("passed values:", ob3.a, ob4.a)
print(ob3 == ob4)

#Activity 2

class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        
        #we will return a string
        return self.word+'('+self.meaning+')'
flash = []
print("Welcome to flashcard application")

#the following loop will be repeated until user stops to add the flashcards
while(True):
    word = input("enter the name you want to add to flashcard:")
    meaning = input("enter the meaning of the word")
    
    flash.append(flashcard(word, meaning))
    option = int(input("enter 0, if you want to add another flashcard otherwise enter 1: "))
    
    if(option):
        break

#printing all the flashcards
print("\nYour flashcards")
for i in flash:
    print(">", i)