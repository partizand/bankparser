# Generate automatically by build.py
# don`t change manually

class ConfCommons:

   delimiter = ';' # Разделитель полей
   encoding = 'utf-8' # Кодировка файла
   startafter = None # Начинать разбор строк со следующей, после стоки начинающейся с указанных символов
   type = 'Bank' # Тип выписки: Bank или Invst (обычная или операции с ценными бумагами)
   fields = [] # Обязательное поле. Имена полей в файле через пробел, нужные поля должны совпадать с именем в описанни доступных полей
   dateformat = '%Y-%m-%d %H:%M:%S' # Формат даты в банковском файле
   banksite = None # Ссылка на сайт банка
   bankname = None # Название банка
