# ✔ Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

# ОГРАНИЧЕНИЕ НА СУММУ КРАНО 50
def check_amount(amount):
    if amount % 50 == 0:
        return True
    else:
        print("Сумма должна быть кратной 50!")
        return False


# НАЧИСЛЕНИЕ 3% ПРОЦЕНТОВ // рассчитать проценты (баланс, число операций)
def calculate_interest(balance, operations_count):
    if operations_count >= 3:                                                   # если число_операций >= 3:
        balance *= 0.97                                                     # Начисляем проценты в размере 3%
        balance = round(balance, 2)                          # баланс = округляем до 2-х символов(баланс, 2)
        print("Начислены проценты 3%.")
        print("Общий счет после начисления процентов:", balance, "y.e.")
    return balance


# НАЛОГ НА БОГАТСТВО // вычесть богатство_налог (баланс):
def deduct_wealth_tax(balance):
    if balance > 5000000:                                                       # если баланс > 5000000:
        wealth_tax = balance * 0.1             # богатство_налог = баланс * 0.1/ Вычитаем налог на богатство 10%
        wealth_tax = round(wealth_tax, 2)                         # налог_на_богатство=округляем(налог_на_богатство, 2)
        balance -= wealth_tax                                                   # баланс -= налог_на богатство
        print("Вычтен налог на богатство:", wealth_tax, "y.e.")
        print("Общий счет после вычета налога на богатство:",
              round(balance, 2), "y.e.")
    return balance


# ПРОЦЕНТ ЗА СНЯТИЕ // рассчитать комиссию за вывод (сумма):
def calculate_withdrawal_fee(amount):
    withdrawal_fee = amount * 0.015                              # вывод_комиссия = сумма * 0,015 # 1,5% от суммы снятия
    withdrawal_fee = max(withdrawal_fee, 30)                                # комиссия за вывод не менее 30 у.е.
    withdrawal_fee = min(withdrawal_fee, 600)                               # комиссия за вывод не более 600 у.е.
    return withdrawal_fee


def deposit(balance, operations_count):                                  # ДЕПОЗИТ(баланс, количество_операций):
    amount = int(input("\nВведите сумму для пополнения (кратную 50): "))
    if check_amount(amount):                                                    # сумма чека (сумма):
        balance += amount                                                       # остаток += сумма
        # Проверяем и вычитаем налог на богатство
        balance = round(deduct_wealth_tax(balance), 2)              # баланс = округл (вычет_налог_богатства (баланс), 2

        print("Счет пополнен на", amount, "у.е.")
        print("Общий счет:", balance, "y.e.")
        operations_count += 1                                                   # число_операций += 1
        balance = calculate_interest(balance, operations_count)  # баланс = рассчитать проценты 3% (баланс, кол_опе)

    return balance, operations_count                                            # возврат баланса, число_операций


def withdraw(balance, operations_count):                            # ВЫВЕСТИ(баланс, количество_операций):
    amount = int(input("\nВведите сумму для снятия (кратную 50): "))
    if check_amount(amount):
        if amount <= balance:                                                   # если сумма <= баланс:
            balance = deduct_wealth_tax(balance)                        # баланс = вычесть налог на богатство (баланс)

            withdrawal_fee = round(calculate_withdrawal_fee(amount), 2)
            balance -= withdrawal_fee                                           # баланс -= комиссия за вывод

            balance -= amount                                                   # остаток -= сумма
            print("Вы сняли", amount, "у.е.")
            print("Процент за снятие:", withdrawal_fee, "у.е.")
            print("Общий счет:", round(balance, 2), "y.e.")
            operations_count += 1
            balance = calculate_interest(balance, operations_count)            # баланс = рас-ть проц 3% (бал, кол_опер)
        else:
            print("Недостаточно средств на счете!")
    return balance, operations_count


def atm():                                                                      # банкомат()
    balance = 0
    operations_count = 0

    while True:
        print("\n1. Пополнить счет")
        print("2. Снять деньги")
        print("3. Выйти")

        choice = input("Выберите действие (1-3): ")

        match choice:
            case "1":
                balance, operations_count = deposit(balance, operations_count)  # бал, кол_опер = депозит(бал, кол_оп)
            case "2":
                balance, operations_count = withdraw(balance, operations_count)  # бал. кол_опер= снятие(бал, кол_опер)
            case "3":
                print("До свидания!")
                break
            case _:
                print("Некорректный выбор. Попробуйте еще раз.")


atm()
