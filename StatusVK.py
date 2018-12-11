#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
	Получаем токен переходом по ссылке ниже:
	https://oauth.vk.com/authorize?client_id=2890984&scope=notify,photos,friends,audio,video,notes,pages,docs,status,questions,offers,wall,groups,messages,notifications,stats,ads,offline&redirect_uri=http://api.vk.com/blank.html&display=page&response_type=token
	В адресной строке берем токен он находится между access_token= и &expires_in:
	http://api.vk.com/blank.html#access_token= ТОКЕН &expires_in=0&user_id=437256099
	Полученный токен вставить в TOKEN = 'СЮДА'
"""

from datetime import datetime, date # $ pip install datetime
import pytz # $ pip install pytz
import vk_api # $ pip install vk_api
from re import findall
from time import sleep

TOKEN = ''	# токен
YOUR_TIME_ZONE = "Asia/Yekaterinburg" # Ваш часовой пояс

print('Запуск скрипта: ' + datetime.strftime(datetime.now(pytz.timezone(YOUR_TIME_ZONE)), "%H:%M:%S"))
vk_session = vk_api.VkApi(token = TOKEN)
try:
    vk = vk_session.get_api()
    try:
        while True:
            if datetime.strftime(datetime.now(pytz.timezone(YOUR_TIME_ZONE)), "%S") == "00":
                now = datetime.now(pytz.timezone(YOUR_TIME_ZONE))

                day = date(int(datetime.strftime(now, "%Y")), int(datetime.strftime(now, "%m")), int(datetime.strftime(now, "%d")))-date(int(datetime.strftime(now, "%Y")), 1, 1)
                if int(datetime.strftime(now, "%Y")) % 4 != 0:
                    percent = (day.days * 100) / 365
                else:
                    percent = (day.days * 100) / 366

                convert = findall(r'\d', datetime.strftime(now, "%H").zfill(2)+
                datetime.strftime(now, "%M").zfill(2)+
                datetime.strftime(now, "%d").zfill(2)+
                datetime.strftime(now, "%m").zfill(2)+
                datetime.strftime(now, "%Y").zfill(4))

                vk.status.set(text = '{0}&#8419;{1}&#8419;:{2}&#8419;{3}&#8419;\
                &#12288;&#12288;|&#12288;&#12288;\
                {4}&#8419;{5}&#8419;.{6}&#8419;{7}&#8419;.{8}&#8419;{9}&#8419;{10}&#8419;{11}&#8419;\
                &#12288;&#12288;|&#12288;&#12288;\
                Год завершен на {12}%'.format(*convert, float("{0:.3f}".format(percent))))
                sleep(59)
            else:
                sleep(1)
    except KeyboardInterrupt:
        print('Выключение скрипта: ' + datetime.strftime(datetime.now(pytz.timezone(YOUR_TIME_ZONE)), "%H:%M:%S"))
        exit()
except vk_api.AuthError as error_msg:
    print(error_msg)