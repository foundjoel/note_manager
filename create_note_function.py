print('Добро пожаловать в менеджер заметок! Вы можете добавить новую заметку.')

from datetime import datetime

current_date = datetime.now().date()
print('Сегодняшняя дата:', current_date.strftime("%d-%m-%Y"))

def create_notes():
    while True:

        all_notes = []
        while True:
            user_add_note = input('Хотите добавить новую заметку? Да или нет. ')
            if user_add_note.lower() == 'да':

                user_name = input('Введите имя: ' )
                print('Имя: ', user_name)

                titles = []
                while True:
                    header = input("Введите заголовок или 'стоп' для завершения: " )
                    if header.lower() == 'стоп':
                        break
                    titles.append(header)
                print('\nСписок заголовков: ' )
                for idx, title in enumerate(titles, start=1):
                    print(f"{idx}. {title}")

                add_content = input('Введите описание заметки: ' )
                print('Описание заметки: ', add_content)

                current_status = 'В процессе'
                print(f'Текущий статус заметки: {current_status}')
                possible_statuses = ['выполнено', 'новая', 'в процессе', 'отложено']
                print("Доступные статусы: " + ", ".join(possible_statuses))
                while True:
                    new_status = input('Введите новый статус заметки: ')
                    if new_status in possible_statuses:
                        current_status = new_status
                        break
                    else:
                        print('Некорректный статус. Пожалуйста, выберите один из доступных статусов.')
                print(f'\nОбновлённый статус заметки: {current_status}')

                from datetime import datetime
                while True:
                    try:
                        deadline_str = input("Введите дату дедлайна в формате дд-мм-гггг: ")
                        deadline_date = datetime.strptime(deadline_str, "%d-%m-%Y").date()
                        time_difference = deadline_date - current_date
                        days_difference = time_difference.days
                        if days_difference < 0:
                            print(f"Внимание! Дедлайн истёк {abs(days_difference):02d} дней назад.")
                        elif days_difference == 0:
                            print("Дедлайн сегодня!")
                        else:
                            print(f"До дедлайна осталось {days_difference:02d} дней.")
                        break
                    except ValueError:
                        print("Ошибка! Пожалуйста, введите дату в правильном формате (день-месяц-год).")
                        print("Пример: 01-01-2025")
                    except Exception as a:
                        print(f"Произошла непредвиденная ошибка: {str(a)}")
                        print("Пожалуйста, попробуйте снова.")

                all_notes.append({'Имя: ': user_name, 'Ваши заголовки: ': titles, 'Описание: ': add_content, 'Статус: ': current_status, 'До дедлайна осталось: ': days_difference})
                print('\nСписок заметок: ')
                for index, title in enumerate(all_notes, start=1):
                    print(f"{index}. Имя: {title['Имя: ']}")
                    print(f" Ваши заголовки: {title['Ваши заголовки: ']}")
                    print(f" Описание: {title['Описание: ']}")
                    print(f" Статус: {title['Статус: ']}")
                    print(f" До дедлайна осталось: {title['До дедлайна осталось: ']}")

            elif user_add_note.lower() == 'нет':
                print('\nВаши заметки: ')
                for index, titles in enumerate(all_notes, start=1):
                    print(f"{index}. Имя: {titles['Имя: ']}")
                    print(f" Ваши заголовки: {titles['Ваши заголовки: ']}")
                    print(f" Описание: {titles['Описание: ']}")
                    print(f" Статус: {titles['Статус: ']}")
                    print(f" До дедлайна осталось: {titles['До дедлайна осталось: ']}")
                quit('Конец работы программы.')
            else:
                print('Неверный ввод, попробйуте ещё раз.')
                continue

while True:
    try:
        start = input('Начать работу заметки? Ответьте да или нет. ')
        if start.lower() == 'да':
            print(create_notes())
        elif start.lower() == '':
            print('Завершение работы заметок.')
            quit()
        else:
            print('Ошибка ввода. Попробуйте снова. ')
            continue
    except ValueError:
        print('Ошибка ввода. Пожалуйста, ответьте да или нет. ')
    except Exception as e:
        print('Попробуйте снова. ', {str(e)})