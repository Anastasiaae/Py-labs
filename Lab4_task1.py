# TODO: описать базовый класс
from typing import List, Optional

class Animal:
    """
    Базовый класс, представляющий животное.

    Атрибуты:
        name (str): Имя животного.
        age (int): Возраст животного в годах.
        _species (str): Вид животного (инкапсулирован, так как не должен изменяться после создания).
    """

    def __init__(self, name: str, age: int, species: str) -> None:
        """
        Конструктор класса Animal.

        Args:
            name: Имя животного.
            age: Возраст животного.
            species: Вид животного.
        """
        self.name = name
        self.age = age
        self._species = species  # Инкапсулируем, чтобы вид нельзя было изменить напрямую

    def make_sound(self) -> str:
        """
        Возвращает звук, который издаёт животное.

        Returns:
            Строка с описанием звука.
        """
        return "Some generic animal sound."

    def get_species(self) -> str:
        """
        Возвращает вид животного.

        Returns:
            Вид животного.
        """
        return self._species

    def __str__(self) -> str:
        """
        Возвращает строковое представление животного.

        Returns:
            Строка с именем, возрастом и видом.
        """
        return f"{self.name}, {self.age} years old, {self._species}"

    def __repr__(self) -> str:
        """
        Возвращает формальное строковое представление объекта.

        Returns:
            Строка, которую можно использовать для создания объекта.
        """
        return f"Animal(name='{self.name}', age={self.age}, species='{self._species}')"
# TODO: описать дочерний класс
class Cat(Animal):
    """
    Дочерний класс, представляющий кошку. Наследуется от Animal.

    Дополнительные атрибуты:
        breed (str): Порода кошки.
        favorite_foods (List[str]): Любимые продукты кошки.
    """

    def __init__(self, name: str, age: int, breed: str, favorite_foods: Optional[List[str]] = None) -> None:
        """
        Конструктор класса Cat. Расширяет конструктор Animal.

        Args:
            name: Имя кошки.
            age: Возраст кошки.
            breed: Порода кошки.
            favorite_foods: Список любимых продуктов (по умолчанию None).
        """
        super().__init__(name, age, "Felis catus")  # Вид кошки всегда Felis catus
        self.breed = breed
        self.favorite_foods = favorite_foods if favorite_foods else ["fish", "meat"]

    def make_sound(self) -> str:
        """
        Перегружает метод make_sound() из Animal, так как кошки издают специфичный звук.

        Returns:
            Строка "Meow!".
        """
        return "Meow!"

    def eat(self, food: str) -> str:
        """
        Возвращает реакцию кошки на еду.

        Args:
            food: Предлагаемая еда.

        Returns:
            Строка с реакцией кошки.
        """
        if food in self.favorite_foods:
            return f"{self.name} happily eats {food}!"
        else:
            return f"{self.name} sniffs {food} and walks away."

    def __str__(self) -> str:
        """
        Перегружает __str__ для более детального описания кошки.

        Returns:
            Строка с именем, возрастом, породой и видом.
        """
        return f"{self.name}, {self.age} years old, {self.breed} cat ({self.get_species()})"

    def __repr__(self) -> str:
        """
        Перегружает __repr__ для создания точного представления объекта.

        Returns:
            Строка, которую можно использовать для создания объекта.
        """
        return f"Cat(name='{self.name}', age={self.age}, breed='{self.breed}', favorite_foods={self.favorite_foods})"
