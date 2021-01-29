 # -*- coding: utf-8 -*-

import telebot 
from telebot import types
import random
token ="1282827672:AAEGigl4htKIeXbxPI-Hpwe1MODDI9KLcuk"
bot= telebot.TeleBot (token)



#upd =bot.get_updates ()
#print (upd)
#last_upd = upd [-1]
#massage_user = last_upd.message
#print (massage_user)

@bot.message_handler (commands =['pass'])
def handle_menu (message):
   user_markup = telebot.types.ReplyKeyboardMarkup (True, False)
   user_markup.row ('/Мені_погано')
   user_markup.row ('/Авто')
   user_markup.row ('/Як_справи? ✔')
   user_markup.row ('/Прибирання', '/Робота')
   user_markup.row ('/Маленька_витрата?', '/Зарядка')
   user_markup.row ('/Плато', '/Розвиток')
   user_markup.row ('/Стосунки', '/Політика')
   user_markup.row ('/Кредит')
   user_markup.row ('/Вихід')
   user_markup.row ('/Ризик')
   user_markup.row ('/Соц_мережі')
   user_markup.row ('/Сумно')
   user_markup.row ('/Бий_або_біжи')
   user_markup.row ('/Маніпуляції')
   user_markup.row ('/Що_роблю?')
   bot.send_message (message.from_user.id, 'Hi+10+10', reply_markup=user_markup)



#START Для меню


@bot.message_handler (commands =['Мені_погано'])
def handle_whatch (message):
 #  user_markup = telebot.types.ReplyKeyboardMarkup (True)
  
   markup = types.ReplyKeyboardMarkup(True)

   item1 = types.KeyboardButton("/Переключитись")
   item2 = types.KeyboardButton("/pass")

   markup.add(item1, item2)
   bot.send_message (message.from_user.id, '1) уникнення необхідного \n  стрес vs невідомість  \n Корисне vs необхідне  \n 2) Виписати всі небхідні справи  \n 3) Переключитись ', reply_markup=markup)

@bot.message_handler (commands =['Авто'])
def handle_whatch (message):
   user_markup = telebot.types.ReplyKeyboardMarkup (True)
   bot.send_message (message.from_user.id, 'Допомога важлива і собі це пріорітет! \n Для чого? Сила часу і переміщення, мене і ваги. \n Кожного дня я не в рівних з собою в рази зі цією силою ', reply_markup=user_markup)



@bot.message_handler (commands =['Що_роблю?'])
def handle_whatch (message):
   user_markup = telebot.types.ReplyKeyboardMarkup (True)
   bot.send_message (message.from_user.id, 'erfsefeeЯ реалізовую толкові речі -права, пк, авто, дім, сімя і заробляю на хжу одяг і соціальні щоб не стресувати - я ж людина ', reply_markup=user_markup)

@bot.message_handler (commands =['Маніпуляції'])
def handle_manip (message):
   user_markup = telebot.types.ReplyKeyboardMarkup (True)
   bot.send_message (message.from_user.id, 'Довіра - ні при чому потрібно її заслужити. Продавець - продає що вигідно - % або не продається. \n Краса - мухомор теж красивий але він смертельний  \n  Стосунки: \n Спаси мене від себе \n обесцінювання \n скривання \n До чого ти мене примусив', reply_markup=user_markup)

@bot.message_handler (commands =['Бий_або_біжи'])
def handle_teranozavr (message):
   user_markup = telebot.types.ReplyKeyboardMarkup (True)
   bot.send_message (message.from_user.id, 'Вона крисива - робиш вищим за себе а стосунки це коли рівні а ну нормально \n Може бути - капарниця, перекручувати, Я мала інше на увазі, Залежним - ти мене вислухав і я хороша - ти молодець що робиш по моєму а визиваюча поведінка щоб загнати в пастку \n Характер 1 місце - людина перевіряється тестами - ОЙ пака', reply_markup=user_markup)


@bot.message_handler (commands =['Сумно'])
def handle_sum (message):
   user_markup = telebot.types.ReplyKeyboardMarkup (True)
   bot.send_message (message.from_user.id, 'Коли переміни теж треба вміти жити коли стає краще 😊😊😊😊', reply_markup=user_markup)



@bot.message_handler (commands =['Ризик'])
def handle_risk (message):
   markup = types.ReplyKeyboardMarkup(True)
   item1 = types.KeyboardButton("randoms")
   item2 = types.KeyboardButton("😊 Як справи?")
   item3 = types.KeyboardButton("50")
   item4 = types.KeyboardButton("/pass")

   markup.add(item1, item2, item3, item4)

   bot.send_message(message.chat.id, "Неповна - сложність (комуналка) \n батьки стріють скоро тільки їм помагати. ",
        parse_mode='html', reply_markup=markup)

