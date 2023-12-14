import telebot 
from telebot import types 
import psycopg2
from config import host, user, password, db_name
import time
import utils

admin = 5359516739
variable = utils.Variable()
bot = telebot.TeleBot("6727983935:AAHV3CGQwY1mCJ0JORZeb5WiCbbXAGlziCo")

@bot.message_handler(commands=['start'])
def stttt(message):
  k = types.InlineKeyboardMarkup(row_width=2)
  k1 = types.InlineKeyboardButton(text="РАСЧЕТ / ОТСЛЕЖИВАНИЕ", web_app=types.WebAppInfo(url="https://main--dancing-cheesecake-968061.netlify.app"))
  k2 = types.InlineKeyboardButton(text="КУРС",callback_data="1")
  k3 = types.InlineKeyboardButton(text="ВОПРОСЫ / ОТВЕТЫ",callback_data="2")
  k4 = types.InlineKeyboardButton(text="ОТЗЫВЫ",callback_data="3")
  k5 = types.InlineKeyboardButton(text="МЕНЕДЖЕР",url="https://t.me/dubrovskiylog")
  k6 = types.InlineKeyboardButton(text="Товары в наличии",callback_data="5")
  k7 = types.InlineKeyboardButton(text="Пополнение Alipay, Wecht",callback_data="6")
  k.row(k1).row(k2).add(k3,k4,k6,k7).row(k5)
  bot.send_message(message.chat.id, text= "Приложение тут", reply_markup=k)
  


@bot.message_handler(commands=['admin'])
def admmmmin(message):
  
  kb_ad = types.InlineKeyboardMarkup(row_width=2)
  k1 = types.InlineKeyboardButton(text="КУРС",callback_data="curs")
  k2 = types.InlineKeyboardButton(text="ТРЕК",callback_data="trek")   
  kb_ad.add(k1,k2) 
  bot.send_message(message.chat.id, "Вы попали в меню администратора\nИсползуйте кнопки ниже",reply_markup=kb_ad)

