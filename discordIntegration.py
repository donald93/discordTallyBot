import discord
import asyncio
import os

client = discord.Client()

@client.event
async def on_message(message):
  if message.content.startswith('!tb'):
    parameters = message.content.split(' ')
    if(parameters[1]).startswith('<@'):
      await client.send_message(message.channel, 'added to mom joke list')
      #just track them for whatever
    else:
      await client.send_message(message.channel, 'added to other type of list')
      #validate against list of approved lists
      #add next parameter to that list
    print (parameters)
    await client.send_message(message.channel, 'it worked')

client.run(os.environ['BOT_TOKEN'])