from datetime import datetime

print('Добро пожаловать в менеджер заметок! Вы можете добавить новую заметку.')

current_date = datetime.now().date()
print('Сегодняшняя дата:', current_date.strftime("%d-%m-%Y"))

username = input('Введите ваше имя:')
print('Имя пользователя:', username)

titles = []
while True:
    header = input("Введите заголовок или 'стоп' для завершения: ")
    if header.lower() == 'стоп':
        break
    titles.append(header)
print('\nСписок заголовков: ')
for idx, title in enumerate(titles, start=1):
    print(f"{idx}. {title}")

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

from datetime import datetime
while True:
    try:
        deadline_str = input("Введите дату дедлайна в формате дд-мм-гггг: ")
        deadline_date = datetime.strptime(deadline_str, "%d-%m-%Y").date()
        time_difference = deadline_date - current_date
        days_difference = time_difference.days
        if days_difference < 0:
            print(f"Внимание! Дедлайн истёк {abs(days_difference):02d} дней назад.")
        elif days_difference == 0:
            print("Дедлайн сегодня!")
        else:
            print(f"До дедлайна осталось {days_difference:02d} дней.")
        break
    except ValueError:
        print("Ошибка! Пожалуйста, введите дату в правильном формате (день-месяц-год).")
        print("Пример: 01-01-2025")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {str(e)}")
        print("Пожалуйста, попробуйте снова.")

note = [
    ('Имя пользователя:', username),
    ('Заголовок:', titles),
    ('Описание:', content),
    ('Статус:', current_status),
    ('Дата дедлайна:', days_difference)
]
print('\nИнформация о заметке: ' )
for index, about_note in enumerate(note, start=1):
    print(f"{index}. {about_note}")