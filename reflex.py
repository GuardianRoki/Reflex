import keyboard
import os
import time
# import datatime
import random

def main():

    # List with all letters & variable to store a randomly selected letter
    keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    key = keys[random.randint(0, len(keys)-1)]
    inittop10List = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    top10List = inittop10List
    test = True

    while test == True:
       print("\nLetters are capatalized for reading convenience.\n")
       file = open("reflex.txt", "r")

       print(f"The reaction times in the Top 10 are : {file.read()}")
       file.close()

       # Countdown Timer
       print("Your test begins on 1.\n")

       for i in range(5,0,-1):
            time.sleep(1)
            print(i)
       # Key match & reaction time recorder
       print(f"Match the key - {key}\n")
       start_time = time.time()
       reception = keyboard.wait(key.lower())
       end_time = time.time()

       reaction_time = end_time - start_time
       print(f"Your reaction time is {reaction_time}")
       # Everything above this point works fine
       for i in range(0, len(top10List)):

            if reaction_time < top10List[i]:

                top10List[i] = reaction_time
                break

       # Top 10 upload & recorder
       file = open("reflex.txt", "w")

       if reaction_time in top10List:

            print("\nCongratulations! you made the top 10.")
            name = input("\nEnter your name: ")
            grad = int(input("\nEnter your graduation year: "))
            file.writelines(f"* Reaction Time: {reaction_time} | Name: {name} | Graduation Year: {grad} *")

       else:
        
            print("\nNice Try! Unfortunately, you did not make top 10.\n")
    
       file.close()
            
       repeat = input("Would you like to try again? (Y/N): ")

       if repeat.capitalize() == "N" or repeat.capitalize() == "NO" or repeat.capitalize() == "NAH":
            test = False
            quit()
       elif repeat.capitalize() == "Y" or repeat.capitalize() == "YES":
            test = True
            continue
       else:
            
            while repeat.capitalize() != "N" or repeat.capitalize() != "Y" or repeat.capitalize() != "NO" or repeat.capitalize() != "YES" or repeat.capitalize() != "NAH":
                print("\nPlease enter a valid input.")
                repeat = input("\nWould you like to try again? (Y/N): ")


main()


