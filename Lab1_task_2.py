from task_1 import Cat, BankAccount, Smartphone  # Импортируем классы из задания 1

# Создаем объекты классов
cat1 = Cat("Murka", 3, "British Shorthair")
account1 = BankAccount("1234567890", 1000.0, "USD")
phone1 = Smartphone("Samsung", "Galaxy S22", 128)

if __name__ == "__main__":
    # Проверяем создание объектов
    print("Созданные объекты:")
    print(cat1)
    print(f"Счет: {account1.get_balance()}")
    print(f"Телефон: {phone1.info()}")
    print()

    # Проверка методов с некорректными аргументами
    try:
        # Пытаемся установить отрицательный возраст для кота
        print("Попытка установить отрицательный возраст:")
        cat1.add_data("Tom", -1, "Siamese")
    except ValueError as e:
        print(f'Ошибка: {e}')

    try:
        # Пытаемся пополнить счет отрицательной суммой
        print("\nПопытка пополнить счет отрицательной суммой:")
        account1.deposit(-100)
    except ValueError as e:
        print(f'Ошибка: {e}')

    try:
        # Пытаемся создать телефон с объемом памяти меньше минимального
        print("\nПопытка создать телефон с 8GB памяти:")
        phone2 = Smartphone("Xiaomi", "Redmi Note", 8)
    except Exception as e:
        print(f'Ошибка: {e}')
    else:
        print(f"Создан телефон с автоматически установленным минимумом: {phone2.info()}")