@bot.callback_query_handler(func = lambda call: True)
def print_all_commands(call): 
  if call.data == "11":
    kb_change_curs = types.InlineKeyboardMarkup(row_width=1)
    k2 = types.InlineKeyboardButton(text="НАЗАД",callback_data="nazad") 
    kb_change_curs.add(k2)
    bot.send_message(call.message.chat.id,"Краткий ответ: Да, зависит от количества позиций и их стоимости, уточняйте у менеджера.",reply_markup=kb_change_curs)
  if call.data == "22":
    kb_change_curs = types.InlineKeyboardMarkup(row_width=1)
    k2 = types.InlineKeyboardButton(text="НАЗАД",callback_data="nazad") 
    kb_change_curs.add(k2)
    bot.send_message(call.message.chat.id,"Комиссия 5% + 500 рублей для позиций дешевле 400 юаней и 5% + 750 рублей для позиций дороже 400 юаней.",reply_markup=kb_change_curs)
  if call.data == "33":
    kb_change_curs = types.InlineKeyboardMarkup(row_width=1)
    k2 = types.InlineKeyboardButton(text="НАЗАД",callback_data="nazad") 
    kb_change_curs.add(k2)
    bot.send_message(call.message.chat.id,f"Доставка с POIZON до склада в Китае занимает 3-4 дня по бирюзовой кнопке💙 и 5-6 по черной кнопке🖤\n\nДоставка из Китая в Москву занимает 15-18 дней.🚛\n\nДоставка по России в эти диапазоны не входит и зависит от удаленности Вашего региона от г. Москва.",reply_markup=kb_change_curs)
  if call.data == "44":
    kb_change_curs = types.InlineKeyboardMarkup(row_width=1)
    k2 = types.InlineKeyboardButton(text="НАЗАД",callback_data="nazad") 
    kb_change_curs.add(k2)
    bot.send_message(call.message.chat.id,"Для оформления заказа необходимо написать менеджеру,чтобы Ваш заказ оформлялся быстро и без проблем, необходимо уделить немного своего времени и внимательно отправить информацию по шаблону написанному ниже:\n\n1) Артикул/ссылка на товар\n2) Размер по представленной сетке на данный товар.\n3) Цвет кнопки заказа\n4) Фото товара",reply_markup=kb_change_curs)
  if call.data == "55":
    kb_change_curs = types.InlineKeyboardMarkup(row_width=1)
    k2 = types.InlineKeyboardButton(text="НАЗАД",callback_data="nazad") 
    kb_change_curs.add(k2)
    bot.send_video(call.message.chat.id,video=open('video.mp4','rb'),caption=f"Артикул - это порядок букв или цифр по которому можно определить что это за модель , необходимо спуститься чуть ниже и открыть всплывающее окно. Нажмите на него и он скопируется, отправьте его нам. *Показано на видео.\n\nЦвет кнопки - это выбор доставки POZION\n\n Синяя - товар уже на складе POIZON, прошел легитчек и уже готов к отправлению\nЧерная - товар у продавца, он отправит его на склад POIZON для проверки на аутентичность и уже после отправится к нам на склад\nСерая(95) - товар Б/У или с дефектами. Нажав на кнопку вас перенесёт на сайт 95 где можно ознакомиться с дефектами. Чтобы заказать товар по серой кнопке, необходимо скачать приложение 95 и отправить ссылку на товар",reply_markup=kb_change_curs)
  if call.data == "66":
    kb_change_curs = types.InlineKeyboardMarkup(row_width=1)
    k2 = types.InlineKeyboardButton(text="НАЗАД",callback_data="nazad") 
    kb_change_curs.add(k2)
    bot.send_message(call.message.chat.id,"В сообщении о пришедшем товаре мы указываем форму для отправки СДЭК-ом и вы высылаете данные для отправки. Оплата производится при получении в ПВЗ СДЭК. Отслеживать свой заказ можно в личном кабинете СДЭК.\n\nСамовывоз в Москве производится по адресу: Днепропетровская 14, время и дни выдачи публикуются в беседе ВК - https://vk.me/join/8QslVR_0aJpEi45lpcKDGMC2WDfsVpP2r5c=",reply_markup=kb_change_curs)
  if call.data == "77":
    kb_change_curs = types.InlineKeyboardMarkup(row_width=1)
    k2 = types.InlineKeyboardButton(text="НАЗАД",callback_data="nazad") 
    kb_change_curs.add(k2)
    bot.send_message(call.message.chat.id,"Стоимость доставки Китай-Москва фиксированная и зависит от товара, вот примерный список позиций и цен:\n1) Кроссовки - 1250 за пару\n2) Футболка - 300\n3) Кофта/худи - 500\n4) Куртка - 900\n5) Часы и мелкие аксессуары - 300",reply_markup=kb_change_curs)
  if call.data == "88":
    kb_change_curs = types.InlineKeyboardMarkup(row_width=1)
    k2 = types.InlineKeyboardButton(text="НАЗАД",callback_data="nazad") 
    kb_change_curs.add(k2)
    bot.send_message(call.message.chat.id,"https://www.dewu.com - ссылка для android/ios\n\nСсылка на Poizon в App Store - https://apps.apple.com/ru/app/得物-得到运动x潮流x好物/id1012871328",reply_markup=kb_change_curs)
  if call.data == "nazad":
    k = types.InlineKeyboardMarkup(row_width=2)
    k1 = types.InlineKeyboardButton(text="РАCЧЕТ / ОТСЛЕЖИВАНИЕ", web_app=types.WebAppInfo(url="https://main--dancing-cheesecake-968061.netlify.app"))
    k2 = types.InlineKeyboardButton(text="КУРС",callback_data="1")
    k3 = types.InlineKeyboardButton(text="ВОПРОСЫ / ОТВЕТЫ",callback_data="2")
    k4 = types.InlineKeyboardButton(text="ОТЗЫВЫ",callback_data="3")
    k5 = types.InlineKeyboardButton(text="МЕНЕДЖЕР",url="https://t.me/botfather")
    k6 = types.InlineKeyboardButton(text="Товары в наличии",callback_data="5")
    k7 = types.InlineKeyboardButton(text="Пополнение Alipay, Wecht",callback_data="6")
    k.row(k1).row(k2).add(k3,k4,k6,k7).row(k5)
    bot.send_message(call.message.chat.id, text= "Приложение тут", reply_markup=k)
    variable.set_action(call.message.chat.id, 0)
  if call.data == "1":
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name    
    )
    connection.autocommit = True

    # #     connection.commit()
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT course FROM yuan"""
        )    
        qe = (cursor.fetchone()[0])
        
    kb_change_curs = types.InlineKeyboardMarkup(row_width=1)
    k2 = types.InlineKeyboardButton(text="НАЗАД",callback_data="nazad") 
    kb_change_curs.add(k2)
    bot.send_message(call.message.chat.id, f"Актуальный курс - {qe}",reply_markup=kb_change_curs)
    variable.set_action(call.message.chat.id, 0)
  if call.data == "2":
    k = types.InlineKeyboardMarkup(row_width=2)
    k1 = types.InlineKeyboardButton(text="🛍 Будет ли цена дешевле, если заказать несколько вещей? " ,callback_data="11")
    k2 = types.InlineKeyboardButton(text="💰Какая у вас комиссия?",callback_data="22")
    k3 = types.InlineKeyboardButton(text="🚚 Сколько времени занимает доставка товара?",callback_data="33")
    k4 = types.InlineKeyboardButton(text="🧩 Как заказать с POIZON?",callback_data="44")
    k5 = types.InlineKeyboardButton(text="🗣Где искать артикул и что значит «цвет кнопки»?", callback_data="55")
    k6 = types.InlineKeyboardButton(text="Есть ли доставка в другие города? Как забрать самовывозом в Москве?",callback_data="66")
    k7 = types.InlineKeyboardButton(text="Какая стоимость доставки?",callback_data="77")
    k8 = types.InlineKeyboardButton(text="Как скачать POIZON?",callback_data="88")
    kk = types.InlineKeyboardButton(text="НАЗАД",callback_data="nazad") 
    k.add(k1,k2,k3,k4,k5,k6,k7,k8,kk)
    bot.send_message(call.message.chat.id, text= "ВОПРОСЫ И ОТВЕТЫ", reply_markup=k)
    variable.set_action(call.message.chat.id, 0)
  if call.data == "3":
    kb_change_curs = types.InlineKeyboardMarkup(row_width=1)
    k2 = types.InlineKeyboardButton(text="НАЗАД",callback_data="nazad") 
    kb_change_curs.add(k2)
    bot.send_message(call.message.chat.id,"Отзывы о моей работе можно найти тут - https://vk.com/shipoizon?w=wall-216336053_3 *И на авито",reply_markup=kb_change_curs)

    
  if call.data == "5":
    kb_change_curs = types.InlineKeyboardMarkup(row_width=1)
    k2 = types.InlineKeyboardButton(text="НАЗАД",callback_data="nazad") 
    kb_change_curs.add(k2)
    bot.send_message(call.message.chat.id,"У нас есть очень много товаров в наличии, которые не нужно долго ждать, а можно сразу приехать и купить или заказать доставкой! Весь ассортимент находиться здесь - https://t.me/dubrovkiyshop",reply_markup=kb_change_curs)
  if call.data == "6":
    kb_change_curs = types.InlineKeyboardMarkup(row_width=1)
    k2 = types.InlineKeyboardButton(text="НАЗАД",callback_data="nazad") 
    kb_change_curs.add(k2)
    bot.send_message(call.message.chat.id,"Вы можете легко пополнить свой счет ALIPAY/WECHAT через меня! Для уточнения курса и обмена свяжитесь со мной - @dubrovskiylog",reply_markup=kb_change_curs)





  elif call.data == "curs":
    
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name    
    )
    connection.autocommit = True

    # #     connection.commit()
    with connection.cursor() as cursor:
        cursor.execute(
            """SELECT course FROM yuan"""
        )    
        qe = (cursor.fetchone()[0])
        
    kb_change_curs = types.InlineKeyboardMarkup(row_width=1)
    k1 = types.InlineKeyboardButton(text="СМЕНА",callback_data="cc")
    k2 = types.InlineKeyboardButton(text="НАЗАД",callback_data="back") 
    kb_change_curs.add(k1,k2)
    bot.send_message(call.message.chat.id, f"Актуальный курс - {qe}",reply_markup=kb_change_curs)
    
  if call.data == "trek":
    kb_change_trak = types.InlineKeyboardMarkup(row_width=1)
    k1 = types.InlineKeyboardButton(text="ДОБАВИТЬ",callback_data="at") 
    k2 = types.InlineKeyboardButton(text="ПОИСК",callback_data="ft") 
    k3 = types.InlineKeyboardButton(text="УДАЛИТЬ",callback_data="dt") 
    k4 = types.InlineKeyboardButton(text="НАЗАД",callback_data="back") 
    kb_change_trak.add(k1,k2,k3,k4)
    bot.send_message(call.message.chat.id, f"Меню Треккинга заказов",reply_markup=kb_change_trak)
  if call.data == "back":
    variable.set_action(call.message.chat.id, 0)
    kb_ad = types.InlineKeyboardMarkup(row_width=2)
    k1 = types.InlineKeyboardButton(text="КУРС",callback_data="curs")
    k2 = types.InlineKeyboardButton(text="ТРЕК",callback_data="trek")   
    kb_ad.add(k1,k2) 
    bot.send_message(call.message.chat.id, "Вы попали в меню администратора\nИсползуйте кнопки ниже",reply_markup=kb_ad)
  # Закончил выполнение меню панели, далее все идет на запросах к бд и используя varrible все работает кайф 
  if call.data == "dt":
    variable.set_action(call.message.chat.id, 5)
    kb_change_trak = types.InlineKeyboardMarkup(row_width=1)
    k3 = types.InlineKeyboardButton(text="НАЗАД",callback_data="back") 
    kb_change_trak.add(k3)
    bot.send_message(call.message.chat.id, "Введите трек номер заказа для удаления трек номера",reply_markup=kb_change_trak)

  if call.data == "cc":
    variable.set_action(call.message.chat.id, 1)
    kb_change_trak = types.InlineKeyboardMarkup(row_width=1)
    k3 = types.InlineKeyboardButton(text="НАЗАД",callback_data="back") 
    kb_change_trak.add(k3)
    bot.send_message(call.message.chat.id, "Введите новый курс",reply_markup=kb_change_trak)
  if call.data == "at":
    variable.set_action(call.message.chat.id, 2)
    kb_change_trak = types.InlineKeyboardMarkup(row_width=1)
    k3 = types.InlineKeyboardButton(text="НАЗАД",callback_data="back") 
    kb_change_trak.add(k3)
    bot.send_message(call.message.chat.id, "Введите новый трек номер и его статус через пробел\n\nПример (AE14713894 1)\n\n1. Выкуплен, в пути склад\n2. Принят на складе, оформляется\n3. Заказ в пути\n4. Сортируется в Москве be\n5. Передан в СДЭК\n6. Получен клиентом",reply_markup=kb_change_trak)
  if call.data == "ft":
    variable.set_action(call.message.chat.id, 3)
    kb_change_trak = types.InlineKeyboardMarkup(row_width=1)
    k3 = types.InlineKeyboardButton(text="НАЗАД",callback_data="back") 
    kb_change_trak.add(k3)
    bot.send_message(call.message.chat.id, "Введите трек номер заказа для смены статуса",reply_markup=kb_change_trak)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
  global treknom
  text = message.text
  action = int(variable.get_action(message.chat.id))


  if action == 1:
    curs = message.text
    connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name    
    )
    connection.autocommit = True
    try:
      with connection.cursor() as cursor:
          cursor.execute(
              f"""UPDATE yuan SET course = {message.text}"""
          )

      #     connection.commit()
      with connection.cursor() as cursor:
          cursor.execute(
              """SELECT course FROM yuan"""
          )    
          print(cursor.fetchone()[0])
          
          kb_change_trak = types.InlineKeyboardMarkup(row_width=1)
          k3 = types.InlineKeyboardButton(text="НАЗАД",callback_data="back") 
          kb_change_trak.add(k3)
          bot.send_message(message.chat.id, f"Актуальный курс - {message.text}",reply_markup=kb_change_trak)
          variable.set_action(message.chat.id, 0)
    except:
      variable.set_action(message.chat.id, 1)
      kb_change_trak = types.InlineKeyboardMarkup(row_width=1)
      k3 = types.InlineKeyboardButton(text="НАЗАД",callback_data="back") 
      kb_change_trak.add(k3)
      bot.send_message(message.chat.id, "Введите новый курс\nПример 13.5",reply_markup=kb_change_trak)
  
  
  if action == 2:
    try:
      trak = message.text.split(" ")[0]
      status = message.text.split(" ")[1]
      print(trak,status)
      connection = psycopg2.connect(
      host=host,
      user=user,
      password=password,
      database=db_name    
      )
      connection.autocommit = True
      try:
        with connection.cursor() as cursor:
            cursor.execute(
                f"""SELECT status FROM orders WHERE track = '{trak}'"""
            )
            a = cursor.fetchone()[0]
            variable.set_action(message.chat.id, 2)
            kb_change_trak = types.InlineKeyboardMarkup(row_width=1)
            k3 = types.InlineKeyboardButton(text="НАЗАД",callback_data="back") 
            kb_change_trak.add(k3)
            bot.send_message(message.chat.id, "УЖЕ СУЩЕСТВУЕТ\nВведите новый трек номер и его статус через пробел\n\nПример (AE14713894 1)\n\n1. Выкуплен, в пути склад\n2. Принят на складе, оформляется\n3. Заказ в пути\n4. Сортируется в Москве be\n5. Передан в СДЭК\n6. Получен клиентом",reply_markup=kb_change_trak)
      except:
        with connection.cursor() as cursor:
            cursor.execute(
              f"""INSERT INTO orders (track,status) VALUES ('{trak}',{status})"""
            )



        variable.set_action(message.chat.id, 0)
        kb_change_trak = types.InlineKeyboardMarkup(row_width=1)
        k3 = types.InlineKeyboardButton(text="НАЗАД",callback_data="back") 
        kb_change_trak.add(k3)
        bot.send_message(message.chat.id, "Успешно добавлен трек номер",reply_markup=kb_change_trak)


    except:
      variable.set_action(message.chat.id, 2)
      kb_change_trak = types.InlineKeyboardMarkup(row_width=1)
      k3 = types.InlineKeyboardButton(text="НАЗАД",callback_data="back") 
      kb_change_trak.add(k3)
      bot.send_message(message.chat.id, "Введите новый трек номер и его статус через пробел\n\nПример (AE14713894 1)\n\n1. Выкуплен, в пути склад\n2. Принят на складе, оформляется\n3. Заказ в пути\n4. Сортируется в Москве be\n5. Передан в СДЭК\n6. Получен клиентом",reply_markup=kb_change_trak)
 
  if action == 3:
    try:
      # поиск по номеру заказа 
      connection = psycopg2.connect(
      host=host,
      user=user,
      password=password,
      database=db_name    
      )
      connection.autocommit = True
      trak = message.text
      treknom = message.text
      with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT status FROM orders WHERE track = '{trak}';"""
        )
        
        a = cursor.fetchone()
        print(a)
        kb_change_trak = types.InlineKeyboardMarkup(row_width=1)
        k3 = types.InlineKeyboardButton(text="НАЗАД",callback_data="back") 
        kb_change_trak.add(k3)
        variable.set_action(message.chat.id, 4)
        bot.send_message(message.chat.id, f"трек номер {trak}\nСтатус - {a[0]}\nВведите новый статус заказа ",reply_markup=kb_change_trak)
    except:
      variable.set_action(message.chat.id, 3)
      kb_change_trak = types.InlineKeyboardMarkup(row_width=1)
      k3 = types.InlineKeyboardButton(text="НАЗАД",callback_data="back") 
      kb_change_trak.add(k3)
      bot.send_message(message.chat.id, "Введите трек номер заказа для смены статуса",reply_markup=kb_change_trak)
  if action == 4:
    stat = message.text
    connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name    
    )
    connection.autocommit = True
    
    with connection.cursor() as cursor:
        cursor.execute(
            f"""UPDATE orders SET status = {message.text} WHERE track = '{treknom}'"""
        )
    variable.set_action(message.chat.id, 0)
    kb_change_trak = types.InlineKeyboardMarkup(row_width=1)
    k3 = types.InlineKeyboardButton(text="НАЗАД",callback_data="back") 
    kb_change_trak.add(k3)
    bot.send_message(message.chat.id, "Успешно добавлен трек номер",reply_markup=kb_change_trak)
  if action == 5:
    trak = message.text
    treknom = message.text
    try:
      # поиск по номеру заказа 
      connection = psycopg2.connect(
      host=host,
      user=user,
      password=password,
      database=db_name    
      )
      connection.autocommit = True
      
      with connection.cursor() as cursor:
        cursor.execute(
            f"""SELECT status FROM orders WHERE track = '{trak}';"""
        )
        a = cursor.fetchone()[0]
        cursor.execute(
            f"""DELETE FROM orders WHERE track = '{trak}';"""
        ) 
        kb_change_trak = types.InlineKeyboardMarkup(row_width=1)
        k3 = types.InlineKeyboardButton(text="НАЗАД",callback_data="back") 
        kb_change_trak.add(k3)
        variable.set_action(message.chat.id, 0)
        bot.send_message(message.chat.id, f"УСПЕШНО УДАЛЕНО",reply_markup=kb_change_trak)
    except:
      variable.set_action(message.chat.id, 5)
      kb_change_trak = types.InlineKeyboardMarkup(row_width=1)
      k3 = types.InlineKeyboardButton(text="НАЗАД",callback_data="back") 
      kb_change_trak.add(k3)
      bot.send_message(message.chat.id, "Введите трек номер заказа для удаления трек номера",reply_markup=kb_change_trak)


while True:
  try:
    bot.polling(non_stop=True)
  except:
    bot.stop_polling()
    time.sleep(5)

