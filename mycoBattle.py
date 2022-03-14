from shutil import move
import cv2
import random
import time
from termcolor import colored


class portobello:
   name = "Portobello"
   hp = 300
   hitPoints = 0
   taunt = "idiot! fool!"
   block = False
   spores = 0
 
  
class morel:
   name = "Morel"
   hp = 325
   hitPoints = 0
   taunt = "trash!"
   block = False
   spores = 0


def playerBlock(blocker):
   blocker.block = True



   
def resetBlock(blocker):
   blocker.block = False




moveName = ["bopped", "shmacked", "dropped", "folded", "clapped"]
moveLog = ""




def playerAttack(attacker, attackee):
   if attacker.name == "Portobello":
      if attackee.block == True:
         attacker.hitPoints = round(random.randint(40, 70) / 4, 2)
         attackee.hp = attackee.hp - attacker.hitPoints
      else:
         attacker.hitPoints = random.randint(40, 70)
         attackee.hp = attackee.hp - attacker.hitPoints
         attackee.spores = attackee.spores - 1
   elif attacker.name == "Morel":
      if attackee.block == True:
         attacker.hitPoints = round(random.randint(25, 85) / 4, 2)
         attackee.hp = attackee.hp - attacker.hitPoints
      else:
         attacker.hitPoints = random.randint(25, 85)
         attackee.hp = attackee.hp - attacker.hitPoints
         attackee.spores = attackee.spores - 1
   print("[*]" + attacker.name + " " + str(random.choice(moveName)) + " " + attackee.name + ":" + colored(" -" + str(attacker.hitPoints), 'red'))




def playerTaunt(taunter):
   taunter.spores = taunter.spores + 2
   print("[!]" + taunter.name + ": " + taunter.taunt)
      



print("Taunt to gain spores[(@]. Landing attacks will cause the player to lose a spore and hp." +
   "Blocking attacks will prevent the player from losing a spore and weakens the enemy's hit. " +
   "\nWinner of the battle gets rewarded 3 spores." +
   "\nThe player with the most spores at the end of the game wins.\n")



while portobello.hp > 0 and morel.hp > 0:
   resetBlock(portobello)
   resetBlock(morel)
   swung = False
   mycoUser = []
   possibleMoves = ["Attacked", "Taunted", "Blocked"]

   if moveLog == "Attacked":
      compMeneuver = random.choices(possibleMoves, weights = [7, 10, 3], k = 1)
   elif moveLog == "Taunted":
      compMeneuver = random.choices(possibleMoves, weights = [10, 5, 7], k = 1)
   elif moveLog == "Blocked":
      compMeneuver = random.choices(possibleMoves, weights = [10, 3, 5], k = 1)
   else:
      compMeneuver = random.choices(possibleMoves, weights = [7, 5, 10], k = 1)
      
   
   print("\n" + portobello.name + ": " + colored(str(round(portobello.hp, 2)), 'green') + " hp | " + \
      colored(str(portobello.spores), 'yellow') + " spores(s) (@\n" + morel.name + ": " + colored(str(round(morel.hp, 2)), 'green') +
      " hp | " + colored(str(morel.spores), 'yellow') + " spores(s) (@\n")
   

   melee = input("Press 'q' to taunt, 'f' to block, or 'e' to attack! -> ")
   print("\nBATTLING...")
   time.sleep(1.5)
   

   if melee == "e":
      print("You Attacked!")
      swung = True
      moveLog = possibleMoves[0]
   elif melee == "q":
      print("You Taunted!")
      playerTaunt(portobello)
      moveLog = possibleMoves[1]
   elif melee == "f":
      print("You Blocked!")
      playerBlock(portobello)
      moveLog = possibleMoves[2]
   else:
     print("ERRRORRR!!")
     break


   time.sleep(1)
   print("Morel " + compMeneuver[0] + "!")
   time.sleep(1)
   

   print("________________RESULTS_________________")
   if compMeneuver == ["Attacked"]:
      if swung == True:
         playerAttack(portobello, morel)
         # time.sleep(1)
      playerAttack(morel, portobello)
   elif compMeneuver == ["Taunted"]:
      if swung == True:
         playerAttack(portobello, morel)
      playerTaunt(morel)
   elif compMeneuver == ["Blocked"] and swung == True:
      playerBlock(morel)
      playerAttack(portobello, morel)






if portobello.hp <= morel.hp:
   morel.spores = morel.spores + 3
elif morel.hp <= portobello.hp:
   portobello.spores = portobello.spores + 2

    
if morel.spores == portobello.spores:
   print("DRAW!!")
elif portobello.spores <= morel.spores:
   print("[+]" + morel.name + " WINS with " + str(morel.spores) + " spores!!")
elif morel.spores <= portobello.spores:
   print("[+]" + portobello.name + " WINS with " + str(portobello.spores) + " spores!!")


