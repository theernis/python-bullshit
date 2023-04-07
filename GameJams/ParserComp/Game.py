import sys
import UI
import Handler


start1 = "game loaded\n"

#displays start menu
def start_menu():
	UI.spell(UI.slider(1,1,25),5)
	UI.print1(start1)
	Handler.command_handler("help")
	Handler.event_command_handler("help")
	a = ""
	while a.lower() != "y":
		a = input("<do you want to play? (y/n)> ")
		if a.lower() == "n":
			sys.exit(0)
		elif a.lower() == "y":
			pass
		else:
			UI.print1("i didnt understand you")
	Handler.tags.append("start")


#main game loop
def game_loop():

	#tag handling part
	Handler.tag_handler(Handler.tags)

	#event handling part
	if len(Handler.events) > 0:
		Handler.event_handler(Handler.events[0])

	#to continue tags or event s if new are added
	if len(Handler.tags) == 0:

		#player input handling part
		player_input = UI.input1("<> ")
		Handler.command_handler(player_input)
		Handler.event_command_handler(player_input)

	game_loop()

start_menu()
game_loop()