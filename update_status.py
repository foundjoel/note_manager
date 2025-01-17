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
