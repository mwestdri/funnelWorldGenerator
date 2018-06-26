import random
import math
from occupation import occupations 
import names
import traits


def mod(score):
  mods = {
       3: -3,
       4: -2,
       5: -2,
       6: -2,
       7: -1,
       8: -1,
       9: 0,
       10: 0,
       11: 0,
       12: 0,
       13: 1,
       14: 1,
       15: 1,
       16: 2,
       17: 2,
       18: 2
  }
  return mods.get(score)

def d6():
  return random.randint(1,6)

def gender():
   g = random.randint(1,2)
   if g == 1:
       return 'Male'
   else:
       return 'Female'
   
def mainStat(stat):
   r1 = d6()
   r2 = d6()
   r3 = d6()
   rawscore = r1 + r2 + r3
   m= str(mod(rawscore))
   print(stat + ': ' +str(rawscore) + ', Mod: '+m)
   return rawscore

def getOccupation():
   oc = random.randint(1,100)
   return occupations[oc]
def getName(occ, gender):
   race = 'Human'
   if 'Dwarf' in occ:
      race = 'Dwarf'
   elif 'Elf' in occ:
      race = 'Elf'
   elif 'Halfling' in occ:
      race = 'Halfling'
   if 'Human' in race:
      index = random.randint(1,100)
      if 'Male' in gender:
         return names.maleNames[index]
      else:
         return names.femaleNames[index]
   if 'Dwarf' in race:
      index = random.randint(1,10)
      if 'Male' in gender:
	  	 return names.maleDwarfNames[index]
      else:
	  	 return names.femaleDwarfNames[index]
   if 'Elf' in race:
      index = random.randint(1,10)
      if 'Male' in gender:
	  	 return names.maleElfNames[index]
      else:
	  	 return names.femaleElfNames[index]
   if 'Halfling' in race:
      index = random.randint(1,10)
      if 'Male' in gender:
	  	 return names.maleHalflingNames[index]
      else:
	  	 return names.femaleHalflingNames[index]
def getPhysTrait():
   index = random.randint(1, 100)
   return traits.physical[index]
def getPersTrait():
   index = random.randint(1, 100)
   return traits.personality[index]
stats = ['str','dex','con', 'int', 'wis','cha','luc']


print('\n\n################### A Villager #################\n')
occ = getOccupation()
gender = gender()
name = getName(occ, gender)
print('Name: '+getName(occ, gender))

print('Occupation: '+occ)
print ('Gender: '+gender+'\n')

print('Traits:')
print('Physical trait: '+str(getPhysTrait()))
print('Personality trait: '+str(getPersTrait()))

print('\n\n############## Ability Scores and Modifiers ##############\n')
st = mainStat('STR')
dex = mainStat('DEX')
con = mainStat('CON')
inte = mainStat('INT')
wis = mainStat('WIS')
cha = mainStat('CHA')
luc = mainStat('LUC')

hp=math.ceil(float(con)/4)
load=mod(st) + 4
print('\nHP: '+str(hp))
print('LOAD: '+str(load))

