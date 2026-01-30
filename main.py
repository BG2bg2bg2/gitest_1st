#Hi

import random

#skills = []
skills = []

#souls
souls = 0
#level = 1
level = 1


# leveling up function
def function():
    #if user has collected 3  of souls then
    if souls == 3:
    # you have leveled up by one level 1 += level 
        level += 1
        print("you've moved up one leved")
    #while level < 10 
    while level < 10:
    # keep adding a level for every three kills
      level += 1 
        

# making a function to view characters options and what skills they have
def characters_options():
    #   storing all the characterics for each character in an induval list
    #   human = {"strength": 23, "health": 50}
    #   dog = {"strength": 47, "health": 120}
    #   goblin = {"strength": 35, "health": 100}
    #   bear = {"strength": 12, "health": 25}
    human = {"strength": 23, "health": 50}
    dog = {"strength": 47, "health": 120}
    goblin = {"strength": 35, "health": 100}
    bear = {"strength": 12, "health": 25}


# making a function to handle skill dependencies and prerequisites(by using if statements)
def skill_change():
# list for special skills [flying monkey, flying dog,spin kick]
  special_skills = ["flying monkey", "flying dog","spin kick,flying blobfish"]
    # if user had 10 == souls
  if souls == 10: 
    #   show user you have unlocked special skill
    print("you have unlocked a special skills")
    #   pull one of the random skills from the list
    random_skill = random.choice(special_skills)
    #add it onto the skills
    skills.append(random_skill)
  # else if user had eqaul 8 souls
  elif souls == 8:
        #show user you got a special skill
        print("you got a special skills")
        # its flying blobfish 
        print("ITS FLYING BLOBFISH")
        # add blobfish to SKILL LIST
        skills.append("flying blobfish")

    # elif user had 5 == souls
  elif souls == 5:
    #    how user you dont get a skill
    print("you dont get a skill")
    #else print you just moved up a level
  else:
     print("you don't get anything")
