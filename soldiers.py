import random
import pdb
from collections import OrderedDict

#pdb.set_trace()

random.seed()

class soldier:
    def __init__(self, 
                 name = None, 
                 baseHealth = None, 
                 health = None, 
                 damage = None, 
                 armor = None, 
                 accuracy = None,
                 agility = None, 
                 fertility = None,
                 stealth = None,
                 detection = None,
                 pursuit = None,
                 escape = None,
                 size = None, 
                 dna = None):

        self.id = random.random() * 100000000000
        self.wins = 0

        if dna == None:
            self.dna = ''
        else:
            self.dna = dna 

        if fertility == None:
            self.fertility = .70
        else:
            self.fertility = fertility

        if name == None:
            self.name = '0'
        else:
            self.name = name

        if baseHealth == None:
            self.baseHealth = 10
        else:
            self.baseHealth = baseHealth

        if health == None:
            self.health = baseHealth
        else:
            self.health = health

        if damage == None:
            self.damage = 1
        else:
            self.damage = damage

        if accuracy == None:
            self.accuracy = .3
        else:
            self.accuracy = accuracy

        if agility == None:
            self.agility = 0
        else:
            self.agility = agility

        if armor == None:
            self.armor = 0
        else:
            self.armor = armor

        if stealth == None:
            self.stealth = 0
        else:
            self.stealth = stealth

        if detection == None:
            self.detection = .01
        else:
            self.detection = detection

        if pursuit == None:
            self.pursuit = .01
        else:
            self.pursuit = pursuit

        if escape == None:
            self.escape = 0
        else:
            self.escape = escape

        if size == None:
            self.size = 1
        else:
            self.size = size

    def attack(self, soldier):
        if self.damage - soldier.armor <= 0:
            pass
        else:
            roll = random.random()

            if soldier.size != 0:
                agileMod = soldier.agility * (1 / soldier.size)
            else:
                agileMod = 99999999999999999

            hit = self.accuracy - agileMod

            if roll < hit:
                soldier.health = soldier.health - ((self.size * self.damage) - soldier.armor)

            #DEBUG
            #print(self.name, 'attacked', soldier.name, 'for', self.damage - soldier.armor, 'damage.')
            #print(soldier.name, 'now has', soldier.health, 'health')

    def serialize(self):

        string = ''
        string += 'id: ' + str(self.id) + '\n'
        string += 'name: ' + self.name + '\n'
        string += 'baseHealth: ' + str(self.baseHealth) + '\n'
        string += 'health: ' + str(self.health) + '\n'
        string += 'damage: ' + str(self.damage) + '\n'
        string += 'armor: ' + str(self.armor) + '\n'
        string += 'accuracy: ' + str(self.accuracy) + '\n'
        string += 'agility: ' + str(self.agility) + '\n'
        string += 'fertility: ' + str(self.fertility) + '\n'
        string += 'stealth: ' + str(self.stealth) + '\n'
        string += 'detection: ' + str(self.detection) + '\n'
        string += 'pursuit: ' + str(self.pursuit) + '\n'
        string += 'escape: ' + str(self.escape) + '\n'
        string += 'size: ' + str(self.size) + '\n'
        string += 'dna: ' + self.dna + '\n' 

        return string


