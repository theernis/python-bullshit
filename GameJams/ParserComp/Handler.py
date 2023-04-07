import webbrowser
import UI
import random
import math

inventory_size = 8
#["name", "type", stack_size, rarity]
items  = [
	["meat", "food:30", 16, 1],
	["health_potion", "food:60", 32, 2],
	["bone", "resources", 64, 1],
	["fang", "resources", 256, 3],
	["scrap", "resources", 16384, -1],
	["coin", "money:5", 4096, 0],
]
#["item", amount]
inventory = []

def inventory_handler(a):
	
	a = a.split(":")

	def fix():

		global inventory
		
		#creates new inventory with infinite size stacks
		new_inventory = []
		for b in inventory:
			
			skip = False

			#adds to a stack if it exists
			for c in range(len(new_inventory)):
	
				if b[0] == new_inventory[c][0]:
					new_inventory[c][1] += b[1]
					skip = True
					break
	
			if not skip:
				#adds to a new stack if no other stack exists
				new_inventory.append(b)


		#if stacks are too big then seperate
		new_inventory2 = []
		for b in new_inventory:
			
			#finds an item for stack size
			for c in items:
				if b[0] == c[0]:
					item_amount = b[1]
					stack_size = c[2]
					while item_amount > 0:
						#if more than full stack create new full stack
						if item_amount >= stack_size:
							new_inventory2.append([b[0], stack_size])
							item_amount -= stack_size
						#if not full stack create new stack with required amount
						elif item_amount > 0:
							new_inventory2.append([b[0], item_amount])
							item_amount -= item_amount

		inventory = new_inventory2

	def add():

		global inventory

		#checks if item able to be added
		in_items = False
		for b in items:

			if b[0] == a[1]:
				in_items = True
		if not in_items:
			return

		#calculates amount of items
		b = 0
		c = float(a[2])
		while c > 0:
			if random.random() < c:
				b += 1
			c -= 1

		#adds to a stack if it exists
		for c in range(len(inventory)):

			if a[1] == inventory[c][0]:
				inventory[c][1] += b
				return

		#adds to a new stack if no other stack exists
		inventory.append([a[1], b])

	def remove():

		global inventory
		
		#creates new inventory with infinite size stacks
		new_inventory = []
		for b in inventory:
			
			skip = False

			#adds to a stack if it exists
			for c in range(len(new_inventory)):
	
				if b[0] == new_inventory[c][0]:
					new_inventory[c][1] += b[1]
					skip = True
					break
	
			if not skip:
				#adds to a new stack if no other stack exists
				new_inventory.append(b)

		#finds needed item and removes from it
		#if there is not enouh of item return false
		item_found = False
		for b in range(len(new_inventory)):

			if new_inventory[b][0] == a[1]:
				
				if new_inventory[b][1] >= int(a[2]):
					new_inventory[b][1] -= int(a[2])
					item_found = True
				break

		inventory = new_inventory
		return item_found

	def show():
		
		global inventory

		if len(inventory) == 0:
			UI.print1(">>you have no items")
			return

		#if this value is true it shows extra info
		info = False
		if len(a) > 1:
			info = bool(a[1])

		for b in range(len(inventory)):

			if info:
				item = ["item", "debug", math.inf, math.pi]

				for c in items:
					
					if c[0] == inventory[b][0]:
						item = c

				print("{number}. - {name} ({amount}), type - {type}, stack_size - {stack_size}, rarity - {rarity}".format(
					number=b, name=inventory[b][0], amount=inventory[b][1], type=item[1], stack_size=item[2], rarity=item[3]))
			else:
				print("{number}. - {name} ({amount})".format(number=b, name=inventory[b][0], amount=inventory[b][1]))

	if a[0] == "fix":
		fix()
		return

	if a[0] == "add":
		add()
		fix()
		return

	if a[0] == "remove":
		b = remove()
		fix()
		return b

	if a[0] == "show":
		fix()
		show()
		return


events = []

health = 100
max_health = 100

attacks = ["fist:meele:10:15:.25"]

#["name", health, attacks[], drops[]]
enemies = [
	["wolf", 50, [["claw", 5], ["bite", 10]], ["meat:5", "bone:10", "fang:0.1"]],
	["bear", 150, [["claw", 15], ["bite", 30]], ["meat:10", "bone:20", "fang:0.25"]]
]

