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

def main():
    current_status = "В процессе"
    print(f"Текущий статус заметки: {current_status}")
    possible_statuses = ["выполнено", "в процессе", "отложено"]
    print("Доступные статусы: " + ", ".join(possible_statuses))
    while True:
        new_status = input("Введите новый статус заметки:").strip()
        if new_status in possible_statuses:
            current_status = new_status
            break
        else:
            print("Некорректный статус. Пожалуйста, выберите один из доступных статусов.")
    print(f"Обновлённый статус заметки: {current_status}")
if __name__ == "__main__":
    main()

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
    ('Статус:', ),
    ('Дата создания:', ['День:', created_date, 'Месяц:', created_month]),
    ('Дата дедлайна:', ['День:', issue_date, 'Месяц:', issue_month])
]
print('Данные о заметке:', note)