@bot.message_handler (commands =['Вихід'])
def handle_tuda (message):
   user_markup = telebot.types.ReplyKeyboardMarkup (True)
   bot.send_message (message.from_user.id, 'Найкраще самому - Команда - багато людей для багато людей. Толкові знайомі - Коля. Бізнес - від 1000$ крім базових.', reply_markup=user_markup)

@bot.message_handler (commands =['Стосунки'])
def handle_simya (message):
   user_markup = telebot.types.ReplyKeyboardMarkup (True)

   markup = types.ReplyKeyboardMarkup(True)
 
   item1 = types.KeyboardButton("/Оцінка_Розмови")
   item2 = types.KeyboardButton("/pass")
   markup.add(item1, item2)
   bot.send_message (message.from_user.id, 'Все просто -якщо я себе почуваю добре то ок якщо якесь непонятно то пака \n Маніпуляції - чоловіки мають... \n Давлять на емоції перекручують - води не жаліють - йли в магаз скажи так \n Бачити коли спокійно маленькі знаки великого. Навязливість - щось дуже не так. \n Я подумаю - Запасний варіант і неповага. \n Фото самої - гачок. \n Початок з поноціних особистостей - допомога людина приймає бо виживає а потім включаються справжні цілі - тобто ти незнає з ким маєш справу)', reply_markup=markup)






@bot.message_handler (commands =['Політика'])
def handle_pol (message):
   user_markup = telebot.types.ReplyKeyboardMarkup (True)
   bot.send_message (message.from_user.id, 'Йдуть - Бо в контексті (Україна - конституція. армія. обовязки) і захищають себе від впливу  і стоять у потоку впливу і захищають свої інтереси законно а ти виконуй закон', reply_markup=user_markup)



@bot.message_handler (commands =['Кредит'])
def handle_money (message):
   user_markup = telebot.types.ReplyKeyboardMarkup (True)
   bot.send_message (message.from_user.id, 'За телефон 6000 переплата 1000 + 800 грн за і рік при продажі. І я втрачаю 1800 а людина без кредиту 800', reply_markup=user_markup)


@bot.message_handler (commands =['Розвиток'])
def handle_progres (message):
   user_markup = telebot.types.ReplyKeyboardMarkup (True)
   bot.send_message (message.from_user.id, 'Люди - не логіка а спонтанність, Переконання - Вобхід, Сила - враховувати лінь ', reply_markup=user_markup)

@bot.message_handler (commands =['Плато'])
def handle_plato (message):
   user_markup = telebot.types.ReplyKeyboardMarkup (True)
   bot.send_message (message.from_user.id, 'Робити на джинси,ремінь,шорти і на толкові речі не хватає - стрес 1 або 2', reply_markup=user_markup)








@bot.message_handler (commands =['Маленька_витрата?'])
def handle_vitrata (message):

   

   markup = types.ReplyKeyboardMarkup(True)

   item1 = types.KeyboardButton("50")
   item2 = types.KeyboardButton("/pass")

   markup.add(item1, item2)

   bot.send_message (message.from_user.id, '50 грн? (минуле 1500) - (Я не людина? 50+300 грн) (сума 3000) - (толкові 1750) - майбутнє', reply_markup=markup)
   #next step
  
   bot.send_message (message.from_user.id, "відправте", reply_markup=markup)
   bot.send_message (message.from_user.id, "c", reply_markup=markup)
   bot.send_message (message.from_user.id, "відправте", reply_markup=markup)




      
  


@bot.message_handler (commands =['Прибирання'])
def handle_chisto (message):
   user_markup = telebot.types.ReplyKeyboardMarkup (True)
   bot.send_message (message.from_user.id, 'В box або закрито, забрав бокс і протер', reply_markup=user_markup)
   

@bot.message_handler (commands =['Робота'])
def handle_work (message):
   user_markup = telebot.types.ReplyKeyboardMarkup (True)
   bot.send_message (message.from_user.id, 'Зробити Прайс IT', reply_markup=user_markup)


@bot.message_handler (commands =['Зарядка'])
def handle_zara (message):
   user_markup = telebot.types.ReplyKeyboardMarkup (True)
   bot.send_message (message.from_user.id, 'Великі довгі моменти, фокус окрім роботи', reply_markup=user_markup)


@bot.message_handler (commands =['/Жарко'])
def handle_sums (message):
   user_markup = telebot.types.ReplyKeyboardMarkup (True)
   bot.send_message (message.from_user.id, ' tstndsd', reply_markup=user_markup)



   

#END Для меню

