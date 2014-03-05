import random
import pdb

#pdb.set_trace()

random.seed()

class soldier:
	def __init__(self, name = None, baseHealth = None, health = None, damage = None, armor = None):
		
		if name == None:
			self.name = '0'
		else:
			self.name = name

		if baseHealth == None:
			self.baseHealth = 100
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

		if armor == None:
			self.armor = 0
		else:
			self.armor = armor

	def attack(self, soldier):
		if self.damage - soldier.armor <= 0:
			pass
		else:
			soldier.health = soldier.health - (self.damage - soldier.armor)
			
			#DEBUG
			#print(self.name, 'attacked', soldier.name, 'for', self.damage - soldier.armor, 'damage.')
			#print(soldier.name, 'now has', soldier.health, 'health')

def reproduce(sol):
	mutate = random.randint(0, 100)
	offspring = soldier(str(int(sol.name) + 1), sol.baseHealth, sol.damage, sol.armor)

	if mutate <= 5:
		offspring.name = str(int(offspring.name) + 100)

	mutate = random.randint(0, 100)
	
	if mutate <= 5:
		offspring.baseHealth = random.randint(offspring.baseHealth - 5, offspring.baseHealth + 5)
		offspring.health = offspring.baseHealth

	mutate = random.randint(0, 100)
	
	if mutate <= 5:
		offspring.damage = random.randint(offspring.damage - 1, offspring.damage + 1)

	if offspring.damage <= 0:
			offspring.damage = 1
	
	mutate = random.randint(0, 100)
	
	if mutate <= 5:
		offspring.armor = random.randint(offspring.armor - 1, offspring.armor + 1)

	if offspring.armor < 0:
		offspring.armor = 0

	return offspring

def fight(sol1, sol2):

	if sol1.name == sol2.name:
		winner = sol1
		return sol1

	first = random.randint(1, 2)

	print('Health of', sol1.name, sol1.health)
	print('Armor of', sol1.name, sol1.armor)
	print('Damage of', sol1.name, sol2.damage)

	print('Health of', sol2.name, sol2.health)
	print('Armor of', sol2.name, sol2.armor)
	print('Damage of', sol2.name, sol2.damage)

	rounds = 0

	if first == 1:
		while (sol1.health > 0) and (sol2.health > 0) and (rounds < 3000):
			sol1.attack(sol2)
			if sol2.health > 0:
				sol2.attack(sol1)
			rounds += 1
		if sol1.health > 0:
			winner = sol1
			return winner
		elif sol2.health > 0:
			winner = sol2
			return winner
		else:
			return None

	else:
		while (sol1.health > 0) and (sol2.health > 0) and (rounds < 3000):
			sol2.attack(sol1)
			if sol1.health > 0:
				sol1.attack(sol2)
			rounds += 1
		if sol1.health > 0:
			winner = sol1
			return winner
		elif sol2.health > 0:
			winner = sol2
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
			if match[0].name == match[1].name:
				pass
			else:
				print('Item', x, soldier_list[x].name, 'matched with Item', x-1, soldier_list[x-1].name)
				tuplelist.append(match)

	return tuplelist


def main():
	soldiers = []
	iterations = 20

	abel = soldier('0', baseHealth = 10)

	cain = soldier('1', baseHealth = 13)

	soldiers.append(abel)
	soldiers.append(cain)

	for x in range(0, iterations):
		
		matches = matchfighters(soldiers)
		winner_list = []

		print('Round', x, 'of', iterations)
		
		for match in matches:

			print(match[0].name, 'vs.', match[1].name)

			winner = fight(match[0], match[1])

			if winner != None:
				winner_list.append(winner)

			try:
				print('Match Complete,', winner.name, 'won with', winner.health, 'health remaining')
			except:
				print('Both combatants died')

		soldiers = winner_list.copy()

		for victor in winner_list:
			victor.health = victor.baseHealth
			for k in range(0, 3):
				print(k)
				soldiers.append(reproduce(victor))

		try:
			print(soldiers[0].name)
		except:
			print('There are no winners for this round')

main()


