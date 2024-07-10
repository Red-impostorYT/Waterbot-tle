import discord
import time

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!water'):
            await message.reply('Starting...', mention_author=True)
            time.sleep(5)
            while True:
                    irl_time = time.strftime("%I:%M %p")
                    await message.reply('Drink Water!', mention_author=True)
                    time.sleep(5)
                    await message.reply(irl_time, mention_author=True)
                    time.sleep(9000) #2.5 Hours

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

client.run('token') #Your bot token (Don't share with people!!)
