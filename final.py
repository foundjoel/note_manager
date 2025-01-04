username = input('Введите ваше имя:')
print('Имя пользователя:', username)
title = input('Введите заголовок:')
title2 = input('Введите заголовок:')
title3 = input('Введите заголовок:')
print('Заголовок заметки:', title, title2, title3)
content = input('Введите описание заметки:')
print('Описание заметки:', content)
status = input('Введите статус заметки:')
print('Статус заметки:', status)
created_date = int(input('Введите день заметки:'))
created_month = int(input('Введите месяц заметки:'))
print('Дата заметки:', (f'День: {created_date}, Месяц: {created_month}'))
issue_date = int(input('Введите дату дедлайна:'))
issue_month = int(input('Введите месяц заметки:'))
print('Дедлайн:', (f'День: {issue_date}, Месяц: {issue_month}'))

note = [
    ('Имя пользователя:', username),
    ('Заголовок:', [title, title2, title3]),
    ('Описание:', content),
    ('Статус:', (f'Активность: {status}, Для заголовка: {title, title2, title3}')),
    ('Дата создания:', ['День:', created_date, 'Месяц', created_month]),
    ('Дата дедлайна:', ['День:', issue_date, 'Месяц', issue_month])
]
print('Данные о заметке:', note)
