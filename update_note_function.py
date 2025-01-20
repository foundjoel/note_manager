def update_note():
    username = ['Алексей'],
    title = ['Список покупок'],
    content = ['Купить продукты'],
    status = ['новая'],
    created_date = ['27-11-2024'],
    issue_date = ['30-11-2024'],

    note = username + title + content + status + created_date + issue_date

    print('Ваши заметки: ', note)

    while True:
        update_keys = input('Хотите обновить словарь? Ответье да или нет. ')
        if update_keys.lower() == 'да':
            print('Доступные поля для обновления: username, title, content, status, created_date, issue_date')
            select_keys = input('Введите поле, которое хотите изменить: ')
            select_keys.lower()
            print(select_keys)
            for select_keys in note:
                new_keys = input(f'Введите новое значение для {select_keys}: ')
                print(new_keys)
                note = new_keys
                print(f'Заметка обновлена: {new_keys} = {note}')
                break
        elif update_keys.lower() == 'нет':
            quit('Завершение программы.')
        else:
            print('Неверный ввод. Попробуйте снова. ')
            continue

update_note()