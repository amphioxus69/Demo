# welcome to pig dice game

import random
import time



def SCOREBOARD():
  time.sleep(1)
  print("\n\t\t\t\t\t\t\tSCOREBOARD\n\t\t\t\t\t\t\t==========")
  for i in range(n):
    print("\t\t\t\t\t\t\t  ", names[i], ":", scores[i])


def abcd(j, k):
  print()
  time.sleep(1)
  print(j, " is choosing.... ", end="")
  chu = int(input())
  sum = 0

  while (True):

    roll = random.randint(1, 6)
    
    print("rolling dice....\n")
    time.sleep(1)
    
    print("You rolled : ", roll)
    time.sleep(1)
    print("You chose : ", chu)
    print()
    if chu == roll:
      time.sleep(1)
      print("\t\t[unlucky]\n")
      return 0

    sum += roll

    if sum + scores[k] >= 10:
      return sum

    time.sleep(1)

    

    print("Wanna go on?.... : ", end="")
    x = input()

    if x == "\n":
      continue
    elif x == "n":
      return sum


print("\t\t\t\t\t\t\tPIG DICE")
print("\t\t\t\t\t\t\t========\n")

n = int(input("\t\t\t\t\tNumber of Players : "))
if n < 2:
  time.sleep(1)
  print("\n\t\t\t\t\tMake more friends :)")
  exit()
  
names = []
print("\n\t\t\t\t\t\tEnter Player Names")
print("\t\t\t\t\t\t==================\n")
for i in range(n):
  print("\t\t\t\t\tPlayer", i + 1, " : ", end="")
  names.append(input())

scores = []
for i in range(n):
  scores.append(0)

while (True):
  for j in range(n):
    scores[j] += abcd(names[j], j)

    for i in scores:
      if i >= 10:
        ind = scores.index(i)
        time.sleep(2)
        print("\n\n\t\t\t\t  ......[", names[ind], "IS THE WINNER]......\n\n")
        time.sleep(1)
        SCOREBOARD()
        exit()

    SCOREBOARD()



