# REVIEWER: рекомендация (PEP 257) - отсутствует документирование модуля в
# целом.
# Коллега, каждый модуль желательно задокументирован в соответствие с PEP 257.
# Документация модуля, размещается в верхней части файла (начиная с 1-й строки).
import datetime as dt


class Record:
    # REVIEWER: рекомендация (PEP 257) - рекомендуется документировать класс.
    # REVIEWER: поскольку параметр date является не обязательным, его лучше
    # сразу инициализировать как None.
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        self.date = (
            dt.datetime.now().date() if
            not
            # REVIEWER: последнюю скобку лучше перенести на следующую строку.
            date else dt.datetime.strptime(date, '%d.%m.%Y').date())
        self.comment = comment


class Calculator:
    # REVIEWER: рекомендация (PEP 257) - рекомендуется документировать класс.
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        # REVIEWER: рекомендация (PEP 257) - рекомендуется документировать
        # метод.
        self.records.append(record)

    def get_today_stats(self):
        # REVIEWER: рекомендация (PEP 257) - рекомендуется документировать
        # метод.
        today_stats = 0
        # REVIEWER: рекомендуется переименовать переменную Record, поскольку
        # существует класс Record, что может ввести в замешательство. Кроме
        # того, согласно (PEP8) - названия переменных должны начинаться
        # с символа в нижнем регистре.
        for Record in self.records:
            if Record.date == dt.datetime.now().date():
                # REVIEWER: можно упростить 'today_stats += Record.amount'
                today_stats = today_stats + Record.amount
        return today_stats

    def get_week_stats(self):
        # REVIEWER: рекомендация (PEP 257) - рекомендуется документировать
        # метод.
        week_stats = 0
        today = dt.datetime.now().date()
        for record in self.records:
            # REVIEWER: можно упростить: 7 > (today - record.date).days >= 0
            if (
                (today - record.date).days < 7 and
                (today - record.date).days >= 0
            ):
                week_stats += record.amount
        return week_stats


class CaloriesCalculator(Calculator):
    # REVIEWER: рекомендация (PEP 257) - рекомендуется документировать класс.
    # REVIEWER: Я бы не рекомендовал использовать лишние комментарии в коде,
    # код должен быть самодокументирующимся.
    def get_calories_remained(self):  # Получает остаток калорий на сегодня
        # REVIEWER: лучше переименовать переменную 'x', название переменным
        # должны быть осознанные, например 'remainder'
        x = self.limit - self.get_today_stats()
        if x > 0:
            # REVIEWER: лучше не использовать '\', с целью переноса строки
            # REVIEWER: можно так:
            # return (
            #     f'Сегодня можно съесть что-нибудь'
            #     f' ещё, но с общей калорийностью не более {x} кКал'
            # )
            return f'Сегодня можно съесть что-нибудь' \
                   f' ещё, но с общей калорийностью не более {x} кКал'
        # REVIEWER: Лучше упростить и не использовать else, а сразу
        # возвращать результат
        else:
            return('Хватит есть!')


class CashCalculator(Calculator):
    # REVIEWER: рекомендация (PEP 257) - рекомендуется документировать класс.
    USD_RATE = float(60)  # Курс доллар США.
    EURO_RATE = float(70)  # Курс Евро.
    # REVIEWER: в условиях задачи метод get_today_cash_remained должен
    # принимать только один аргумент currency, соответственно USD_RATE и
    # EURO_RATE в аргументах не должно быть
    def get_today_cash_remained(self, currency,
                                USD_RATE=USD_RATE, EURO_RATE=EURO_RATE):
        # REVIEWER: рекомендация (PEP 257) - рекомендуется документировать
        # метод.
        # REVIEWER: лучше данные в currency приводить к нижнему регистру
        # currency.lower()
        currency_type = currency
        cash_remained = self.limit - self.get_today_stats()
        if currency == 'usd':
            cash_remained /= USD_RATE
            currency_type = 'USD'
        elif currency_type == 'eur':
            cash_remained /= EURO_RATE
            currency_type = 'Euro'
        elif currency_type == 'rub':
            # REVIEWER: допущена ошибка. Значение 'cash_remained == 1.00' не 
            # имеет никакого логического эффекта 
            cash_remained == 1.00
            currency_type = 'руб'
        if cash_remained > 0:
            return (
                f'На сегодня осталось {round(cash_remained, 2)} '
                f'{currency_type}'
            )
        elif cash_remained == 0:
            return 'Денег нет, держись'
        # REVIEWER: Лучше упростить и не использовать elif, а сразу
        # возвращать результат. Также лучше не использовать '\', 
        # с целью переноса строки и использовать через f-строку.
        elif cash_remained < 0:
            return 'Денег нет, держись:' \
                   ' твой долг - {0:.2f} {1}'.format(-cash_remained,
                                                     currency_type)
    
    # REVIEWER: Поскольку метод get_week_stats не переопределяется в
    # дочернем классе, нет необходимости в его обозначении.
    def get_week_stats(self):
        super().get_week_stats()
# REVIEWER: отсутствует в конце кода пустая строка.
