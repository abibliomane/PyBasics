user = input("Please enter your age as a whole number: ") 
if user.isdigit():
          age = int(user)
          ageseconds = age * 365 * 24 * 60**2
          ageminutes = age * 365 * 24 * 60
          agedays = age * 365 * 24
          agemonths = age * 12
          print("Gosh, {} years!".format(int(user)))
          print("{} years is either {} months, or {} days, or {} minutes, or {} seconds.".format(age, agemonths, agedays, ageminutes, ageseconds))
          print("You have lived, in other words, for {} seconds, which is {} minutes, or if you like {} days, that is to say {} months. Tired yet?".format(ageseconds, ageminutes, agedays, agemonths))
else:
        print("That won't work, sorry! Try a whole number instead.")


    
