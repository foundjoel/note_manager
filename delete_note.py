welcome_print = 'Добро пожаловать в менеджер заметок!'
print(welcome_print)

from datetime import datetime

current_date = datetime.now().date()
print('Сегодняшняя дата:', current_date.strftime("%d-%m-%Y"))

notes = [
    {'name': 'Анна', 'title': 'ДР', 'content': 'забрать подарок с вб'},
    {'name': 'Алексей', 'title': 'покупки', 'content': 'купить бекон, сливки, шампиньоны'}
]

while True:
    if not notes:
        print('Список пуст.')
        break

    print('\nВаши заметки: ')
    for index, note in enumerate(notes, start=1):
        print(f"{index}. Имя: {note['name']}")
        print(f" Заголовок: {note['title']}")
        print(f" Описание: {note['content']}")

    select_delete = input(
        'Вы можете удалить заметку по имени и заголовку. Напишите слово-ключ (или "стоп" для выхода): ')

    if select_delete.lower() == 'стоп':
        break

    updated_notes = []
    found = False

    for note in notes:
        if note['name'] == select_delete or note['title'] == select_delete:
            found = True
        else:
            updated_notes.append(note)

    if found:
        notes = updated_notes
        print('Заметка удалена.')
    else:
        print('Не найдено.')

    if not notes:
        print('Список пуст.')
        break
