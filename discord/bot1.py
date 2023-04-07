import discord
import time
from discord.ext import commands

client = commands.Bot(command_prefix="!")

filtered_words = ["bad word", "badword"]
filtered_URLs = ["free nitro", "freenitro"]

@client.event
async def on_ready():
	print("Bot is ready")

@client.event
async def on_message(msg):
	for word in filtered_words:
		if word.lower() in msg.content.lower():
			await msg.delete()

	for word in filtered_URLs:
		if word.lower() in msg.content.lower() and "http".lower() in msg.content.lower():
			await msg.delete()

	await client.process_commands(msg)
	
@client.command(aliases=['say'])
async def Say(ctx, *, text = "you didnt told me what to say so whats up?"):
	await ctx.send(text)
	
@client.command(aliases=['filter'])
@commands.has_permissions(manage_messages = True)
async def Filter(ctx, *, text):
	filtered_words.append(text.lower())
	await ctx.send(text + " was added to flitered words")

@client.command(aliases=['filterclear'])
@commands.has_permissions(manage_messages = True)
async def FilterClear(ctx, *, text):
	filtered_words.remove(text.lower())
	await ctx.send(text + " was removed from flitered words")

@client.command(aliases=['URLfilter'])
@commands.has_permissions(manage_messages = True)
async def URLFilter(ctx, *, text):
	filtered_words.append(text.lower())
	await ctx.send(text + " was added to flitered URL words")

@client.command(aliases=['URLfilterclear'])
@commands.has_permissions(manage_messages = True)
async def URLFilterClear(ctx, *, text):
	filtered_words.remove(text.lower())
	await ctx.send(text + " was removed from flitered URL words")

@client.command(aliases=['test'])
async def Test(ctx):
	await ctx.send("P33P33P00P00")
	await ctx.send(ctx.message.author)
	
@client.command(aliases=['clear'])
@commands.has_permissions(manage_messages = True)
async def Clear(ctx, amount=2):
	await ctx.channel.purge(limit = amount)

@client.command(aliases=['kick'])
@commands.has_permissions(kick_members = True)
async def Kick(ctx, member : discord.Member, *, reason="No reason provided"):
	await member.send("you have been kicked because: "+reason)
	await member.kick(reason=reason)

@client.command(aliases=['ban'])
@commands.has_permissions(ban_members = True)
async def Ban(ctx, member : discord.Member, *, reason="No reason provided"):
	await ctx.send(member.name + " has been Baned because: "+reason)
	await member.ban(reason=reason)

@client.command(aliases=['unban'])
@commands.has_permissions(ban_members = True)
async def Unban(ctx, *,member):
	banned_users = await ctx.guild.bans()
	member_name, member_disc = member.split('#')

	for banned_entry in banned_users:
		user = banned_entry.user

		if(user.name, user.discriminator)==(member_name,member_disc):
			
			await ctx.guild.unban(user)
			await ctx.send(member_name + " has been unbanned!")
			return

	await ctx.send(member + " was not found ")

client.run(input("token: "))
