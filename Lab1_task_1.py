import doctest

class Cat:
    """
    Класс, описывающий кота.

    Атрибуты:
    - name (str): имя кота
    - age (int): возраст кота в годах (не может быть отрицательным)
    - breed (str): порода кота
    """

    def __init__(self, name: str = None, age: int = None, breed: str = None):
        """
        Создание объекта класса Cat.

        :param name: имя кота
        :param age: возраст кота
        :param breed: порода кота

        Примеры:
        >>> cat1 = Cat("Murka", 3, "British Shorthair")

        """
        self.add_data(name, age, breed)

    def add_data(self, name: str = None, age: int = None, breed: str = None) -> None:
        """
        Добавление или обновление данных о коте.

        :param name: имя кота
        :param age: возраст кота (должен быть >= 0)
        :param breed: порода кота
        :raises ValueError: если возраст отрицательный

        Примеры:
        >>> cat = Cat()
        >>> cat.add_data("Tom", 2, "Siamese")
        >>> cat.add_data("Tom", -1, "Siamese")
        Traceback (most recent call last):
        ...
        ValueError: Возраст не может быть отрицательным
        """
        if age is not None and age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        if name is not None:
            self.name = name
        if age is not None:
            self.age = age
        if breed is not None:
            self.breed = breed

    def get_human_age(self, multiplier: int = 7) -> int:
        """
        Возвращает примерный возраст кота в "человеческих" годах.

        :param multiplier: множитель для пересчета (по умолчанию 7)
        :return: возраст в "человеческих" годах

        Примеры:
        >>> cat = Cat("Barsik", 3)
        >>> cat.get_human_age()
        21
        >>> cat.get_human_age(6)
        18
        """
        return self.age * multiplier

    def __str__(self) -> str:
        """Возвращает строковое представление кота."""
        return f"Кот {self.name}, возраст {self.age}, порода {self.breed}"


class BankAccount:
    """
    Класс, описывающий банковский счет.

    Атрибуты:
    - account_number (str): номер счета
    - balance (float): текущий баланс (не может быть отрицательным)
    - currency (str): валюта счета (по умолчанию "RUB")
    """

    def __init__(self, account_number: str, balance: float = 0.0, currency: str = "RUB"):
        """
        Создание банковского счета.

        :param account_number: номер счета
        :param balance: начальный баланс
        :param currency: валюта счета

        Примеры:
        >>> account1 = BankAccount("1234567890", 1000.0)
        >>> account2 = BankAccount("0987654321", 500.0, "USD")
        """
        self.account_number = account_number
        self.currency = currency
        self.deposit(balance)  # Используем метод deposit для валидации баланса

    def deposit(self, amount: float) -> float:
        """
        Пополнение счета.

        :param amount: сумма для пополнения (должна быть > 0)
        :return: новый баланс
        :raises ValueError: если сумма пополнения <= 0

        Примеры:
        >>> account = BankAccount("123")
        >>> account.deposit(1000)
        1000.0
        >>> account.deposit(-100)
        Traceback (most recent call last):
        ...
        ValueError: Сумма пополнения должна быть положительной
        """
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.balance = getattr(self, 'balance', 0) + amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """
        Снятие денег со счета.

        :param amount: сумма для снятия (должна быть > 0 и <= баланса)
        :return: новый баланс
        :raises ValueError: если сумма некорректна

        Примеры:
        >>> account = BankAccount("123", 1000)
        >>> account.withdraw(500)
        500.0
        >>> account.withdraw(1000)
        Traceback (most recent call last):
        ...
        ValueError: Недостаточно средств на счете
        """
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете")
        self.balance -= amount
        return self.balance

    def get_balance(self) -> str:
        """
        Возвращает строку с текущим балансом.

        :return: строка с балансом и валютой

        Примеры:
        >>> account = BankAccount("123", 1500.50, "RUB")
        >>> account.get_balance()
        '1500.5 RUB'
        """
        return f"{self.balance} {self.currency}"


class Smartphone:
    """
    Класс для представления смартфона.

    Атрибуты:
    - brand (str): производитель телефона
    - model (str): модель телефона
    - storage (int): объем памяти в ГБ (не может быть меньше 16)
    - on (bool): состояние телефона (включен/выключен)
    """

    def __init__(self, brand: str, model: str, storage: int = 64):
        """
        Создание объекта класса Smartphone.

        :param brand: производитель телефона
        :param model: модель телефона
        :param storage: объем памяти в ГБ (по умолчанию 64)

        Примеры:
        >>> phone1 = Smartphone("Apple", "iPhone 13", 128)
        >>> phone2 = Smartphone("Samsung", "Galaxy S21")
        >>> phone3 = Smartphone("Xiaomi", "Redmi Note", 8)  # Автоматически станет 16GB
        """
        self.brand = brand
        self.model = model
        self.storage = max(16, storage)  # Минимум 16ГБ
        self.on = False

    def power(self, state: bool = True) -> str:
        """
        Включение/выключение телефона.

        :param state: желаемое состояние (True - включить, False - выключить)
        :return: строковое представление состояния

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 12")
        >>> phone.power(True)
        'Включен'
        >>> phone.power(False)
        'Выключен'
        """
        self.on = state
        return "Включен" if state else "Выключен"

    def info(self) -> str:
        """
        Возвращает информацию о телефоне.

        :return: строка с информацией о телефоне

        Примеры:
        >>> phone = Smartphone("Samsung", "Galaxy S22", 256)
        >>> phone.info()
        'Samsung Galaxy S22, 256GB'
        """
        return f"{self.brand} {self.model}, {self.storage}GB"

    def __str__(self) -> str:
        """
        Строковое представление телефона.

        :return: строка с полной информацией о телефоне

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 14", 128)
        >>> str(phone)
        'Apple iPhone 14, 128GB (состояние: Выключен)'
        """
        state = "Включен" if self.on else "Выключен"
        return f"{self.brand} {self.model}, {self.storage}GB (состояние: {state})"


if __name__ == "__main__":
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    testmod()