from aiogram import types
from misc import dp,bot
import asyncio
import random
import datetime
import pytz
from .sqlit import get_caption,reg_user,get_caption2
reg_user(1)
content_id = -1002091292683 # контент для перекрытия подборок
content_pp = -1002053337757 # контент для партнерок ( основные посты)

link0 = -1001628459993 #Студентки


# link2 = -1001756828717 #Доманшка
# link3 = -1001622262140
# link4 = -1001652652655
# link5 = -1001754189943
# link6 = -1001669219428

channels = [link0]

len_kontent = [2, 786]
len_partnerk = [30 , 56]


async def nite_pp(chat_id): # ЭТО НОЧНОЙ ПРОГРЕВ 22 - 06 { выйдет 5}
    print('зашелл')
    try:
        try:
            q1 = await bot.copy_message(from_chat_id=content_pp, chat_id=chat_id, message_id=random.randint(len_partnerk[0], len_partnerk[1] - 1),parse_mode='html') # рандомный пост
            await asyncio.sleep(random.randint(2000,4000))
            await bot.delete_message(chat_id = chat_id, message_id=q1.message_id)
        except:
            pass


        try:
            q1 = await bot.copy_message(from_chat_id=content_pp, chat_id=chat_id, message_id=random.randint(len_partnerk[0], len_partnerk[1] - 1),parse_mode='html')  # рандомный пост
            await asyncio.sleep(random.randint(2000, 4000))
            await bot.delete_message(chat_id=chat_id, message_id=q1.message_id)
        except:
            pass

        try:
            q1 = await bot.copy_message(from_chat_id=content_pp, chat_id=chat_id, message_id=random.randint(len_partnerk[0], len_partnerk[1] - 1),parse_mode='html')  # рандомный пост
            await asyncio.sleep(random.randint(2000, 4000))
            await bot.delete_message(chat_id=chat_id, message_id=q1.message_id)
        except:
            pass

        try:
            q1 = await bot.copy_message(from_chat_id=content_pp, chat_id=chat_id, message_id=random.randint(len_partnerk[0], len_partnerk[1] - 1),parse_mode='html')  # рандомный пост
            await asyncio.sleep(random.randint(2000, 4000))
            await bot.delete_message(chat_id=chat_id, message_id=q1.message_id)
        except:
            pass

        try:
            q1 = await bot.copy_message(from_chat_id=content_pp, chat_id=chat_id, message_id=random.randint(len_partnerk[0], len_partnerk[1] - 1),parse_mode='html')  # рандомный пост
            await asyncio.sleep(random.randint(2000, 4000))
            await bot.delete_message(chat_id=chat_id, message_id=q1.message_id)
        except:
            pass
    except:
        pass








async def random_pp(): # ЭТО РАНДОМНЫЙ ПОСТ НА ПАРТНЕРКИ
    for chaneel in channels:
        try:
            await bot.copy_message(from_chat_id=content_pp, chat_id=chaneel,message_id=random.randint(len_partnerk[0], len_partnerk[1] - 1), parse_mode='html')
        except:
            pass


async def posting(cap = 1): # ЭТО ПЕРЕКРЫТИЯ ПОДБОРОК
    for chaneel in channels:
        try:
            if cap == 1:
                try:
                    await bot.copy_message(caption = get_caption()[0][0],from_chat_id=content_id,chat_id= chaneel,message_id = random.randint(len_kontent[0], len_kontent[1] - 1), parse_mode='html')
                except:
                    try:
                        await bot.copy_message(caption=get_caption()[0][0], from_chat_id=content_id, chat_id=chaneel,message_id=random.randint(len_kontent[0], len_kontent[1] - 1), parse_mode='html')
                    except: pass

            else:
                try:
                    await bot.copy_message(caption=get_caption2()[0][0], from_chat_id=content_id, chat_id=chaneel,message_id=random.randint(len_kontent[0], len_kontent[1] - 1), parse_mode='html')
                except:
                    try:
                        await bot.copy_message(caption=get_caption2()[0][0], from_chat_id=content_id, chat_id=chaneel,message_id=random.randint(len_kontent[0], len_kontent[1] - 1), parse_mode='html')
                    except:
                        pass
        except:
            pass





def second_time(finish_data):
    hours_f = int(finish_data[0:2]) #Часы финиша
    min_f = int(finish_data[3:]) #Минуты финиша
    second_f = 0

    hours_now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).hour
    min_now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).minute
    seconf_now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).second


    time_now = datetime.datetime(year = 2022,month = 1,day = 1, hour = hours_now,minute = min_now,second = seconf_now)
    time_finish = datetime.datetime(year = 2022,month = 1,day = 1, hour = hours_f,minute = min_f,second = second_f)

    delta = (time_finish-time_now).seconds
    return delta



async def sender():
    while True:
        await asyncio.sleep(5)
        hours_now = datetime.datetime.now(pytz.timezone('Europe/Moscow')).hour

        #if  hours_now == 9 or hours_now == 10 or hours_now == 11 or hours_now == 14 or hours_now == 17 or hours_now == 18 or hours_now == 21 or hours_now == 22:
        if hours_now == 14:
            if hours_now == 9:
                t = second_time("09:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await posting(cap=1)
                await posting(cap=2)

            elif hours_now == 10:
                t = second_time("10:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await posting(cap=2)

            elif hours_now == 11:
                t = second_time("11:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await random_pp()

            elif hours_now == 14:
                t = second_time("14:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await posting(cap=1)
                await posting(cap=2)

            elif hours_now == 17:
                t = second_time("17:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await posting(cap=1)
                await posting(cap=2)

            elif hours_now == 18:
                t = second_time("18:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await random_pp()

            elif hours_now == 21:
                t = second_time("21:59")
                print(f"Спим {t} секунд")
                await asyncio.sleep(t)
                await posting(cap=1)
                await posting(cap=2)

            elif hours_now == 22:
                await nite_pp(link0)






        await asyncio.sleep(1800) #Проверяем каждые 30 минут

