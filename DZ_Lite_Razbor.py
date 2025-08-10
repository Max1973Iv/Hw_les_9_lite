# Интернет-магазин

# 1. Базовый класс Product и производные классы для различных типов продуктов

class Product:
    """
    Базовый класс, представляющий продукт.
    """
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_details(self):
        return f"Продукт: {self.name}, Цена: {self.price} руб."

class Electronics(Product):
    """
    Класс, представляющий электронный продукт, наследующий класс Product.
    """
    def __init__(self, name, price, brand, warranty_period):
        super().__init__(name, price)
        self.brand = brand
        self.warranty_period = warranty_period

    def get_details(self):
        return f"Электроника: {self.name}, Бренд: {self.brand}, Цена: {self.price} руб, Гарантия: {self.warranty_period} лет"

class Clothing(Product):
    """
    Класс, представляющий одежду, наследующий класс Product.
    """
    def __init__(self, name, price, size, material):
        super().__init__(name, price)
        self.size = size
        self.material = material

    def get_details(self):
        return f"Одежда: {self.name}, Размер: {self.size}, Материал: {self.material}, Цена: {self.price} руб"

class HouseholdChemicals(Product):
    """
    Класс, представляющий бытовую химию, наследующий класс Product.
    """
    def __init__(self, name, price, brand, usage):
        super().__init__(name, price)
        self.brand = brand
        self.usage = usage

    def get_details(self):
        return f"Бытовая химия: {self.name}, Бренд: {self.brand}, Использование: {self.usage}, Цена: {self.price} руб"

# 2. Базовый класс User и производные классы для различных типов пользователей

class User:
    """
    Базовый класс, представляющий пользователя.
    """
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def get_details(self):
        return f"Пользователь: {self.username}, Email: {self.email}"

class Customer(User):
    """
    Класс, представляющий клиента, наследующий класс User.
    """
    def __init__(self, username, email, address):
        super().__init__(username, email)
        self.address = address

    def get_details(self):
        return f"Клиент: {self.username}, Email: {self.email}, Address: {self.address}"

class Admin(User):
    """
    Класс, представляющий администратора, наследующий класс User.
    """
    def __init__(self, username, email, admin_level):
        super().__init__(username, email)
        self.admin_level = admin_level

    def get_details(self):
        return f"Admin: {self.username}, Email: {self.email}, Admin Level: {self.admin_level}"

# 3. Класс для управления корзиной покупок

class ShoppingCart:
    """
    Класс, представляющий корзину покупок.
    """
    def __init__(self, customer, admin):
        self.items = []
        self.customer = customer
        self.admin = admin

    def add_item(self, product, quantity):
        """
        Добавляет продукт в корзину.
        """
        self.items.append({"product": product, "quantity": quantity})

    def remove_item(self, product_name):
        """
        Удаляет продукт из корзины по имени.
        """
        self.items = [item for item in self.items if item["product"].name != product_name]

    def get_total(self):
        """
        Возвращает общую стоимость продуктов в корзине.
        """
        total = sum(item["product"].price * item["quantity"] for item in self.items)
        return total

    def get_details(self):
        """
        Возвращает детализированную информацию о содержимом корзины и общей стоимости.
        """
        details = f"Клиент {self.customer.username} приобрел следующие предметы:\n"
        for item in self.items:
            details += f"{item['product'].get_details()}, Количество: {item['quantity']}\n"
        total = self.get_total()
        details += f"Общая стоимость: {total} руб\n"
        details += f"Покупку зарегистрировал сотрудник: {self.admin.username}"
        return details

# 4. Пример использования

# Создаем продукты
laptop = Electronics(name="Ноутбук", price=180000, brand="Dell", warranty_period=2)
tshirt = Clothing(name="Носки", price=50, size="M", material="Хлопок")
detergent = HouseholdChemicals(name="Доместос", price=750, brand="CleanMaster", usage="Уборка")

# Создаем пользователей
customer = Customer(username="Татьяна", email="tatyana@example.com", address="123 burr rus")
admin = Admin(username="Mikhail", email="root@example.com", admin_level=5)

# Создаем корзину покупок и добавляем товары
cart = ShoppingCart(customer, admin)
cart.add_item(laptop, 1)
cart.add_item(tshirt, 3)
cart.add_item(detergent, 2)

# Выводим детали корзины
print(cart.get_details())
