import discord
import json
import random
from discord.ext import commands

client = commands.Bot(command_prefix="!", help_command=None)

polls = [] 

file = open("help1.txt", "r")
helptext = file.read()
file.close()

file = open("poll.json","r", encoding="utf8")
pollstring = file.read()
file.close()
polls = json.loads(pollstring) 

def save():
    pollstring = json.dumps(polls)
    file = open("poll.json","w")
    file.write(pollstring)
    file.close()

def GetPollID():
	x = (str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9))+str(random.randint(0,9)))
	global polls
	for y in polls:
		if y[0] == x:
			return (GetPollID)
	return (x)
		

@client.event
async def on_ready():
	print("Bot is ready")

#help - explain all comands
@client.command(aliases=['help'])
async def Help(ctx):
	await ctx.send(helptext)

#poll - shows all polls or one specific if specified
@client.command(aliases=['poll'])
async def Poll(ctx, *,PollID = ""):
	if PollID == "":
		for x in polls:
			await ctx.send("PollID: " + x[0] + "\nPoll name: " + x[1])
		return
	if PollID != "":
		for x in polls:
			if PollID.startswith(x[0]):
				await ctx.send("PollID: " + x[0] + "\nPoll name: " + x[1])
				return
	await ctx.send("Error 404: poll not found")

#create - creates poll and shows its ID
@client.command(aliases=['create'])
async def Create(ctx):
	PollID = GetPollID()
	polls.append([str(PollID),str(PollID) + " poll",[[1, "1 chose", []],[2, "2 chose", []],[3, "3 chose", []]]])
	await ctx.send("poll created with ID: "+str(PollID))
	save()

#name - changes polls name using its ID
@client.command(aliases=['name'])
async def Name(ctx, *, PollID=""):
	if PollID == "":
		await ctx.send("please use PollID")
		return
	if PollID != "":
		global polls
		for x in polls:
			if PollID.startswith(x[0]):
				x[1] = str(PollID.split(" ", 1)[1])
				await ctx.send("name changed to: " + str(PollID.split(" ",1)[1]))
				save()
				return
	await ctx.send("Error 404: poll not found")

#size - sets number of possible answers using its ID
@client.command(aliases=['size'])
async def Size(ctx, *, PollID=""):
	if PollID == "":
		await ctx.send("please use PollID")
		return
	if PollID != "":
		global polls
		for x in polls:
			if PollID.startswith(x[0]):
				y = PollID.split(" ", 2)[1]
				z = []
				for i in range(int(y)):
					z.append([int(i+1), str(i+1)+" chose", []])
				x[2] = z
				await ctx.send("size set to: " + str(y))
				save()
				return
	await ctx.send("Error 404: poll not found")

#choses - sets posible answers to text using its ID
@client.command(aliases=['choses'])
async def Choses(ctx, *, PollID=""):
	if PollID == "":
		await ctx.send("please use PollID")
		return
	if PollID != "":
		global polls
		for x in polls:
			if PollID.startswith(x[0]):
				y = PollID.split(" ", 2)[1]
				z = PollID.split(" ", 2)[2]
				for  i in x[2]:
					if i[0] == int(y):
						i[1] = str(z)
						await ctx.send("chose nr. " + str(y) + "was set to: " + str(z))
						save()
						return
	await ctx.send("Error 404: poll not found")

#delete - deletes polls using its ID
@client.command(aliases=['delete'])
async def Delete(ctx, *, PollID=""):
	if PollID == "":
		await ctx.send("please use PollID")
		return
	if PollID != "":
		global polls
		for x in range (len(polls)):
			y = polls[x]
			z = y[0]
			if PollID.startswith(z):
				polls.pop(x)
				await ctx.send("Poll deleted succesfully")
				save()
				return
	await ctx.send("Error 404: poll not found")

#vote - vote for chosen poll and vote using its ID and answer number
@client.command(aliases=['vote'])
async def Vote(ctx, *, PollID=""):	
	if PollID == "":
		await ctx.send("please use PollID")
		return
	if PollID != "":
		global polls
		for x in polls:
			if PollID.startswith(x[0]):
				y = PollID.split(" ", 2)[1]
				for i in x[2]:
					try:
						i[2].remove(str(ctx.message.author))
					except:
						pass
				for i in x[2]:
					if i[0] == int(y):
						i[2].append(str(ctx.message.author))
						await ctx.send("succesfully voted")
						save()
						return
				await ctx.send("succesfully removed your vote")
				save()
				return
	await ctx.send("Error 404: poll not found")

#votes - show votes of chosen poll using its ID
@client.command(aliases=['votes'])
async def Votes(ctx, *, PollID=""):
	if PollID == "":
		await ctx.send("please use PollID")
		return
	if PollID != "":
		global polls
		for x in polls:
			if PollID.startswith(x[0]):
				await ctx.send(x[2])
				return
	await ctx.send("Error 404: poll not found")

client.run(input("token: "))