class Product:
    """Класс продукта."""

    def __init__(self, id: int, name: str, url: str, price: str, disc_price: int, brand: str):
        """Инициализация класса."""

        self.id = id
        self.name = name
        self.price = price
        self.disc_price = disc_price
        self.brand = brand

    def as_dict(self) -> dict:
        """Функция для получения атрибутов класса в виде словаря."""

        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'disc_price': self.disc_price,
            'brand': self.brand
        }