running_away = False

#["name", "short description", trades[]]
traders = [
	["john", "nomad cleric",
		[
			["meat:1", "coin:4"],
			["bone:1", "coin:4"],
			["fang:1", "coin:16"],
			["coin:8", "health_potion:1"]
		]
	]
]

#creates trader jake who buys everything
jake_trades = []
for item in items:
	if item[3] > 0:
		jake_trades.append(["{item}:1".format(item=item[0]), "coin:{cost}".format(cost=2**(item[3]+1))])
traders.append(["jake", "hoarder", jake_trades])


#handles events
#one per game loop
def event_handler(event):
	
	a = event.split(":")
	events.remove(event)

	#tutorial event
	def tutorial():
		UI.spell("\n----------", 5)
		UI.print1("tutorial\nwe should start with a simple fight")

		#starts a tutorial fight
		events.append("fight:wolf")
		event_handler(events[len(events)-1])

		#starts a second tutorial fight
		UI.spell("\n----------", 5)
		UI.print1("now you will have to use 'run' command\nto run away from too strong enemy\nor you can use command 'eat [item]' to restore health" )

		events.append("fight:bear")
		event_handler(events[len(events)-1])

		#starts a tutorial trade
		UI.spell("\n----------", 5)
		UI.print1("now you can trade some items you got from fights" )

		events.append("trade:john")
		event_handler(events[len(events)-1])

	#starts tutorial event
	if event == "tutorial":
		tutorial()
		return

	#fight event
	def fight():
		
		global health
		global running_away
		global tags

		enemy_info = []

		for i in enemies:
			if i[0] == a[1]:
				enemy_info = i

		if enemy_info == []:
			return

		enemy = enemy_info[0]
		enemy_health = enemy_info[1]
		enemy_attacks = enemy_info[2]
		enemy_loot = enemy_info[3]

		UI.print1("\n----------")
		UI.print1("you got into a fight with: {enemy} ({health})".format(enemy=enemy, health=enemy_health))

		#prints all player attacks
		UI.print1("\nyour attacks:")
		for attack in attacks:
			b = attack.split(":")
			UI.print1("{name}, type - {attack_type}, damage - {damage}".format(name = b[0], attack_type = b[1], damage = b[2]))

		#prints all enemy attacks
		UI.print1("\nenemy attacks:")
		for attack in enemy_attacks:
			UI.print1("{name}, damage - {damage}".format(name = attack[0], damage = attack[1]))


		damage = 0
		damage_dealt = 0

		#enemy attack function
		def enemy_attack(enemy_attacks):
			attack = random.choice(enemy_attacks)
			UI.print1("{enemy} used {attack} and dealt {amount} damage".format(enemy = enemy, attack = attack[0], amount = attack[1]))
			return int(attack[1])

		#player attack function
		def player_attack():

			move_chosen = ""

			#player choosing his move_chosen
			while move_chosen == "":

				player_input = UI.input1("<select your move> ")

				event_command_handler(player_input)

				for i in attacks:
					if player_input == i.split(":")[0]:
						move_chosen = i.split(":")

				if player_input == "run":
					global running_away
					running_away = True
					return 0
			
			damage_amount = 0
			
			#calculates critical bonus
			if move_chosen[1] == "meele":
				damage_amount = int(move_chosen[2])
				if random.random() < float(move_chosen[4]):
					damage_amount = int(move_chosen[3])

			UI.print1("you used {attack} and dealt {amount} damage".format(attack = move_chosen[0], amount=damage_amount))

			return damage_amount

		#fight loop
		while health > damage and enemy_health > damage_dealt:
			b = damage_dealt
			damage_dealt += player_attack()
			if running_away:
				break
			if enemy_health > damage_dealt:
				damage += enemy_attack(enemy_attacks)
			UI.print1("enemy health: {health}".format(health = UI.slider(enemy_health - damage_dealt, enemy_health, 25)))
			UI.print1("your health: {health}".format(health = UI.slider(health - damage, max_health, 25)))

		UI.print1("\n----------")
		if not running_away:
			if enemy_health > damage_dealt:
				UI.print1("{enemy} won".format(enemy=enemy))
			
			if health > damage:
				UI.print1("you won")
				b = []
				for attack in enemy_attacks:
					b.append(attack[1])
				exp = int(sum(b)/len(b)*enemy_health+damage)
				health -= damage
				tags.append("exp:{exp}".format(exp=exp))
				for item in enemy_loot:
					inventory_handler("add:{item}".format(item=item))
				inventory_handler("show")

			tags.append("dmg:{damage}".format(damage=damage))
			tag_handler(tags)
		else:
			UI.print1("you ran away")
			running_away = True


	#starts fight event
	if a[0] == "fight":
		fight()
		return

	def trade():

		#finds a trader
		trader = []
		for b in traders:
			if a[1] == b[0]:
				trader = b
				break

		#if trader is found get his trades
		trades = []
		try:
			trades = trader[2]
		except:
			pass

		#randomizes values of trades
		for b in range(len(trades)):
			#randomize sell
			c = int(int(trades[b][0].split(":")[1])*(random.random()+.5))
			if not c == 0:
				trades[b][0] = ":".join([trades[b][0].split(":")[0], str(c)])
			#randomize buy
			c = int(int(trades[b][1].split(":")[1])*(random.random()+.5))
			if not c == 0:
				trades[b][1] = ":".join([trades[b][1].split(":")[0], str(c)])

		#checks if tyrader is found and has trades
		if trader == [] or trades == []:
			return

		UI.print1("\n----------")
		UI.print1("you were approached by trader {name}\n>>{description}\n".format(name=trader[0], description=trader[1]))
		
		going_away = False

		#prints trades
		def print_trades():
			for b in range(len(trades)):
				UI.print1("{number}. {sell_amount} {sell_item} -> {buy_amount} {buy_item}".format(number=b, sell_amount=trades[b][0].split(":")[1], sell_item=trades[b][0].split(":")[0], buy_amount=trades[b][1].split(":")[1], buy_item=trades[b][1].split(":")[0]))

		print_trades()

		#trade loop
		while not going_away:
			try:
				trade_input = UI.input1("<trade number> ")
				if trade_input == "trades":
					print_trades()
				if trade_input == "exit":
					break
				event_command_handler(trade_input)
				trade_number = int(trade_input)
				if inventory_handler("remove:"+trades[trade_number][0]):
					inventory_handler("add:"+trades[trade_number][1])
				else:
					UI.print1("you dont have enough items")
			except:
				pass


	if a[0] == "trade":
		trade()
		pass

