# Guido van Rossum <guido@python.org>


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_no_umbrella():
    print(
        'Утка маляр решила дойти до бара без зонтика и попала под ливень. 🌧️'
    )
    print('К счастью, недалеко от нее оказался магазин одежды. 🧥')
    shop = {
        'Плащ': '450',
        'Шляпа': '200',
        'Резиновые сапоги': '350',
        'Шарф': '150',
        'Носки': '100'
    }
    print('Аксессуары в магазине:')
    for item, price in shop.items():
        print(f' - {item}: {price} рублей')
    purchase = ''
    while purchase not in shop:
        purchase = input(
            'Выберите, что купить (или нажмите Enter,'
            ' чтобы ничего не покупать): '
        ).capitalize()
        if purchase == '':
            break
    if purchase:
        print(f'Утка купила {purchase.lower()} и немного согрелась.')
    else:
        print('Утка решила не покупать ничего и промокла ещё сильнее!')

    print('Утка все-таки добралась до бара и заказала самый горячий напиток.')
    hot_menu = {
        'Горячий шоколад': '220',
        'Глинтвейн': '300',
        'Чай': '200',
        'Кофе': '250'
    }
    print('Горячие напитки:')
    for key, value in hot_menu.items():
        print(f' - {key}: {value} рублей')
    hot_drink = ''
    while hot_drink not in hot_menu:
        hot_drink = input('Выберите горячий напиток: ').capitalize()
    print(
        f'Утка решила выпить {hot_drink.lower()}, чтобы согреться.'
    )

    ways = {'картой', 'наличными', 'улыбкой', 'криптовалютой'}
    way = ''
    while way not in ways:
        print('Как ей оплатить заказ?')
        print('Варианты:', '/'.join(ways))
        way = input('Выберите способ оплаты: ').lower()
    if purchase:
        print(
            f'Утка заплатила {hot_menu[hot_drink]} рублей {way} '
            'и отправилась домой в новом образе. 🦆🧣'
        )
    else:
        print(
            'Утка согревшаяся и довольная, что сэкономила деньги на покупке '
            'одежды, отправилась домой!'
        )


def step2_umbrella():
    print(
        'Утка дошла до бара 🍸, '
        'потому что зонтик спас ее от проливного дождя. ☔'
    )
    print('Утка выбирает, что бы выпить')
    menu = {
        'Латте': '150',
        'Сок': '200',
        'Глинтвейн': '300',
        'Вино': '400',
        'Пина колада': '400'
    }
    print('Барное меню:')
    for key, value in menu.items():
        print(f' - {key.capitalize()}: {value} рублей')
    drink = ''
    while drink not in menu:
        drink = input('Выберите напиток: ').capitalize()
    print(f'Утка выбрала: {drink}')
    print(f'Утке принесли {drink.lower()} и она довольная попросила счет 🧾')
    print('Утке принесли счет и спросили, как она будет платить 💲')
    way = ''
    ways = {'картой', 'наличными', 'улыбкой'}
    while way not in ways:
        print('Выберите, чем платить утке: {}/{}/{}'.format(*ways))
        way = input().lower()
    print(
        f'Утка оплатила счет ({menu[drink]} рублей) {way} '
        'и довольная пошла домой под зонтиком. ☂️'
    )


if __name__ == '__main__':
    step1()
