# --------------------------------------
# oh rjain, Adding alot of invisable characters doesnt do anything anymore
# At this point, Im making this just to piss yall off
# have a happy christmas!
# i never left the server ;)
# --------------------------------------


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
import re
init(convert=True)

intro = f"""

                                              {Fore.RED}Selfbot running fag
{Fore.CYAN}                     ███▄,                              ,╓╖╓,
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

# -------------------- Selfbot stuff -----------------------

with open('config.json') as f:
    config = json.load(f)
token = config.get('token')
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

# -------------------- Get message and send -----------------------

@Exploit.event
async def on_message(message):
    time = random.randint(3, 5)
    if message.author.id == 788908970852352031:
                if message.content:
                    damessage = str(message.content).replace(u'\u200e', '').replace(u'\u200b', '').replace(u'\u200c', '') # removes all the invis nasty usless stuff 
                    
                    # -------------------- Repeats the message -----------------------
                    if 'Repeat after me:' in damessage:
                        matcher = damessage.split('Repeat after me:')[1].replace(f'\u200e', '') # fweak 
                        print(f"{Fore.YELLOW}Message detected! sending in {time} seconds...")
                        await asyncio.sleep(time)
                        print("Message sent!")
                        await message.channel.send(matcher.replace('`', ''))
                    
                    # -------------------- Counting candies -----------------------
                    if "Count the number of candies!" in damessage:                         # me
                        matcher = damessage.split('Count the number of candies!')[1]
                        yoo = matcher.replace('🍬', "-pog")
                        fart = list(yoo.split("-"))        
                        print(f"{Fore.YELLOW}Message detected! sending in {time} seconds...")
                        await asyncio.sleep(time)
                        print(f"{Fore.GREEN}Message sent!")
                        await message.channel.send(fart.count("pog"))
                    
                    # -------------------- Emoji pattern -----------------------
                    if "emoji" in damessage:                                    # fweak 
                        matcher = damessage.split('Memorize the emoji pattern:')[1]
                        print(f"{Fore.YELLOW}Message detected! sending in {time} seconds...")
                        await asyncio.sleep(time)
                        print("Message sent!")
                        await message.channel.send(matcher.replace(' ', ''))                   
                    
                    # -------------------- Random number -----------------------
                    if "I'm thinking of a number between" in damessage:                  # me
                        fart = random.randint(1, 10)
                        print(f"Message detected! sending {fart} messages every 2 seconds...")
                        await asyncio.sleep(2)
                        for x in range(0, fart):
                            await message.channel.send(random.randint(1, 40))
                            await asyncio.sleep(2)
                    
                    # -------------------- Word unscramble -----------------------
                    if "Unscramble the word:" in damessage:                                # me
                        matcher = damessage.split('Unscramble the word:')[1].replace(f'\u200e', '')
                        Scrabled = matcher.replace('`', '')
                        print(f"{Fore.YELLOW}word detected, sending in {time} seconds")
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
                            
                        # -------------------- Colored emoji -----------------------                      # legit all fweak mad man
                    dotsOrder = {
                        '🔵': {
                            'color': 'blue circle?',
                        },
                        '🟢': {
                            'color': 'green circle?'
                        },
                        '⚪': {
                            'color': 'white circle?'
                        }
                    }
                        

                    if 'Remember the order:' in damessage:
                                print(f"{Fore.YELLOW}word detected, waiting for edit...")
                                dotsFromMessage = damessage.split(
                                    'order:')[1].strip().split('\n')

                                for combos in dotsFromMessage:
                                    combination = combos.split(' ')
                                    dot = combination.pop(0)
                                    text = ' '.join(combination)

                                    dotsOrder[dot]['text'] = text

                                ResponeFromEdit = await Exploit.wait_for('message_edit', check=lambda old, new: new.id == message.id)

                                whatTheyWant = ResponeFromEdit[1].content.replace(
                                    u'\u200e', '').replace(u'\u200b', '').split('to the ')[1]

                                for dot in dotsOrder:
                                    order = dotsOrder[dot]
                                    if order['color'] == whatTheyWant:
                                        print(f"{Fore.GREEN}word detected, waiting {time} seconds to send...")
                                        await asyncio.sleep(time)
                                        await message.channel.send(order['text'])
                                        print(f"{Fore.GREEN}sent!")
                                        break
    


# -------------------- dictionary stuff -----------------------

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

def Convert(string): 
    li = list(string.split(":")) 
    return li 

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


# -------------------- start -----------------------
if __name__ == '__main__':
    Init()
    GetDic()
    
