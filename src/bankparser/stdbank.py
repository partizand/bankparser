class StdBank:
    """
    Стандартные настройки для банка
    """
    # start_fields description
    parser = 'ParserCSV'  # Имя класса парсера для разбора файла. ParserCSV or ParserXML
    delimiter = ";"  # Разделитель полей для CSV
    startafter = None  # Для CSV. Начинать разбор строк со следующей, после стоки начинающейся с указанных символов
    dateformat = "%Y-%m-%d %H:%M:%S"  # Формат даты в банковском файле
    encoding = "utf-8"  # Кодировка файла
    fields = []  # Имена полей в файле, нужные поля должны совпадать с именем в описанни доступных полей
    type = "Bank"  # Тип выписки: Bank или Invst (обычная или операции с ценными бумагами)
    banksite = None  # Ссылка на сайт банка
    banktitle = ''  # Название банка
    statementfile = ''  # Стандартное имя файла выписки
    description = ''  # Описание
    xpath_tolines = ''  # для формата xml путь к элементам перечисления. Например ./details/detail
    m_vars = {}  # Пременные нужные для конкретного банка. Переопределяются в ini
    m_descr_account = {} # Сопоставление назначений платежа. Переопределяются в ini
    bankname = 'stdbank'  # код банка. Имя файла банка без расширения. Задается автоматически
    # end_fields

    def after_row_parsed(self, statementline, rawline):
        """
        Event calls after row was parsed.
        You may override this function to do something.
        statementline is parsed object of StatementLine.
        rawline is raw data. Map field name to string value. Contains all fields.
        If you want cancel line, return None
        :param statementline: parsed object of StatementLine
        :param rawline: raw data line. Map = {'field name': 'string value', ..}
        :return: StatementLine object or None
        """
        return statementline

    def __repr__(self):
        return '<bank name={0}>'.format(self.bankname)