name = ""

tags = []
exp = 0
level = 0

#handles tags
#all of them per game loop
#should be used for showing stats after events
def tag_handler(tags):

	global events

	welcome1 = "welcome adventurer mr. ehrr... \nwhats your name again? \ni keep forgetting."
	#*asks for name*
	welcome2 = "oh, its {name} \ni hope i will remember this time"
	welcome3 = "i guess we should start your adventure"
	
	#displays start text
	def start_text():
		UI.print1(welcome1)
		global name
		name = UI.input1("<whats your name?> ")
		UI.print1(welcome2.format(name=name))
		UI.print1(welcome3)
		events.append("tutorial")

	#prints damage taken
	def damage(value):
		UI.print1("damage taken: {value}".format(value=value))

	#prints experience got
	def experience(value):
		global exp
		exp += int(value)
		UI.print1("experience got: {value}".format(value=value))

		def level_up():
			global level
			global exp
			old = level
			level = math.floor(math.log(exp + 1, 2))
			if old != level:
				UI.print1("level up: {old} -> {new}".format(old=old, new=level))

		level_up()


	#loops trough all tags and executes each other 
	for a in tags:

		tags.remove(a)

		if a == "start":
			start_text()
			continue

		b = a.split(":")

		if b[0] == "dmg":
			damage(b[1])
			continue

		if b[0] == "exp":
			experience(b[1])
			continue


#!!!DONT FORGET!!!
#7 LETTER RULE:
#every command
#has to be 7
#letters or less

