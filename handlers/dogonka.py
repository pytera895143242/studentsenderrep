import random
import datetime
import pytz

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



def rangome_index_otvetok(text):
    number_otvetok = []
    array_link = text.split('\n')

    for link_and_kol in array_link:
        k = int((link_and_kol.split(' - '))[1])
        link = (link_and_kol.split(' - '))[0]
        for i in range(0,k):
            number_otvetok.append(link)

    random.shuffle(number_otvetok)
    return number_otvetok
