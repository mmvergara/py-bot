import discord
import Responses




async def send_message(message,user_message,is_private):
    try:
        response = Responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
  TOKEN ="MTExMTA1MDEwNTE1NjU0MjU0NQ.GGQgFa.H2b23juLUNbmku6vZ-WN5V6Qwc89kLtQzQhM6k"
  intents = discord.Intents.default()  
  intents.message_content = True
  client = discord.Client(intents=intents)

  @client.event
  async def on_ready():
      print(f"{client.user} BOT IS READY")

  @client.event
  async def on_message(message):
      if message.author == client.user:
          return
      
      username = str(message.author)
      print(message)
      
      user_message = str(message.content)
      channel = str(message.channel)
      print(f"{username} said {user_message} on {channel}")

      if(user_message[0] == "?"):
          user_message = user_message[1:]
          await send_message(message,user_message=user_message,is_private=True)
      else:
          await send_message(message,user_message=user_message,is_private=False)

  client.run(TOKEN)
          