#handles player input commands during events
def event_command_handler(text):
	
	if text == "":
		return
	
	a = text.split(" ")

	def event_help():
		print("##########")
		print(">>game commands")
		print("help - shows this list")
		print("inventory - shows your inventory")
		print("eat - eats specified item and restores health")
		print(">>event-specific game commands")
		print("#>fight")
		print("#run - exits batlle with no additional damage")
		print("#>trade")
		print("#trades - show trades")
		print("#exit - leaves trade")
		print("##########")

	if a[0] == "help":
		event_help()

	def show():
		inventory_handler("show")

	if a[0] == "inventory":
		show()

	def eat():

		is_food = False
		heal = 0
		for b in items:

			if b[0] == a[1]:
				if b[1].split(":")[0] == "food":
					is_food = True
					heal = int(b[1].split(":")[1])
		if not is_food:
			return

		if inventory_handler("remove:{item}:1".format(item=a[1])):
			global health
			health += heal
			UI.print1("ate {item} and healed {heal}".format(item=a[1], heal=heal))
			if health > max_health:
				health = max_health

	if a[0] == "eat":
		eat()
		return


locations = ["field", "forest"]
current_location = "field"

#handles player input commands
def command_handler(text):
	
	if text == "":
		return

	text = text.split(" ")

	#non-game commands
	def help_text():
		print("##########")
		print(">>explanations")
		print("<> - it means you can type any commands")
		print("<text> - means its waiting for input")
		print("<text()> - in () are showed possible answers")
		print("----------")
		print(">>non-game commands")
		print("help - this text")
		print("test - made to test command handler")
		print("credits - shows credits")
		print("twitter - shows a link to my twitter page")
		print("exit - leaves the game")
		print("----------")
		print(">>non-event game commands")
		print("go_to - go to some location")
		print("all_loc - show possible locations")
		print("my_loc - show your current location")
		print("time - shows day and time")
		print("nap - skips time with chance of events")
		print("##########")

	if text[0] == "help":
		help_text()
		return
	
	def test():
		print("##########")
		print("test")
		print("##########")

	if text[0] == "test":
		test()
		return

	def credits():
		print("##########")
		print("Game Made By:")
		print("<<The Ernis>>")
		print("##########")

	if text[0] == "credits":
		credits()
		return

	def twitter():
		print("##########")
		print("https://twitter.com/ernis_the")
		if input("<do you want to open in browser (y)>: ") == "y":
			webbrowser.open('https://twitter.com/ernis_the')
		print("##########")

	if text[0] == "twitter":
		twitter()
		return

	def quit_game():
		exit()

	if text[0] == "exit":
		quit_game()

	#game commands
	def go_to():
		global current_location
		try:
			location = text[1]
		except:
			return
		if current_location != location:
			for a in locations:
				if a == location:
					current_location = location
					UI.print1("went to: {location}".format(location=location))
					return
			UI.print1("location not found")
			return
		UI.print1("you are already there")

	if text[0] == "go_to":
		go_to()
		return

	def print_locations():
		UI.print1(str(locations))

	if text[0] == "all_loc":
		print_locations()
		return
		
	def print_current_location():
		UI.print1(current_location)

	if text[0] == "my_loc":
		print_current_location()
		return

	def show_time():
		UI.print1("day: {day}\ntime: {time}".format(day=day, time=hour))

	if text[0] == "time":
		show_time()
		return

	def nap():
		#sets nap yime
		nap_time = 1
		try:
			nap_time = int(text[1])
		except:
			pass
		if hour + nap_time >= 12:
			nap_time = 12 - hour

		#reapeats nap needed amount
		for a in range(nap_time):
			pass_time()
		UI.print1("you napped for {time} hours".format(time=nap_time))
		return

	if text[0] == "nap":
		nap()
		return


def random_events():
	chances = []

	#defines how often event appears based on location
	if current_location == "forest":
		chances = [
			["fight:wolf", 5],
			["fight:bear", 1],
			["trade:john", 2],
			["trade:jake", 1]
		]

	if current_location == "field":
		chances = [
			["trade:john", 1],
			["trade:jake", 1]
		]

	#choses random event
	event = ""
	a = 0
	for b in chances:
		a += b[1]
	b = random.random()*a
	for c in chances:
		if a <= c[1]:
			event = c[0]
			break
		a -= c[1]
	
	#adds new event
	global events
	events.append(event)


day = 0
hour = 0
event_chance = .25

def pass_time():
	global hour
	global day
	hour += 1
	if random.random() < event_chance:
		random_events()
	if hour >= 12:
		hour = 0
		day += 1