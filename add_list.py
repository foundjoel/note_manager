username = input('Введите ваше имя: ')
print('Имя пользователя: ', username)

titles = []
while True:
    title = input('Введите заголовок: ')
    title2 = input('Введите заголовок: ')
    title3 = input('Введите заголовок: ')
    titles.append(title, title2, title3)
print('\nСписок заголовков: ')
for idx, title in enumerate(titles, start=1):
    print(f"{idx}. {title}")

print('Заголовок заметки:', title, title2, title3)
content = input('Введите описание заметки: ')
print('Описание заметки: ', content)
status = input('Введите статус заметки: ')
print('Статус заметки: ', status)
created_date = int(input('Введите день заметки: '))
created_month = int(input('Введите месяц заметки: '))
print('Дата заметки:', (f'День: {created_date}, Месяц: {created_month}'))
issue_date = int(input('Введите дату дедлайна: '))
issue_month = int(input('Введите месяц заметки: '))
print('Дедлайн:', (f'День: {issue_date}, Месяц: {issue_month}'))