def reproduce(sol):
    fertile = random.random()
    if fertile < sol.fertility:
        MUTATE_THRESHOLD = 2
        mutate = int(random.random() * 100)
        offspring = soldier(name = str(int(sol.name) + int(random.random() * 10)), 
                            baseHealth = sol.baseHealth, 
                            damage = sol.damage, 
                            armor = sol.armor, 
                            accuracy = sol.accuracy,
                            agility = sol.agility, 
                            fertility = sol.fertility,
                            stealth = sol.stealth,
                            detection = sol.detection,
                            pursuit = sol.pursuit,
                            escape = sol.escape,
                            size = sol.size, 
                            dna = sol.dna)

        if mutate <= MUTATE_THRESHOLD:
            offspring.name = str(int(offspring.name) + 100)
            offspring.dna += 'N'

        mutate = int(random.random() * 100)

        if mutate <= MUTATE_THRESHOLD:
            old = offspring.baseHealth
            offspring.baseHealth += (random.random() - .5)
            offspring.health = offspring.baseHealth
            if old < offspring.baseHealth:
                offspring.dna += 'H'
            else:
                offspring.dna += 'h'

        mutate = int(random.random() * 100)

        if mutate <= MUTATE_THRESHOLD:
            old = offspring.damage
            offspring.damage += (random.random() - .5) * 2
            if old < offspring.damage:
                offspring.dna += 'D'
            else:
                offspring.dna += 'd'
    
        mutate = int(random.random() * 100)
    
        if mutate <= MUTATE_THRESHOLD:
            old = offspring.armor
            offspring.armor += (random.random() - .5) * 2
            if old < offspring.armor:
                offspring.dna += 'R'
            else:
                offspring.dna += 'r'

        mutate = int(random.random() * 100)

        if mutate <= MUTATE_THRESHOLD:
            old = offspring.accuracy
            offspring.accuracy +=(random.random() - .5)
            
            if old < offspring.accuracy:
                offspring.dna += 'A'
            else:
                offspring.dna += 'a'

        mutate = int(random.random() * 100)

        if mutate <= MUTATE_THRESHOLD:
            old = offspring.agility
            offspring.agility += (random.random() - .5)
            
            if old < offspring.agility:
                offspring.dna += 'G'
            else:
                offspring.dna += 'g'

        mutate = int(random.random() * 100)

        if mutate <= MUTATE_THRESHOLD:
            old = offspring.fertility
            offspring.fertility += (random.random() - .5) * .3
            if offspring.fertility > 1:
                offspring.fertility = 1
            elif offspring.fertility < 0:
                offspring.fertility = 0
            if old < offspring.fertility:
                offspring.dna += 'F'
            else:
                offspring.dna += 'f'

        mutate = int(random.random() * 100)

        if mutate <= MUTATE_THRESHOLD:
            old = offspring.stealth
            offspring.stealth += (random.random() - .5)
            
            if old < offspring.stealth:
                offspring.dna += 'S'
            else:
                offspring.dna += 's'

        mutate = int(random.random() * 100)

        if mutate <= MUTATE_THRESHOLD:
            old = offspring.detection
            offspring.detection += (random.random() - .5)

            if old < offspring.detection:
                offspring.dna += 'T'
            else:
                offspring.dna += 't'

        mutate = int(random.random() * 100)

        if mutate <= MUTATE_THRESHOLD:
            old = offspring.pursuit
            offspring.pursuit += (random.random() - .5)

            if old < offspring.pursuit:
                offspring.dna += 'P'
            else:
                offspring.dna += 'p'

        mutate = int(random.random() * 100)

        if mutate <= MUTATE_THRESHOLD:
            old = offspring.escape
            offspring.escape += (random.random() - .5)
            
            if old < offspring.escape:
                offspring.dna += 'E'
            else:
                offspring.dna += 'e'

        mutate = int(random.random() * 100)

        if mutate <= MUTATE_THRESHOLD:
            old = offspring.size
            offspring.size = offspring.size * (random.random() + .5)
            
            if old < offspring.size:
                offspring.dna += 'Z'
            else:
                offspring.dna += 'z'

        return offspring
    return None

def fight(sol1, sol2):

    sol1.health = sol1.baseHealth
    sol2.health = sol2.baseHealth

    if sol1.id == sol2.id:
        return sol1

    detect = sol1.stealth - (sol2.detection * sol1.size)
    
    if detect < 0:
        detect = sol2.stealth - (sol1.detection * sol2.size)

    look = random.random()

    if sol1.stealth > sol2.detection:
        if look < detect:
            return sol1

    if sol2.stealth > sol1.detection:
        if look < detect:
            return sol2

    #if sol1.stealth > sol2.detection:
    #    return sol1
    #elif sol2.stealth > sol1.detection:
    #    return sol2

    first = random.random()

#    print('Health of', sol1.name, sol1.health)
#    print('Armor of', sol1.name, sol1.armor)
#    print('Damage of', sol1.name, sol2.damage)

