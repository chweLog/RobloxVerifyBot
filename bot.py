import discord
from server import run_server

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name}에 로그인 성공!')

@client.event
async def on_message(message):
    if message.content.startswith('!인증'):
        try:
            name = (message.content.split(" ")[1]).lower()
        except IndexError:
            embed = discord.Embed(title=':x: 오류', description='로블록스 닉네임을 입력해주세요', colour=0xFF0000)
            await message.channel.send(embed=embed)
            return
        f = open(f"{str(name)}.txt","w+").write(str(message.author))
        embed = discord.Embed(title=':white_check_mark: 성공', description='게임에 접속해주세요!', colour=0x7da565)
        await message.channel.send(embed=embed)

run_server()
client.run('OTc5NzE4MjYxMTE1NTkyNzE0.GD6qhG.PSQUnn7wIKoT9oTMgqtgJCjxb8ji-fSjUcJpUc')