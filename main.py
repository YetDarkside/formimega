# -*- coding: utf8 -*-
import discord
from discord.ext import commands
import asyncio
import random
config = {
	'token': '',
	'OwnerID': '600616636495560707',
}
replika = ['Запишу на ваш счёт.','Угощайтесь!', 'Жду вашего следующего заказа!']

extensions = ['cogs.alc']



sussy = ['https://c.tenor.com/z2JlZku6XtgAAAAd/red-sus.gif', 'https://avatars.mds.yandex.net/i?id=4546ab7fb0d2c9dbdbad8c3dc442446f-4580923-images-thumbs&n=13', 'https://i.ytimg.com/vi/7uZCzfg2Ego/maxresdefault.jpg', 'https://c.tenor.com/UNsLn7iQxfEAAAAd/among-us-anong-us-drip.gif']
bot = commands.Bot(
    command_prefix=';',
    strip_after_prefix=True,
    case_insensitive=True,
    intents=discord.Intents.all(),
    help_command=None
)

def vips():
	def inner(ctx):
		_all=[ 600616636495560707, 790218504623489025, 689148385449738374, 725968048980361217, 717596465475747910, 644199299466526730, 835467766584311819, 419892040726347776, 775374324630552577, 419892040726347776]
		if not ctx.author.id in _all:
			return False
		return ctx.author.id in _all
	return commands.check(inner)


@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=';help'), status=discord.Status.idle)

@bot.command(name='Вип')
async def vipss(ctx):
	await ctx.reply('**Q:** Как стать Випом?\n **A:** Никак. По нескольким причинам.\n Первая: взять нечего взамен.\n Вторая: Не стоит впринципе особо чего-либо.\n Даю лишь Своим друзьям или хорошим знакомым. Выпрашивать не пытайтесь.')

@bot.command(name='Версия')
async def vversion(ctx):	
	vers = discord.Embed(title='Версия: 1.0.3-Beta.')
	vers.add_field(name='Новый хостинг!', value='*Теперь бот перешёл на платный хостинг! Спрасибо djoh#2071 за спонсорство и MagMigo_♡#6065 за поддержку с технической стороны! *', inline=False)
	vers.add_field(name='Прочее', value='*Изменение ошибок.*', inline=False)
	vers.set_thumbnail(url='https://assets.stickpng.com/images/5a5a6d1814d8c4188e0b088b.png')
	await ctx.send(embed=vers)
@bot.command(name='help')
async def help(ctx):
	hel = discord.Embed(title='Команды:')
	hel.add_field(name=';help', value='*Список доступных команд*', inline=False)
	hel.add_field(name=';Меню', value='*Меню напитков и закусок у бота*', inline=False)
	hel.add_field(name=';Вип', value='*Ответит на все ваши вопросы по поводу ВИП статуса.*', inline=False)
	hel.add_field(name=';Версия', value='*Покажет текущую версию бота и напишет все его последние изменения.*', inline=False)
	hel.add_field(name=';sus (Only for VIPs)', value='*???*', inline=False)
	await ctx.send(embed=hel)

@vips()	
@bot.command(name='sus')
async def suss(ctx):
	await ctx.message.delete()
	sus = discord.Embed(title='Some of Cringe. Bone Appetit.')
	sus.set_image(url=random.choice(sussy))
	await ctx.send(embed=sus)
