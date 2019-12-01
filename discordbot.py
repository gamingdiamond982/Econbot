# We need a token, and account, but mobil can add that - since he's ES

import discord
import logging

# from keep_alive import keepAlive - Need to set up keep_alive and uptimerobot.com

TOKEN = os.environ.get("TOKEN") # Gets token
logging.basicConfig(level=logging.INFO)
client = discord.Client()

# Declaring Variables

prefix = "e;" # The prefix

# The Progam

@client.event
async def on_message(message): # When a message on a channel the bot can see is put out
  if message.content == prefix + "hello": # Just some test stuff
    await message.channel.send("Hello " + message.author.mention)
  if message.content == prefix + "
  # The help command
    
  if message.content == prefix + "help":
        embed = discord.Embed(title="help", description="The help page - you're here now!", color=message.author.color)
      

@client.event
async def on_ready():
  print('Logged in as')
  print(client.user.name)
  print(client.user.id)
  print('------------------')

keepAlive() # Keeps repl from shutting down

while True:
  try:
    client.run(TOKEN, bot=True)
  except:
    pass
