username = input('Введите ваше имя: ')
print('Имя пользователя: ', username)

title_1 = input("Введите заголовок: ")
print(title_1)
title_2 = input("Введите заголовок: ")
print(title_2)
title_3 = input("Введите заголовок: ")
print(title_3)
all_titles = [title_1 + ', ' + title_2 + ', ' + title_3]
print('Список заголовков: ', all_titles)

content = input('Введите описание заметки: ')
print('Описание заметки: ', content)
status = input('Введите статус заметки: ')
print('Статус заметки: ', status)
created_date = int(input('Введите день заметки: '))
created_month = int(input('Введите месяц заметки: '))
print('Дата заметки:', (f'День: {created_date}, Месяц: {created_month}'))
issue_date = int(input('Введите дату дедлайна: '))
issue_month = int(input('Введите месяц дедлайна: '))
print('Дата заметки:', (f'День: {issue_date}, Месяц: {issue_month}'))
