notes = [
    {'username': 'Алексей',
     'title': 'Список дел',
     'content': 'Купить продукты на неделю',
     'status': 'новая',
     'created_date': '27-11-2024',
     'issue_date': '30-11-2024'},
    {'username': 'Марина',
     'title': 'Учёба',
     'content': 'доделать третий этап',
     'status': 'в процессе',
     'created_date': '18-01-2025',
     'issue_date': '19-01-2025'},
    {'username': 'Крестик квадробер',
     'title': 'Кошачьи дела',
     'content': 'Хулиганить',
     'status': 'в процессе',
     'created_date': '27-12-2024',
     'issue_date': '06-01-2025'},
]

def search_notes(notes, keyword = None, status = None):
    while True:

        user_input = input("Введите ключевое слово или статус: ")
        keyword, status = [item.strip() for item in user_input.split(',')] if ',' in user_input else (user_input.strip(), None)

        results = []
        for note in notes:
            if keyword and status:
                if (keyword in note['title'] or
                    keyword in note['content'] or
                    keyword in note['username']) and note['status'] == status:
                    results.append(note)
                    break
            elif keyword:
                if (keyword in note['title'] or
                    keyword in note['content'] or
                    keyword in note['username']):
                    results.append(note)
                    break
            elif status:
                if status.lower() in note['status'].lower():
                    results.append(note)
                    break

        if results:
            for note in results:
                print('Вот что найдено по вашему запросу: ')
                print('__________________________________')
                print(f"Имя: {note['username']}"
                      f"\nЗаголовок: {note['title']}"
                      f"\nОписание: {note['content']}"
                      f"\nСтатус: {note['status']}"
                      f"\nДата создания: {note['created_date']}"
                      f"\nДата дедлайна: {note['issue_date']}")
        else:
            print('Список пуст.')

        return results

search_notes(notes, keyword = None, status = None)