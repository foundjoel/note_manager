title = []
while True:
    header = input("Введите заголовок или 'стоп' для завершения:")
    if header.lower() == 'стоп':
        break
    title.append(header)
print("\nСписок заголовков:")
for idx, h in enumerate(title, start=1):
    print(f"{idx}. {h}")
