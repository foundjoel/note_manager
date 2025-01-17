welcome_print = 'Добро пожаловать в менеджер заметок!'
print(welcome_print)

from datetime import datetime
current_date = datetime.now().date()
print('Сегодняшняя дата:', current_date.strftime("%d-%m-%Y"))

notes = [
    {'name: ': 'Анна',
    'title: ': 'ДР',
    'content: ': 'забрать подарок с вб'},
{'name: ': 'Алексей',
    'title: ': 'покупки',
    'content: ': 'купить бекон, сливки, шампиньоны'}
]
if not notes:
    print('Список пуст.')
else:
    print('\nВаши заметки: ')
    for index, note in enumerate(notes, start=1):
        print(f'{index}. {note}')

select_delete = input('Вы можете удалить заметку по имени и заголовку. Напишите слово-ключ: ')
print(select_delete)

updated_notes = []

for notes in notes:
    if notes['name: '] != select_delete and notes['title: '] != select_delete:
        updated_notes.append(notes)
        print('Не найдено.')
        break
    elif notes['name: '] == select_delete and notes['title: '] == select_delete:
        del notes

if not updated_notes:
    print('Список пуст.')
else:
    print('\nОстались следующие заметки: ')
    for index, note in enumerate(updated_notes, start=1):
        print(f"{index}. Имя: {note['name: ']}")
        print(f" Имя: {note['title: ']}")
        print(f" Имя: {note['content: ']}")