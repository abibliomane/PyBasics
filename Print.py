user = input("Please enter your age as a whole number: ") 
if user.isdigit():
          age = int(user)
          ageseconds = age * 365 * 24 * 60**2
          ageminutes = age * 365 * 24 * 60
          agedays = age * 365 * 24
          agemonths = age * 12
          print("Gosh, {} years!".format(int(user)))
          print(str(age) + " years is either " + str(agemonths) + " months, or " + str(agedays) + " days, or " + str(ageminutes) + " minutes, or " + str(ageseconds) + " seconds.")
          print("You have lived, in other words, for " + str(agemonths) + " months, which is " + str(agedays) + " days, or if you like " + str(ageminutes) + " minutes, that is to say " + str(ageseconds) + " seconds. Tired yet?")
else:
        print("That won't work, sorry! Try a whole number instead.")


    
