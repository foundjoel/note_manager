username = input('Введите ваше имя:')
print('Имя пользователя:', username)

title = []
while True:
    header = input("Введите заголовок (или 'стоп' для завершения):")
    if header.lower() == 'стоп':
        break
    title.append(header)
print("\nСписок заголовков:")
for idx, h in enumerate(title, start=1):
    print(f"{idx}. {h}")

content = input('Введите описание заметки:')
print('Описание заметки:', content)

statuses = []
current_status = 'В процессе'
print(f'Текущий статус заметки: {current_status}')
possible_statuses = ['выполнено', 'в процессе', 'отложено']
print("Доступные статусы: " + ", ".join(possible_statuses))
while True:
    new_status = input('Введите новый статус заметки: ')
    if new_status in possible_statuses:
        current_status = new_status
        break
    else:
        print('Некорректный статус. Пожалуйста, выберите один из доступных статусов.')
print(f'\nОбновлённый статус заметки: {current_status}')

created_date = int(input('Введите день заметки:'))
created_month = int(input('Введите месяц заметки:'))
print('Дата заметки:', f'День: {created_date}, Месяц: {created_month}')

issue_date = int(input('Введите дату дедлайна:'))
issue_month = int(input('Введите месяц заметки:'))
print('Дедлайн:', f'День: {issue_date}, Месяц: {issue_month}')

note = [
    ('Имя пользователя:', username),
    ('Заголовок:', [title]),
    ('Описание:', content),
    ('Статус:', current_status),
    ('Дата создания:', ['День:', created_date, 'Месяц:', created_month]),
    ('Дата дедлайна:', ['День:', issue_date, 'Месяц:', issue_month])
]
print('\nИнформация о заметке: ' )
for index, about_note in enumerate(note, start=1):
    print(f"{index}. {about_note}")
