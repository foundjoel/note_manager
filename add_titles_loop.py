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

status = input('Введите статус заметки:')
print('Статус заметки:', status)

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
    ('Статус:', f'Активность: {status}, Для заголовка: {title}'),
    ('Дата создания:', ['День:', created_date, 'Месяц:', created_month]),
    ('Дата дедлайна:', ['День:', issue_date, 'Месяц:', issue_month])
]
print('Данные о заметке:', note)
