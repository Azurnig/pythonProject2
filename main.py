import os
import openai
import discord
from discord.ext import commands

openai.api_key = os.getenv("seckety")

intents = discord.Intents.all()
intents.message_contents = True

client = commands.Bot(command_prefix='/', intents=intents)


@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} - {client.user.id}')


@client.command()
async def ask(ctx, *, question):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Q: {question}\nA:",
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    answer = response.choices[0].text.strip()
    await ctx.send(answer)

client.run(os.getenv("seckey"))
