import discord
import os
import requests
import json
import random

#searches for the discord client
client = discord.Client()

#STATUS CODE CHECK
def get_statusCode():
  response = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=500') #fetches data from the api
  response = (response.status_code)
  return(response)

def getFact():
  response = requests.get('https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=500') #currently down
  json_data = json.loads(response.text)
  for i in json_data:
    newResponse = i['text'] #gets the text key for random facts
  return(newResponse)

def getCatPic():
  response = requests.get('https://api.thecatapi.com/v1/images/search')
  json_data = json.loads(response.text)
  for i in json_data:
    newResponse = i['url'] #gets the url key for cat pictures
  return(newResponse)


def getCatBreed():
  value = [] 
  response = requests.get('https://api.thecatapi.com/v1/breeds')
  json_data = json.loads(response.text)
  for i in json_data: 
    newResponse = i["name"]#WIP: will get a random cat breed and information
    value.append(newResponse)
  return(value)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client)) #informs on console that the bot is logged in on discord

@client.event
async def on_message(message):
  if message.author == client.user:
    return #allows bot to respond to messages
  
  #REQUESTS THAT USERS CAN USE
  if message.content.startswith('!status code'):
    response = get_statusCode()
    await message.channel.send(response)

  if message.content.startswith('!fact'):
    fact = getFact()
    await message.channel.send(fact)
  
  if message.content.startswith('!cat pic'):
    pic = getCatPic()
    await message.channel.send(pic)

  if message.content.startswith('!cat breed'):
    breed = getCatBreed()
    breed = random.choice(breed)
    await message.channel.send(breed) #WIP

  if message.content.startswith('!about'):
    await message.channel.send('Meow! My name is CatBot.\nI will always send images at your request! Type type !cat pic if you want a cat picture! Type !about if you want to hear this message again.')







#reads the token and runs the bot

client.run(os.getenv('TOKEN')) #hidden