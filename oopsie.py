import requests
from colorama import Fore, init
import os
import asyncio
import discord
from discord import Permissions
from discord.ext import commands
from discord.utils import get
import json
from urllib.request import Request, urlopen
import random
init(convert=True)

intro = f"""

                                              {Fore.RED}Selfbot running fag
                                ███▄,                              ,╓╖╓,
{Fore.CYAN}                     ╙█████░▒▄'                      ▄███▒▓▓╣╣╢╗
{Fore.CYAN}                        ▀▀█████▄,:                  ▐█████████▓▓▓▄
{Fore.CYAN}                            ` █▓░  █╖               ████████▓▄▓▀██
{Fore.CYAN}                              '██▄▄█▓▒╗,             ███████▀▀▀██▀
{Fore.CYAN}                                ▀█████▓▒╢╖            ▀██▄▄░░░░sT
{Fore.CYAN}                                  ██████▓╬╢╖          └███░░░░░─
{Fore.CYAN}                                   ▀█████▓╣╣▒╣         ███▄µ▒░░
{Fore.CYAN}                                     ▀████▓▓▓▓╫┐       ,██▀▀
{Fore.CYAN}                                       ████▓▓█▓▌@▓▒▓▒▄@▓█▓µ▌\  ┌╖
{Fore.CYAN}                                        ▐███████▓▓▓▓▓▒▄▌╢╢╣▀▒ ,░░░▒▒∩,,
{Fore.CYAN}                                         ▀███████▓█▓▓╩▒▀█▄▒▒▒▄▒░░░|░▒░░]▒
{Fore.CYAN}                                            ▀████████▓▓▓▒▀███Ñ▓▒░▒░░░░░▒▒▒
{Fore.CYAN}                                             ░`▀██████▓▓▓@▒███▒▒▒▒▀▒¢g▄╢▒░
{Fore.CYAN}                                                ▐█████▓▓▓▓╣▓▒██▌▒▒▒▒▒▒▐███▄
{Fore.CYAN}                                               ░ ██████▓▓▓▓▌Ñ▓▓▀██▄▒╢¼████æ▄
{Fore.CYAN}                                                 ▀███████▓███▓▓▓▓█░░░░▀▀▀▀██▄
{Fore.CYAN}                                                ╒█████████▓██▓▓▓▓█▒▒▒▒▒▒▒▒▒░░▄
{Fore.CYAN}                                               ,▓█╣▓██▓▓███████▓▓█▒▒▒╢╢▒▒▒▒▒▒░
{Fore.CYAN}                                              ▄▓█▓▄▓███▓█████████████▄▒╢▓╣▓▓╜
{Fore.CYAN}                                             ▐████▓▓██▓▓▓▓▒▒╢╣╣▒▒▒▀█▀█-└▀▀
"""

with open('config.json') as f:
    config = json.load(f)
token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')





   
def Init():
    os.system("cls")
    print(intro)
    
    try:
        Exploit.run(token, bot=False, reconnect=True)
        os.system(f'title Auto discvent -- fag')
    except discord.errors.LoginFailure:
        print(f"{Fore.RED}[ERROR] {Fore.YELLOW}Improper token has been passed" + Fore.RESET)
        os.system('pause >NUL')

def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)

        return inner

    return outer

class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()

Exploit = discord.Client()
Exploit = commands.Bot(
    description='fag nuuts',
    command_prefix=prefix,
    self_bot=True
)
Exploit.remove_command('help')

@Exploit.event
async def on_message(message):
    time = random.randint(3, 5)
    if message.channel.id == 789652165609521192:
          return
    if message.author.id == 788602856185790495:
                if message.content:
                    if 'Repeat after me:' in message.content:
                        matcher = message.content.split('Repeat after me:')[1].replace(f'\u200e', '')
                        print(f"Message detected! sending in {time} seconds...")
                        await asyncio.sleep(time)
                        print("Message sent!")
                        await message.channel.send(matcher.replace('`', ''))
                        print(message.content)
                    if "Repeat after me:" in message.content:
                        matcher = message.content.split('Memorize the emoji pattern:')[
                            1].replace(f'\u200e', '')
                        print(f"Message detected! sending in {time} seconds...")
                        await asyncio.sleep(time)
                        print("Message sent!")
                        await message.channel.send(matcher.replace(' ', ''))
                    if "I'm thinking of a number between" in message.content:
                        print(f"Message detected! sending each message every 2 seconds...")
                        await asyncio.sleep(2)
                        await message.channel.send(random.randint(1, 40))
                        print("Message sent!")
                        await asyncio.sleep(2)
                        await message.channel.send(random.randint(1, 40))
                        print("Message sent!")
                        await asyncio.sleep(2)
                        await message.channel.send(random.randint(1, 40))
                        print("Message sent!")
                        await asyncio.sleep(2)
                        await message.channel.send(random.randint(1, 40))
                        print("Message sent!")
                        await asyncio.sleep(2)
                        await message.channel.send(random.randint(1, 40))
                        print("Message sent!")
                        await asyncio.sleep(2)
                        await message.channel.send(random.randint(1, 40))
                        print("Message sent!")
                        await asyncio.sleep(2)
                    if "Unscramble the word:" in message.content:
                        matcher = message.content.split('Unscramble the word:')[1].replace(f'\u200e', '')
                        Scrabled = matcher.replace('`', '')
                        print(f"word detected, sending in {time} seconds")
                        v = Vect2Int(Word2Vect(Scrabled))
                        tp = ind.get(v, 'Word Not in Dictionary.')
                        ass = ' '.join(map(str, tp)) 
                        if ass == 'W o r d   N o t   i n   D i c t i o n a r y .':
                            print('unknown word, Add to dictionary manually')
                            pass
                        else:
                            await asyncio.sleep(time)
                            await message.channel.send(ass)
                            print(f"Message '{ass}' sent after {time} seconds!")




def RemoveFromList(thelist, val):
    return [value for value in thelist if value != val]
    
def GetDic():
    try:
        dicopen = open("DL.txt", "r")
        dicraw = dicopen.read()
        dicopen.close()
        diclist = dicraw.split("\n")
        diclist = RemoveFromList(diclist, '')
        return diclist
    except FileNotFoundError:
        print("No Dictionary!")
        return 

def Word2Vect(word):
    l = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    v = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    w = word.lower()
    wl = list(w)
    for i in range(0, len(wl)):
        if wl[i] in l:
            ind = l.index(wl[i])
            v[ind] += 1
    return v
    
def Vect2Int(vect):
    pv = 0
    f = 0
    for i in range(0, len(vect)):
        wip = (vect[i]*(2**pv))
        f += wip
        pv += 4
    return f

def Ints2Dic(dic):
    d = {}
    for i in range(0, len(dic)):
        v = Word2Vect(dic[i])
        Int = Vect2Int(v)
        if Int in d:
            tat = d.get(Int)
            tat.append(dic[i])
            d[Int] = tat
        elif Int not in d:
            d[Int] = [dic[i]]
    return d

d = GetDic()
ind = Ints2Dic(d)



if __name__ == '__main__':
    Init()
    GetDic()
    
