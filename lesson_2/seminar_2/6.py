# Задание №6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю +
# ✔ Допустимые действия: пополнить, снять, выйти +
# ✔ Сумма пополнения и снятия кратны 50 у.е. +
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.+
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3% +
# ✔ Нельзя снять больше, чем на счёте +
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной +
# ✔ Любое действие выводит сумму денег +

def check_amount(amount):                                                       # ОГРАНИЧЕНИЕ НА СУММУ КРАНО 50
    if amount % 50 == 0:
        return True
    else:
        print("Сумма должна быть кратной 50!")
        return False

def calculate_interest(balance, operations_count):                              # НАЧИСЛЕНИЕ 3% ПРОЦЕНТОВ // рассчитать проценты (баланс, число операций)
    if operations_count >= 3:                                                   # если число_операций >= 3:
        balance *= 0.97                                                     # Начисляем проценты в размере 3%
        balance = round(balance, 2)                                             # баланс = округляем до 2-х символов(баланс, 2)
        print("Начислены проценты 3%.")
        print("Общий счет после начисления процентов:", balance, "y.e.")
    return balance

def deduct_wealth_tax(balance):                                                 # НАЛОГ НА БОГАТСТВО // вычесть богатство_налог (баланс):
    if balance > 5000000:                                                       # если баланс > 5000000:
        wealth_tax = balance * 0.1                                          # богатство_налог = баланс * 0.1/ Вычитаем налог на богатство 10%
        wealth_tax = round(wealth_tax, 2)                                       # налог_на_богатство=округляем(налог_на_богатство, 2)
        balance -= wealth_tax                                                   # баланс -= налог_на богатство
        print("Вычтен налог на богатство:", wealth_tax, "y.e.")
        print("Общий счет после вычета налога на богатство:",
              round(balance, 2), "y.e.")
    return balance

def calculate_withdrawal_fee(amount):                                           # ПРОЦЕНТ ЗА СНЯТИЕ // рассчитать комиссию за вывод (сумма):
    withdrawal_fee = amount * 0.015                                         # вывод_комиссия = сумма * 0,015 # 1,5% от суммы снятия
    withdrawal_fee = max(withdrawal_fee, 30)                                # комиссия за вывод не менее 30 у.е.
    withdrawal_fee = min(withdrawal_fee, 600)                               # комиссия за вывод не более 600 у.е.
    return withdrawal_fee

def deposit(balance, operations_count):                                         # ДЕПОЗИТ(баланс, количество_операций):
    amount = int(input("\nВведите сумму для пополнения (кратную 50): "))
    if check_amount(amount):                                                    # сумма чека (сумма):
        balance += amount                                                       # остаток += сумма
        # Проверяем и вычитаем налог на богатство
        balance = round(deduct_wealth_tax(balance), 2)                          # баланс = округл (вычет_налог_богатства (баланс), 2

        print("Счет пополнен на", amount, "у.е.")
        print("Общий счет:", balance, "y.e.")
        operations_count += 1                                                   # число_операций += 1
        balance = calculate_interest(balance, operations_count)                 # баланс = рассчитать проценты 3% (баланс, количество_операций)

    return balance, operations_count                                            # возврат баланса, число_операций

def withdraw(balance, operations_count):                                        # ВЫВЕСТИ(баланс, количество_операций):
    amount = int(input("\nВведите сумму для снятия (кратную 50): "))
    if check_amount(amount):
        if amount <= balance:                                                   # если сумма <= баланс:
            balance = deduct_wealth_tax(balance)                                # баланс = вычесть налог на богатство (баланс)

            withdrawal_fee = round(calculate_withdrawal_fee(amount), 2)         # комиссия за снятие средств = округление (рассчитать комиссию за вывод (сумма), 2)
            balance -= withdrawal_fee                                           # баланс -= комиссия за вывод

            balance -= amount                                                   # остаток -= сумма
            print("Вы сняли", amount, "у.е.")
            print("Процент за снятие:", withdrawal_fee, "у.е.")
            print("Общий счет:", round(balance, 2), "y.e.")
            operations_count += 1
            balance = calculate_interest(balance, operations_count)            # баланс = рассчитать проценты 3% (баланс, количество_операций)
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
                balance, operations_count = deposit(balance, operations_count)  # баланс, количество_операций = депозит(баланс, количество_операций)
            case "2":
                balance, operations_count = withdraw(balance, operations_count) # баланс, количество_операций = снятие(баланс, количество_операций)
            case "3":
                print("До свидания!")
                break
            case _:
                print("Некорректный выбор. Попробуйте еще раз.")

atm()      # банкомат()



# ----------------------------------------------------------                                                                     

summ = 0
count_add = 0
count_out = 0

while True:
    # print("Ваша Сумма: ", summ)
    if summ > 5_000_000:
        print("С вас сняли налог на богатство", summ * 0.1)
        summ -= summ * 0.1

    action = input("Действие: ")

    if action == "q":
        print("Выходим из банкомата")
        print("Сумма: ", summ)
        break
    elif action == "a":
        summ_add = int(input("Сумма: "))
        if summ_add % 50 == 0:
            summ += summ_add
            count_add += 1
            if count_add % 3 == 0:
                summ *= 1.03
        else:
            print("Введена некорректная сумма (не кратна 50)")

    elif action == "o":
        summ_out = int(input("Сумма: "))
        comission = summ_out * 0.015
        if comission < 30:
            comission = 30
        elif comission > 600:
            comission = 600

        if summ_out + comission > summ:
            print("Недостаточно средств")

        else:
            if summ_out % 50 == 0:
                summ -= summ_out + comission

                count_out += 1
                if count_out % 3 == 0:
                    summ *= 1.03
            else:
                print("Введена некорректная сумма")

    print(f"Сумма: {summ}")