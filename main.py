# REVIEWER: нарушение (PEP8) - отсутствует документирование модуля в целом.
# Коллега, каждый модуль должен быть задокументирован в соответствие с PEP 257.
# Документация модуля, размещается в верхней части файла (начиная с 1-й строки).
import datetime as dt
# REVIEWER: неиспользуемый импорт.
import json
# REVIEWER: нарушение (PEP8) - перед классом должно быть два отступа.
class Record:
    # REVIEWER: нарушение (PEP8) - отсутствует документирование класса.
    # REVIEWER: параметр date - лучше сразу инициализировать как None.
    def __init__(self, amount, comment, date=''):
        # REVIEWER: нарушение (PEP8) - отсутствуют пробелы до и после оператора `=`.
        self.amount=amount
        # REVIEWER: нарушение (PEP8) - длина строки не должна превышает 79 символов.
        # REVIEWER: инициализацию даты лучше вынести в отдельный метод. 
        self.date = dt.datetime.now().date() if not date else dt.datetime.strptime(date, '%d.%m.%Y').date()
        # REVIEWER: нарушение (PEP8) - отсутствуют пробелы до и после оператора `=`.
        self.comment=comment
# REVIEWER: нарушение (PEP8) - перед классом должно быть два отступа.
class Calculator:
    # REVIEWER: нарушение (PEP8) - отсутствует документирование класса.
    def __init__(self, limit):
        self.limit = limit
        # REVIEWER: нарушение (PEP8) - отсутствуют пробелы до и после оператора `=`.
        self.records=[]
    # REVIEWER: отсутствует отступ между блоками.
    def add_record(self, record):
        # REVIEWER: нарушение (PEP8) - отсутствует документирование метода.
        self.records.append(record)
    # REVIEWER: отсутствует отступ между блоками.
    def get_today_stats(self):
        # REVIEWER: нарушение (PEP8) - отсутствует документирование метода.
        # REVIEWER: нарушение (PEP8) - отсутствуют пробелы до и после оператора `=`.
        today_stats=0
        # REVIEWER: нарушение (PEP8) - название переменной должно быть с маленькой буквы.
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                # REVIEWER: today_stats += rcord.amount
                today_stats = today_stats+Record.amount
        return today_stats
    # REVIEWER: отсутствует отступ между блоками.
    def get_week_stats(self):
        # REVIEWER: нарушение (PEP8) - отсутствует документирование метода.
        # REVIEWER: нарушение (PEP8) - отсутствуют пробелы до и после оператора `=`.
        week_stats=0
        today = dt.datetime.now().date()
        for record in self.records:
            # REVIEWER: нарушение (PEP8) - отсутствуют пробелы между оператором `<` и 7.
            # REVIEWER: нарушение (PEP8) - отсутствуют пробелы между оператором `>=` и 0.
            # REVIEWER: нарушение (PEP8) - длина строки не должна превышает 79 символов.
            # REVIEWER: можно упростить: 7 > (today - record.date).days >= 0
            if (today -  record.date).days <7 and (today -  record.date).days >=0:
                # REVIEWER: нарушение (PEP8) - отсутствуют пробелы между оператором `+=` и record.amount.
                week_stats +=record.amount
        return week_stats
# REVIEWER: нарушение (PEP8) - перед классом должно быть два отступа.
class CaloriesCalculator(Calculator):
    # REVIEWER: нарушение (PEP8) - отсутствует документирование класса.
    # REVIEWER: комментарии не должны использоваться.
    def get_calories_remained(self): # Получает остаток калорий на сегодня
        # REVIEWER: нарушение (PEP8) - отсутствует документирование метода.
        # REVIEWER: нарушение (PEP8) - отсутствуют пробелы до и после оператора `=`.
        # REVIEWER: нарушение (PEP8) - отсутствуют пробелы до и после оператора `-`.
        # REVIEWER: нарушение (PEP8) - имя переменной `х` должно быть осмысленное.
        x=self.limit-self.get_today_stats()
        if x > 0:
            # REVIEWER: нарушение (PEP8) - длина строки не должна превышает 79 символов.
            # REVIEWER: можно так:
            # return('Сегодня можно съесть что-нибудь ещё, но с общей'
            #       f'калорийностью не более {x} кКал')
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {x} кКал'
        # REVIEWER: else лишний
        else:
            return 'Хватит есть!'
# REVIEWER: нарушение (PEP8) - перед классом должно быть два отступа.
class CashCalculator(Calculator):
    # REVIEWER: нарушение (PEP8) - отсутствует документирование класса.
    # REVIEWER: нарушение (PEP8) - отсутствуют пробелы до и после оператора `=`.
    # REVIEWER: нет необходимости явного преобразования во float, Python сам преобразует.
    # REVIEWER: константные переменые лучше вынести вверх модуля после импортов.
    USD_RATE=float(60) #Курс доллар США.
    EURO_RATE=float(70) #Курс Евро.
    # REVIEWER: отсутствует отступ между блоками.
    # REVIEWER: нарушение (PEP8) - длина строки не должна превышает 79 символов.
    # REVIEWER: согласно условий задачи, метод get_today_cash_remained должен принимать только один
    # аргумент currency, соответственно USD_RATE и EURO_RATE использовать через
    # self.USD_RATE и self.EURO_RATE соответственно
    def get_today_cash_remained(self, currency, USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        # REVIEWER: нарушение (PEP8) - отсутствует документирование метода.
        # REVIEWER: нарушение (PEP8) - отсутствуют пробелы до и после оператора `=`.
        currency_type=currency
        cash_remained = self.limit - self.get_today_stats()
        # REVIEWER: нарушение (PEP8) - отсутствуют пробелы  пробелы между currency и оператором `==`.
        if currency=='usd':
            cash_remained /= USD_RATE
            currency_type ='USD'
        # REVIEWER: нарушение (PEP8) - отсутствуют пробелы  пробелы между currency_type и оператором `==`.
        elif currency_type=='eur':
            cash_remained /= EURO_RATE
            currency_type ='Euro'
        # REVIEWER: нарушение (PEP8) - отсутствуют пробелы  пробелы между currency_type и оператором `==`.
        elif currency_type=='rub':
            # REVIEWER: ошибочная строка.
            cash_remained == 1.00
            currency_type ='руб'
        if cash_remained > 0:
        # REVIEWER: в f-строках нет логических или арифметических операций
        # REVIEWER: нарушение (PEP8) - длина строки не должна превышает 79 символов.
            return f'На сегодня осталось {round(cash_remained, 2)} {currency_type}'
        elif cash_remained == 0:
            return 'Денег нет, держись'
        # REVIEWER: лучше использовать else вместо elif
        elif cash_remained < 0:
        # REVIEWER: должно быть единообразие в коде. Нужно использовать через f-строку.
        # REVIEWER: нарушение (PEP8) - длина строки не должна превышает 79 символов
            return 'Денег нет, держись: твой долг - {0:.2f} {1}'.format(-cash_remained, currency_type)
    # REVIEWER: метод лишний 
    def get_week_stats(self):
        super().get_week_stats()

# REVIEWER: отсутствует конструкция точка входа if __name__ == ‘__main__’
# if __name__ == ‘__main__’
# REVIEWER: отсутствует после кода пустая строка.
