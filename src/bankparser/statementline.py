from datetime import datetime

class StatementLine:

# start_fields qif_letter;description
   amount = 0.0  # T;Сумма
   amountsign = ""  # ;Слово указание на списание или зачисление, для определения знака суммы
   account = ""  # ;Счет
   date = datetime.now()  # D;Дата проводки
   description = ""  # M;Описание
   action = ""  # N;Операция (для ценных бумаг): buy, sell. Для приведения к стандартным операциям используйте секцию [action]. Например [action] Покупка=buy
   securityname = ""  # Y;Имя ценной бумаги
   price = 0.0  # I;Цена (для ценных бумаг)
   quantity = 0.0  # Q;Количество бумаг
   commission = 0.0  # O;Комиссия (для ценных бумаг)
   payee = ""  # P;Получатель платежа
   numbercheck = ""  # N;Номер чека (Номер транзакции ?)
   category = ""  # L;Название счета для списания/зачисления (второй счет проводки). Например, Расходы:Питание
# end_fields