# обробка кнопок
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'randoms':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == '😊 Як справи?':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
      
 
            markup.add(item1)
 
            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)

   
        if message.text == '50':
           bot.send_message(message.chat.id, "минуле \n сума {str_a} \n майбутнє")
          
        if message.text == "10000":
            str_a = message.text
            b = 10
            c = int(str_a) + b
            print ("The value of c = ",c)
            bot.send_message (message.from_user.id, c)

        if message.text == '/Як_справи? ✔':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Дуже добре 🙃", callback_data='good')
            item2 = types.InlineKeyboardButton("Сумно 😔", callback_data='sadly')
            item3 = types.InlineKeyboardButton("Стосунки 🧐", callback_data='relations')
            item4 = types.InlineKeyboardButton("Погано 😥", callback_data='bad')
 
            markup.add(item1, item2, item3,item4)
 
            bot.send_message(message.chat.id, 'Будемо вирулювати 😊😊😊', reply_markup=markup)



 # прослушка кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
         # Levl_2 
        if call.message:
            if call.data == 'good':
               bot.send_message(call.message.chat.id, 'От і здорово 😊')
            
               markup = types.InlineKeyboardMarkup(row_width=2)
               item1 = types.InlineKeyboardButton("Мертва зона", callback_data='goods')
               
 
               markup.add(item1)
               bot.send_message(call.message.chat.id, 'Рухаємлсь дальше', reply_markup=markup)

              
            elif call.data == 'bad':

                 bot.send_message(call.message.chat.id, 'Впораємось 😊')
            
                 markup = types.InlineKeyboardMarkup(row_width=2)
                 item1 = types.InlineKeyboardButton("Температура", callback_data='bad1')
                 item2 = types.InlineKeyboardButton("Освітлення", callback_data='bad2')
                 item3 = types.InlineKeyboardButton("в'ялість", callback_data='bad3')
                 
 
                 markup.add(item1, item2,item3)
                 bot.send_message(call.message.chat.id, 'Рухаємлсь дальше', reply_markup=markup)



@bot.message_handler (commands =['Оцінка_Розмови'])
def handle_pol (message):
   user_markup = telebot.types.ReplyKeyboardMarkup (True)
   bot.send_message (message.from_user.id, 'сіві', reply_markup=user_markup)
                 

         # Levl_3  
        if call.message:
            if call.data == 'goods':
               bot.send_message(call.message.chat.id, 'Славно 😊')
               bot.send_message(call.message.chat.id, 'Все в цьому світі задяки і за допомогою людей')           



            if call.data == 'bad1':
               bot.send_message(call.message.chat.id, 'Впораємось 😊')

                           
               markup = types.InlineKeyboardMarkup(row_width=2)
               item1 = types.InlineKeyboardButton("Жарко", callback_data='C_plus')
               item2 = types.InlineKeyboardButton("Холодно", callback_data='C_minus')
 
               markup.add(item1, item2)

               bot.send_message(call.message.chat.id, 'adsdasa', reply_markup=markup)           



         # Levl_4
        if call.message:
            if call.data == 'C_plus':
               bot.send_message(call.message.chat.id, 'Значить тобі 🥵')

                           
               markup = types.InlineKeyboardMarkup(row_width=2)
               item1 = types.InlineKeyboardButton("День", callback_data='C_p_day')
               item2 = types.InlineKeyboardButton("Вечір_ніч", callback_data='C_p_night')
 
               markup.add(item1, item2)

               bot.send_message(call.message.chat.id, 'Все в цьому світі задяки і за допомогою людей', reply_markup=markup)           

            if call.data == 'C_minus':
               bot.send_message(call.message.chat.id, 'Значить тобі 🥶')

                           
               markup = types.InlineKeyboardMarkup(row_width=2)
               item1 = types.InlineKeyboardButton("День", callback_data='C_m_day')
               item2 = types.InlineKeyboardButton("Вечір_ніч", callback_data='C_m_night')
 
               markup.add(item1, item2)

               bot.send_message(call.message.chat.id, "dfdf", reply_markup=markup)           


         # Levl_5
        if call.message:
            if call.data == 'C_p_day':
               bot.send_message(call.message.chat.id, 'Олдягни шорти і скинь кофту \n попий води')

                           
               






 # remove inline buttons
         # bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="вийло", 
          
          #reply_markup=None)





            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False, text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")
 
    except Exception as e:
        print(repr(e))

def new_func1(call, markup):
    new_var = new_func(call, markup)
    new_var

def new_func(call, markup):
    bot.send_message(call.message.chat.id, 'Ye lfdfjq', reply_markup=markup)









bot.polling (none_stop=True, interval=0)


