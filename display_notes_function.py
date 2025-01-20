notes = [
    {'username': 'Алексей',
    'title': 'Список дел',
    'content': 'Купить продукты на неделю',
    'status': 'новая',
    'created_date': '27-11-2024',
    'issue_date': '30-11-2024'},
{'username': 'Марина',
    'title': 'Список дел',
    'content': 'Купить озонатор воздуха',
    'status': 'новая',
    'created_date': '27-11-2024',
    'issue_date': '30-11-2024'}
]

def display_notes():
    if not notes:
        print('Список пуст.')
    else:
        print('\nВаши заметки: ')
        for index, titles in enumerate(notes, start=1):
            print('________________')
            print(f'Заметка № {index}:')
            print(f" Имя: {titles['username']}")
            print(f" Ваши заголовки: {titles['title']}")
            print(f" Описание: {titles['content']}")
            print(f" Статус: {titles['status']}")
            print(f" Дата создания: {titles['created_date']}")
            print(f" Дата дедлайна: {titles['issue_date']}")
        quit('Конец работы программы.')

display_notes()