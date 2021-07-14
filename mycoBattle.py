import cv2
import random
import time


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


def playerAttack(attacker, attackee):
   if attacker.name == "Golden Teacher":
      if attackee.block == True:
         attacker.hitPoints = round(random.randint(40, 70) / 2, 2)
         attackee.hp = attackee.hp - attacker.hitPoints
      else:
         attacker.hitPoints = random.randint(40, 70)
         attackee.hp = attackee.hp - attacker.hitPoints
         attackee.onions = attackee.onions - 0.5
   elif attacker.name == "Albino A+":
      if attackee.block == True:
         attacker.hitPoints = round(random.randint(25, 85) / 2, 2)
         attackee.hp = attackee.hp - attacker.hitPoints
      else:
         attacker.hitPoints = random.randint(25, 85)
         attackee.hp = attackee.hp - attacker.hitPoints
         attackee.onions = attackee.onions - 0.5
   print("[*]" + attacker.name + " " + str(random.choice(moveName)) + " " + attackee.name + ": -" + str(attacker.hitPoints))


def playerTaunt(taunter):
   taunter.onions = taunter.onions + 1
   print("[!]" + taunter.name + ": " + taunter.taunt)
      

print("Use the keys to battle the agent. Taunt to gain onions(!*!). Get hit and lose half a grain.\nBlock to prevent losing onions. Winner of the fight gets rewarded 1 grain.\nThe side with most onions at the end of the game wins.\n")

while goldenTeacher.hp > 0 and albinoAPlus.hp > 0:
   resetBlock(goldenTeacher)
   resetBlock(albinoAPlus)
   swung = False
   mycoAgent = ["attack", "taunt", "block"]
   agentMeneuver = random.choices(mycoAgent, weights = [10, 3, 5], k = 1)
   
   print("\n" + goldenTeacher.name + ": " + str(round(goldenTeacher.hp, 2)) + "hp    !*! : " + \
      str(goldenTeacher.onions) + " onion(s)\n" + albinoAPlus.name + ": " + str(round(albinoAPlus.hp, 2)) + "hp    !*! : " + str(albinoAPlus.onions) + " onion(s)\n")
   
   melee = input("Press 'q' to taunt, 'f' to block, or 'e' to attack! -> ")
   print("\nBATTLING...")
   time.sleep(1.5)
   
   if melee == "e":
      print("You Attacked!")
      swung = True
      # playerAttack(goldenTeacher, albinoAPlus)
   elif melee == "q":
      print("You Taunted!")
      playerTaunt(goldenTeacher)
   elif melee == "f":
      print("You Blocked!")
      playerBlock(goldenTeacher)
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
         time.sleep(1)
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
   albinoAPlus.onions = albinoAPlus.onions + 1
elif albinoAPlus.hp <= goldenTeacher.hp:
   goldenTeacher.onions = goldenTeacher.onions + 1

    
if albinoAPlus.onions == goldenTeacher.onions:
   print("DRAW!!")
elif goldenTeacher.onions <= albinoAPlus.onions:
   print("[+]" + albinoAPlus.name + " WINS with " + str(albinoAPlus.onions) + " onions!!")
elif albinoAPlus.onions <= goldenTeacher.onions:
   print("[+]" + goldenTeacher.name + " WINS with " + str(goldenTeacher.onions) + " onions!!")