#import sus
@bot.command(name='Меню')
async def menu(ctx):
	alc = discord.Embed(title='Наше меню:', description='***Алкоголь(18+):***')
	alc.set_thumbnail(url='https://i2.wp.com/www.alzahraprint.com/wp-content/uploads/2017/05/menu1.jpg?fit=1920%2C1278&ssl=1')
	alc.add_field(name='-Виски (;Виски)', value='*Виски – это алкогольный напиток, изготавливаемый путем сбраживания зерновых культур, таких как рожь, ячмень, пшеница или кукуруза.*', inline=False)
	alc.add_field(name='-Пиво светлое, нефильтрованное (;СветлПиво)', value='*Светлое Нефильтрованное Пиво - это Не прошедшее процедуру пастеризации, то есть «живое». У него ярко выраженный вкус, насыщенный аромат, а главное — есть составляющие, которые довольно полезны для человека*', inline=False)
	alc.add_field(name='-Коньяк (;Коньяк)', value='*Конья́к — крепкий алкогольный напиток (разновидность бренди), производимый из определённых сортов винограда по особой технологии в департаменте Шаранта.*', inline=False)
	alc.add_field(name='-Водка (;Водка)', value='*Во́дка — крепкий алкогольный напиток, бесцветный водно-спиртовой раствор с характерным вкусом и ярко выраженным спиртовым запахом.*', inline=False)
	alc.add_field(name='-Красное Вино (;КраснВино)', value='*Кра́сное вино́ — вино, произведённое из красных сортов винограда по технологии, обеспечивающей переход антоцианов из кожицы в сусло. Красные вина богаты дубильными веществами и поэтому обладают пряными первичными ароматами.*', inline=False)
	alc.set_footer(text='Черезмерное употребление алкоголя вредит вашему здоровью. Алкоголь не продаётся лицам младше 18 лет.')
	await ctx.send(embed=alc)

	drink = discord.Embed(description='**Безалкогольные напитки:**')
	drink.set_thumbnail(url='https://s1.1zoom.ru/big3/871/Drinks_Cocktail_Lemons_439370.jpg')
	drink.add_field(name='-CocaCola (;Кола)', value='*Газированный безалкогольный напиток, производимый компанией Coca-Cola.*', inline=False)
	drink.add_field(name='-Schweppes (;Швепс)', value='*Газированный безалкогольный напиток, основанный Якобом Швеппом в 1783 году. Широкоизвестный напиток, который часто покупают в паре с джином. Их сочетание с лаймом получается просто великолепным на вкус.*', inline=False)
	drink.add_field(name='-Schweppes "Дерзкий Гранат" (;ГранШвепс), (Only for VIPs)', value='*Тот же Швепс, но более вкусный и сладкий. Со вкусом Граната.*', inline=False)
	drink.add_field(name='-Яблочный Сок (;ЯблСок)', value='*Яблочный сок-это фруктовый сок, получаемый путем мацерации и прессования яблока.*', inline=False)
	drink.add_field(name='-Чёрный Чай (;ЧёрнЧай)', value='*Вид чая, подвергающийся полной ферментации в течение от двух недель до месяца.*', inline=False)
	drink.add_field(name='-Чай Аббакио (;АббЧай), (Only for VIPs)', value='*Кто знает, тот знает...*', inline=False)
	drink.add_field(name='-Кофе (;Кофе)', value='*Сваренный напиток, приготовленный из обжаренных кофейных зерен, семян ягод некоторых цветущих растений рода Coffea.*', inline=False)
	drink.add_field(name='-Молочный Шоколадный Коктейль (;ШокКоктейль)', value='*Молочный коктейль — десертный напиток на основе молока и мороженого, один из символов американской кухни. Имеет шоколадный вкус.*', inline=False)
	drink.add_field(name='-Молочный Банановый Коктейль (;БананКоктейль), (Only for VIPs)', value='*Молочный Коктейль со вкусом банана.*', inline=False)
	await ctx.send(embed=drink)
	
	food=discord.Embed(description='**Еда и закуски:**')
	food.set_thumbnail(url='https://elleonora.ru/wp-content/uploads/2017/09/zakuski-fotogrfa-i-limuzin-8.jpg')
	food.add_field(name='-Сэндвич с ветчиной и сыром (;СэндвичВС)', value='*Сэндвич - это Вид бутерброда, состоящего из двух кусочков хлеба и какой-либо начинки между ними. В данном случае там находится ветчина, сыр и пару листов салата.*', inline=False)
	food.add_field(name='-Блины с бананом и шоколадом (;БлиныШБ)', value='*Блины — блюдо русской, немецкой, кавказской кухонь, выпекаемое из жидкого теста на сковороде. Начинка состоит из растопленного тёплого шоколада и кусочков банана.*', inline=False)
	await ctx.send(embed=food)

	
@bot.command(name='Кола')
async def Cola(ctx):
	cola = discord.Embed(title='Вот ваша кола!', description=f'{random.choice(replika)}')
	cola.set_image(url='https://cdn.setafi.com/wp/uploads/2021/06/tallypress.com1_.jpg')
	await ctx.send(embed=cola)

