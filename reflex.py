import keyboard
import os
import time
from datetime import datetime
import random

def main():

    test = True

    while test == True:
       keys = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
       key = keys[random.randint(0, len(keys)-1)]
       initNameList = []
       initGradList = []

       
       top10List = []
       current_Time = datetime.now()

       print("\nLetters are capatalized for reading convenience. Answers are lowercase for speed\n")
       print(f"The current time is {current_Time}")
       
       file = open("reaction_scores.txt", "r")

       fileread = [line for line in file]
       print(f"The reaction times in the Top 10 are : {fileread}")
            
       file.close()

       test = False


       for x in fileread:
            while x[x.find(" ") + 1].isnumeric() == False:
                    x = x[x.find(" ") + 1:]
            x = x[x.find(" ") + 1:]
            x = x[0: x.find(" ")]
            top10List.append(x)
       print(top10List)
            
       
       # Countdown Timer
       print("Your test begins on 1.\n")

       for i in range(random.randint(2,5),0,-1):
            time.sleep(1)
            print(i)

       # Key match & reaction time recorder

       print(f"Match the key - {key}\n")

       start_time = time.time()

       keyboard.wait(key.lower())

       end_time = time.time()

       reaction_time = end_time - start_time
       print(f"Your reaction time is {reaction_time}")

       for i in range(0, len(top10List)):

            if reaction_time < top10List[i] or len(top10List) < 10:

                    top10List.insert(i, reaction_time)
                    print("\nCongratulations! you made the top 10.")
                    name = input("\nEnter your name: ")
                    grad = input("\nEnter your graduation year: ")
                    initNameList.append(name)
                    initGradList.append(grad)

                    file = open("reaction_scores.txt", "w")
                    for i in range (len(top10List)):
                         
                        file.write(f"Reaction time: {top10List[i]} | Name: {initNameList[i]} | Graduation year: {initGradList[i]}")

                    file.close()

                    break

            else:
        
                print("\nNice Try! Unfortunately, you did not make top 10.\n")
                break

       if len(top10List) > 10:
            while len(top10List) > 10:
                 top10List.pop(-1)

       if len(initNameList) > 10:
            while len(initNameList) > 10:
                 initNameList.pop(-1)
                 
       if len(initGradList) > 10:
            while len(initGradList) > 10:
                 initGradList.pop(-1)

       # Top 10 upload & recorder

            
       repeat = str(input("Would you like to try again? (Y/N): "))

       if repeat == "N" or repeat == "n":
            
            os.system('cls')
            
            file = open("reaction_scores.txt", "r")
            print(f"The reaction times in the Top 10 are : {file.read(-1)}")
            file.close()

            test = False
            quit()

       elif repeat == "Y" or repeat == "y":
            
            test = True
            continue
       else:
            
            print("\nPlease enter a valid input.")
            test = False
                


main()

