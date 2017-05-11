import random

def menu():
    #Request user numbers
    usernumbers = getnumbers()
    
    #Generate lottery numbers
    lotteryvalues = lotterynumbers()
    
    #Print out winnings
    matchednumbers = usernumbers.intersection(lotteryvalues)
    print("You matched {}. You won ${}!".format(matchednumbers, 100 ** len(matchednumbers)))

        
#User picks 6 numbers
def getnumbers():
    user_csv = input("Enter 6 numbers between 1 and 20, separated by commas: ")
    user_list = user_csv.split(",")
    user_intset = {int(number) for number in user_list}
    return user_intset

#Lottery generates 6 random numbers between 1 and 20
def lotterynumbers():
    values = set()
    while len(values) < 6:
        values.add(random.randint(1, 20))
    return values

menu()




        