#    print('Health of', sol2.name, sol2.health)
#    print('Armor of', sol2.name, sol2.armor)
#    print('Damage of', sol2.name, sol2.damage)

    rounds = 0

    if first > .5:
        while (sol1.health > 0) and (sol2.health > 0) and (rounds < 3000):

            if rounds % 5 == 0 or rounds == 0:
                escape = sol1.escape - sol2.pursuit

                if escape < 0:
                    escape = sol2.escape - sol1.pursuit

                run = random.random()

                if sol1.escape > sol2.pursuit:
                    if run < escape:
                        return sol1

                if sol2.escape > sol2.pursuit:
                    if run < escape:
                        return sol2

            sol1.attack(sol2)

            if sol2.health > 0:
                sol2.attack(sol1)

            rounds += 1

        if sol1.health > 0:
            winner = sol1
            winner.wins += 1
            return winner

        elif sol2.health > 0:
            winner = sol2
            winner.wins += 1
            return winner

        else:
            return None

    else:
        while (sol1.health > 0) and (sol2.health > 0) and (rounds < 3000):
            
            if rounds % 5 == 0 or rounds == 0:
                escape = sol1.escape - sol2.pursuit * sol1.size

                if escape < 0:
                    escape = sol2.escape - sol1.pursuit * sol2.size

                run = random.random()

                if sol1.escape > sol2.pursuit:
                    if run < escape:
                        return sol1

                if sol2.escape > sol2.pursuit:
                    if run < escape:
                        return sol2

            sol2.attack(sol1)


            if sol1.health > 0:
                sol1.attack(sol2)

            rounds += 1

        if sol1.health > 0:
            winner = sol1
            winner.wins += 1
            return winner

        elif sol2.health > 0:
            winner = sol2
            winner.wins += 1
            return winner
            
        else:
            return None

def matchfighters(soldier_list):
    tuplelist = []
    for x in range(0, len(soldier_list)):

        if x % 2 == 0:
            pass

        else:
            match = (soldier_list[x], soldier_list[x-1])
            if match[0].id == match[1].id:
                pass
            else:
#                print('Item', x, soldier_list[x].name, 'matched with Item', x-1, soldier_list[x-1].name)
                tuplelist.append(match)

    return tuplelist

def writeDNAtoFile(filename, dnaDict = None, dnaList = None):
    with open(filename, 'w') as f:
        if dnaDict != None:
            for dna in dnaDict.keys():
                f.write(dna + '    ' + str(dnaDict[dna]) + '\n')
        elif dnaList != None:
            for dna in dnaList:
                f.write(dna + '\n')

def sequence(dna):
    traits = {}
    seq = ''
    for letter in dna:
        increase = 0
        if letter.islower():
            increase = -1
        else:
            increase = 1
        letter = letter.upper()
        if letter not in traits:
            traits[letter] = increase
        else:
            traits[letter] += increase

    for trait in traits.keys():
        seq += trait + ': ' + str(traits[trait]) + '\n'
        
    return seq

def main():
    soldiers = []
    sequences = []
    varieties = []
    survivingDNA = []
    profiles = []
    primeDNA = {}
    MAX_POPULATION = 100
    iterations = 10000

    abel = soldier('0', dna = 'ABE')
    cain = soldier('1', dna = 'CAI')
    cameron = soldier('2', dna = 'CAM')
    josiah = soldier('3', dna = 'JOS')

    soldiers.append(abel)
    soldiers.append(cain)
    soldiers.append(cameron)
    soldiers.append(josiah)

    for x in range(0, iterations):
        survivingDNA = []
        sequences = []
        profiles = []

        matches = matchfighters(soldiers)
        winner_list = []

        print('Round', x, 'of', iterations)
        print('Population:', len(soldiers))

        for match in matches:

#            print(match[0].name, 'vs.', match[1].name)

            winner = fight(match[0], match[1])

            if winner != None:
                winner_list.append(winner)

#            try:
#                print('Match Complete,', winner.name, 'won with', winner.health, 'health remaining')
#            except:
#                print('Both combatants died')

        soldiers = winner_list.copy()

        for victor in winner_list:
            victor.health = victor.baseHealth
            for k in range(0, 3):
                if len(soldiers) < MAX_POPULATION:
                    offspring = reproduce(victor)
                    if offspring != None:
                        soldiers.append(offspring)

        for fighter in soldiers:

            if fighter.dna not in varieties:
                varieties.append(fighter.dna)
                primeDNA[fighter.dna] = fighter.wins
            else:
                primeDNA[fighter.dna] += fighter.wins

            if fighter.dna not in survivingDNA:
                survivingDNA.append(fighter.dna)

            sequences.append(sequence(fighter.dna))
            profiles.append(fighter.serialize())
        

    sortedDNA = OrderedDict(sorted(primeDNA.items(), key=lambda primeDNA: primeDNA[1], reverse=True))

    writeDNAtoFile('dna.txt', dnaDict = sortedDNA)
    writeDNAtoFile('survivors.txt', dnaList = survivingDNA)
    writeDNAtoFile('sequences.txt', dnaList = sequences)
    writeDNAtoFile('profiles.txt', dnaList = profiles)

main()


