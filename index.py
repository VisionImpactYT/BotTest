import discord

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    await client.change_presence(activity=discord.Game(name="Your game here"))

client.run('MTE5MTA1OTAwODcwMjkxODc4OA.GqTo0x.hX1cjrwRJ8j1IVL8yPrwW_a1CR_YER2bIYMdDc')