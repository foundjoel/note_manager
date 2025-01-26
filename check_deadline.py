from datetime import datetime

current_date = datetime.now().date()
print('Сегодняшняя дата:', current_date.strftime("%d-%m-%Y"))

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
