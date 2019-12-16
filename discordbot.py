# We need a token, and account, but mobil can add that - since he's ES

import discord
import logging

# from keep_alive import keepAlive - Need to set up keep_alive and uptimerobot.com

TOKEN = os.environ.get("TOKEN") # Gets token - we don't have the token yet
logging.basicConfig(level=logging.INFO)
client = discord.Client()

# Declaring Variables

prefix = "ee" # The prefix

server = "simdem" # Just a placeholder, IDK simdem's server id

# The Progam

@client.event
async def on_message(message): # When a message on a channel the bot can see is put out
  if message.content == prefix + "balance":
    try:
      print(str(get_account_balance(message.author.id, server)))
    except:
      await message.channel.send("An error has occured. Are you sure you have an account made?")
      
if message.content == prefix + "help": # The help command
  embed = discord.Embed(title="help", description="The help page - you're here now!", color=message.author.color) # Sets up the embed
  embed.add_field(name="Prefix", value="Prefix all statements with " + prefix + '"', inline=False) # Adds lines to the embed

@client.event
async def on_ready(): # Lets the console owner see it's booted up
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------------------')

keepAlive() # Keeps repl from shutting down

while True:
  try:
    client.run(TOKEN, bot=True) # Runs the bot
  except:
    pass