@bot.command(name='Швепс')
async def schv(ctx):
	sch = discord.Embed(title='Вот ваш Швепс!', description=f'{random.choice(replika)}')
	sch.set_image(url='https://solod-suslo.ru/wp-content/uploads/5e73ff475f7be771468cc126c05773062.jpg')
	await ctx.send(embed=sch)
	
@vips()
@bot.command(name='ГранШвепс')
async def gschv(ctx):
	gsch = discord.Embed(title='Вот ваш Гранатовый Швепс!', description=f'{random.choice(replika)}')
	gsch.set_image(url='https://irecommend.ru/sites/default/files/imagecache/copyright1/user-images/1065475/qOmnjZqJHy3n5pOhDHLQg.jpeg')
	await ctx.send(embed=gsch)

@bot.command(name='ЧёрнЧай')
async def Bltea(ctx):
	bltea = discord.Embed(title='Вот ваш чёрный чай!', description=f'{random.choice(replika)}')
	bltea.set_image(url='https://cf.kizlarsoruyor.com/q16003824/ff360ed1-99e9-4681-83c8-ba03c07a7e97.jpg')
	await ctx.send(embed=bltea)
	
@vips()	
@bot.command(name='АббЧай')
async def AbbTea(ctx):
	abb = discord.Embed(title='Вот ваш чай...', description=f'{random.choice(replika)}')
	abb.set_image(url='https://coub-attachments.akamaized.net/coub_storage/coub/simple/cw_timeline_pic/4b6eef55765/9c58b58d66a058038a730/1545756308_image.jpg')
	await ctx.send(embed=abb)

@bot.command(name='ЯблСок')
async def appju(ctx):
	jua = discord.Embed(title='Вот ваш Яблочный Сок!', description=f'{random.choice(replika)}')
	jua.set_image(url='https://mircocktails.ru/wp-content/uploads/2019/02/YAblochnyj-sok-43.jpg')
	await ctx.send(embed=jua)

@bot.command(name='Кофе')
async def coffee(ctx):
	cof = discord.Embed(title='Вот ваш Кофе (кофе - он, а не оно)!', description=f'{random.choice(replika)}')
	cof.set_image(url='https://img4.goodfon.ru/original/1920x1080/a/d1/zavtrak-chashka-kofe-bliudtse-penka.jpg')
	await ctx.send(embed=cof)
	
@bot.command(name='ШокКоктейль')
async def chok(ctx):
	schc = discord.Embed(title='Вот ваш Шоколадный Милкшейк!', description=f'{random.choice(replika)}')
	schc.set_image(url='https://i.pinimg.com/originals/78/f7/1f/78f71f5363ae650da238980a238f8c7e.jpg')
	await ctx.send(embed=schc)

@vips()	
@bot.command(name='БананКоктейль')
async def banan(ctx):
	bc = discord.Embed(title='Вот ваш Банановый Милкшейк!', description=f'{random.choice(replika)}')
	bc.set_image(url='https://eclecticrecipes.com/wp-content/uploads/2014/03/milkshake-3.jpg')
	await ctx.send(embed=bc)
	
@bot.command(name='СэндвичВС')
async def sandvvc(ctx):
	svc = discord.Embed(title='Вот ваш Сэндвич с ветчиной и сыром!', description=f'{random.choice(replika)}')
	svc.set_image(url='https://kartinkin.net/uploads/posts/2021-07/1627728730_19-kartinkin-com-p-tost-s-vetchinoi-i-sirom-yeda-krasivo-foto-24.jpg')
	await ctx.send(embed=svc)


@bot.command(name='БлиныШБ')
async def pancchb(ctx):
	chb = discord.Embed(title='Вот ваши блинчики)', description=f'{random.choice(replika)}')
	chb.set_image(url='http://klublady.ru/uploads/posts/2022-02/1644698253_33-klublady-ru-p-blini-s-bananom-i-shokoladom-foto-33.jpg')
	await ctx.send(embed=chb)

async def main():
     ignore_cogs = ["__pycache__"]
     await bot.start(config['token'])
     for i in extensions:
         if i not in ignore_cogs:
             await bot.load_extension(i)

asyncio.run(main())
