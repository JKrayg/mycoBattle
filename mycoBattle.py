import cv2
import random
import time
from termcolor import colored


class goldenTeacher:
   name = "Golden Teacher"
   hp = 300
   hitPoints = 0
   taunt = "idiot! fool!"
   block = False
   onions = 0
 
  
class albinoAPlus:
   name = "Albino A+"
   hp = 325
   hitPoints = 0
   taunt = "trash!"
   block = False
   onions = 0


def playerBlock(blocker):
   blocker.block = True
   print(blocker.name + " blocked!")

   
def resetBlock(blocker):
   blocker.block = False


moveName = ["bopped", "shmacked", "dropped", "folded", "clapped"]
moveLog = ""


def playerAttack(attacker, attackee):
   if attacker.name == "Golden Teacher":
      if attackee.block == True:
         attacker.hitPoints = round(random.randint(40, 70) / 4, 2)
         attackee.hp = attackee.hp - attacker.hitPoints
      else:
         attacker.hitPoints = random.randint(40, 70)
         attackee.hp = attackee.hp - attacker.hitPoints
         attackee.onions = attackee.onions - 1
   elif attacker.name == "Albino A+":
      if attackee.block == True:
         attacker.hitPoints = round(random.randint(25, 85) / 4, 2)
         attackee.hp = attackee.hp - attacker.hitPoints
      else:
         attacker.hitPoints = random.randint(25, 85)
         attackee.hp = attackee.hp - attacker.hitPoints
         attackee.onions = attackee.onions - 1
   print("[*]" + attacker.name + " " + str(random.choice(moveName)) + " " + attackee.name + ":" + colored(" -" + str(attacker.hitPoints), 'red'))


def playerTaunt(taunter):
   taunter.onions = taunter.onions + 2
   print("[!]" + taunter.name + ": " + taunter.taunt)
      

print("Use the keys to battle the agent. Taunt to gain onions[(@]. Get hit and lose an onion.\nBlock to prevent losing onions and weaken the hit. Winner of the fight gets rewarded 2 onions.\nThe side with most onions at the end of the game wins.\n")

while goldenTeacher.hp > 0 and albinoAPlus.hp > 0:
   resetBlock(goldenTeacher)
   resetBlock(albinoAPlus)
   swung = False
   mycoUser = []
   possibleMoves = ["attack", "taunt", "block"]
   if moveLog == "attack":
      agentMeneuver = random.choices(possibleMoves, weights = [5, 5, 10], k = 1)
   else:
      agentMeneuver = random.choices(possibleMoves, weights = [10, 5, 5], k = 1)
      
   
   print("\n" + goldenTeacher.name + ": " + colored(str(round(goldenTeacher.hp, 2)), 'green') + " hp | (@ " + \
      colored(str(goldenTeacher.onions), 'yellow') + " onion(s)\n" + albinoAPlus.name + ": " + colored(str(round(albinoAPlus.hp, 2)), 'green') + " hp | (@ " + colored(str(albinoAPlus.onions), 'yellow') + " onion(s)\n")
   
   melee = input("Press 'q' to taunt, 'f' to block, or 'e' to attack! -> ")
   print("\nBATTLING...")
   time.sleep(1.5)
   
   if melee == "e":
      print("You Attacked!")
      swung = True
      moveLog = possibleMoves[0]
      # playerAttack(goldenTeacher, albinoAPlus)
   elif melee == "q":
      print("You Taunted!")
      playerTaunt(goldenTeacher)
      moveLog = possibleMoves[1]
   elif melee == "f":
      print("You Blocked!")
      playerBlock(goldenTeacher)
      moveLog = possibleMoves[2]
   else:
     print("ERRRORRR!!")
     break


   time.sleep(1)
   print("Albino A+ " + agentMeneuver[0] + "s!")
   time.sleep(1)
   

   # player block is too late to block the agents attack ----------------------------------[FIXED]
   print("________________RESULTS_________________")
   if agentMeneuver == ["attack"]:
      if swung == True:
         playerAttack(goldenTeacher, albinoAPlus)
         # time.sleep(1)
      playerAttack(albinoAPlus, goldenTeacher)
   elif agentMeneuver == ["taunt"]:
      if swung == True:
         playerAttack(goldenTeacher, albinoAPlus)
      playerTaunt(albinoAPlus)
   elif agentMeneuver == ["block"]:
      if swung == True:
         playerBlock(albinoAPlus)
         playerAttack(goldenTeacher, albinoAPlus)


if goldenTeacher.hp <= albinoAPlus.hp:
   albinoAPlus.onions = albinoAPlus.onions + 2
elif albinoAPlus.hp <= goldenTeacher.hp:
   goldenTeacher.onions = goldenTeacher.onions + 2

    
if albinoAPlus.onions == goldenTeacher.onions:
   print("DRAW!!")
elif goldenTeacher.onions <= albinoAPlus.onions:
   print("[+]" + albinoAPlus.name + " WINS with " + str(albinoAPlus.onions) + " onions!!")
elif albinoAPlus.onions <= goldenTeacher.onions:
   print("[+]" + goldenTeacher.name + " WINS with " + str(goldenTeacher.onions) + " onions!!")


#for z in range(len(mycoUser)):
    #print(mycoUser[z])
# print(len(mycoUser))
# print(mycoUser[0])

