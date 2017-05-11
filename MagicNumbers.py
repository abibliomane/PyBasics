import random

magicnums = [random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)]


def askuserandchecknum():
    usernum = input("Enter a number between 0 and 10: ")
    if int(usernum) in magicnums:
        return "You have a magic number!"
    if int(usernum) not in magicnums:
        return "Sorry, that's not a magic number!"


def runprogramxtimes(chances):
    for attempt in range(chances): #range(chances) is [0,1,2]
        print("This is attempt {} of {}.".format(attempt + 1, chances))
        print(askuserandchecknum())
        

chances = int(input("How many attempts do you want?: "))
runprogramxtimes(chances)

    
