#Функция создания заметок.
def create_notes(all_notes):
    while True:
        user_add_note = input('Хотите добавить новую заметку? Да или нет. ')
        if user_add_note.lower() == 'да':
            user_name = input('Введите имя: ')
            print('Имя: ', user_name)

            titles = []
            while True:
                header = input("Введите заголовок или 'стоп' для завершения: ")
                if header.lower() == 'стоп':
                    break
                titles.append(header)
            print('\nСписок заголовков: ')
            for idx, title in enumerate(titles, start=1):
                print(f"{idx}. {title}")

            add_content = input('Введите описание заметки: ')
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

            while True:
                try:
                    deadline_str = input("Введите дату дедлайна в формате дд-мм-гггг: ")
                    deadline_date = datetime.strptime(deadline_str, "%d-%m-%Y").date()
                    time_difference = deadline_date - current_date
                    days_difference = time_difference.days
                    if days_difference < 0:
                        print(f"Внимание! Дедлайн истёк {abs(days_difference)} дней назад.")
                    elif days_difference == 0:
                        print("Дедлайн сегодня!")
                    else:
                        print(f"До дедлайна осталось {days_difference} дней.")
                    break
                except ValueError:
                    print("Ошибка! Пожалуйста, введите дату в правильном формате (день-месяц-год).")
                    print("Пример: 01-01-2025")
                except Exception as a:
                    print(f"Произошла непредвиденная ошибка: {str(a)}")
                    print("Пожалуйста, попробуйте снова.")

            all_notes.append({'username': user_name, 'title': titles, 'content': add_content, 'status': current_status,
                              'issue_date': days_difference})
            print('\nСписок заметок: ')
            for index, title in enumerate(all_notes, start=1):
                print(f"{index}. Имя: {title['username']}")
                print(f" Ваши заголовки: {title['title']}")
                print(f" Описание: {title['content']}")
                print(f" Статус: {title['status']}")
                print(f" До дедлайна осталось: {title['issue_date']}")

        elif user_add_note.lower() == 'нет':
            print('\nСписок заметок: ')
            for index, title in enumerate(all_notes, start=1):
                print(f"{index}. Имя: {title['username']}")
                print(f" Ваши заголовки: {title['title']}")
                print(f" Описание: {title['content']}")
                print(f" Статус: {title['status']}")
                print(f" До дедлайна осталось: {title['issue_date']}")
            break
        else:
            print('Неверный ввод, попробуйте ещё раз.')
            continue

#Функция обновления заметок.
def update_notes(all_notes):
    show_notes(all_notes)

    if not all_notes:
        print("Нет доступных заметок для обновления.")
        return

    note_index = int(input("Введите номер заметки для обновления: ")) - 1
    if 0 <= note_index < len(all_notes):
        field_to_update = input('Введите поле, которое хотите изменить (username, title, content, status): ')
        if field_to_update in all_notes[note_index]:
            new_value = input(f'Введите новое значение для {field_to_update}: ')
            if field_to_update == 'title':
                all_notes[note_index][field_to_update] = [new_value]
            else:
                all_notes[note_index][field_to_update] = new_value
            print('Заметка обновлена.')
        else:
            print('Ошибка. Повторите попытку')
    else:
        print('Ошибка. Номера заметки не существует')

#Основной блок меню.
while True:
    print(f"\nВыбор меню:"
          f"\nСоздать заметку (1)"
          f"\nОбновить заметку (2)"
          f"\nВыйти из программы (6)")
    
    select_menu = input('\nВыберите нужный пункт: ')

    try:
        if select_menu == '1':
            create_notes(all_notes)
        elif select_menu == '2':
            update_notes(all_notes)
        elif select_menu == '3':
            quit('Конец работы программы.')
        else:
            print('Неверный ввод. Повторите попытку.')
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {str(e)}")