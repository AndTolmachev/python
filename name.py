print("Исключенное Имя")
user_data = {'name': input('Напиши свое имя?\n'),
             'age': int(input('Сколько тебе лет?\n')),
             'pat_name': input('Как зовут твоего питомца?\n'),
             'game_liking': ''
             }
game_liking_answer = input('Нравится ли вам играть?(Да/Нет)')
if game_liking_answer == 'Да':
    user_data['game_liking'] = True
else:
    user_data['game_liking'] = False
if user_data['age'] < 18:
    print('Тебе нельзя играть, ты слишком молод!')
elif user_data['age'] > 90:
    answer = input('Вы уверены, что хотите играть? Мы боимся утомить Вас.(Да/Нет)\n')
    if answer == 'Нет':
        print('Всего хорошего,', user_data['name'])
    elif answer == 'Да':
        answer = input('Вы точно уверены.(Да/Нет)\n')
        if answer == 'Нет':
            print('Всего хорошего,', user_data['name'])
        elif answer == 'Да':
            print('Приветствую,', user_data['name'])
            print('Я могу назвать буквы алфавита, которых нет в твоем имени!')
            for i in 'абвгдеёжзиклмнопрстуфхцчшщэьыъэюя':
                if i not in user_data['name'].lower():
                    print(i)
else:
    print('Приветствую,', user_data['name'])
    print('Я могу назвать буквы алфавита, которых нет в твоем имени!')
    for i in 'абвгдеёжзиклмнопрстуфхцчшщэьыъэюя':
        if i not in user_data['name'].lower():
            print(i)


