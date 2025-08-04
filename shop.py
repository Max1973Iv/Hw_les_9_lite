from classes.products import Electronics, Clothing, HouseHoldChemicals
from classes.users import Customer, Admin
from classes.shoping_carts import ShoppingCart
import sys
sys.stdout.reconfigure(encoding='utf-8')  # Настройка кодировки вывода для корректного отображения русских символов
# Создаем товары
laptop = Electronics(name="Ноутбук", price=1200, brand="Dell", warranty_period=2)
tshirt = Clothing(name="Футболка", price=200, size="M", material="Хлопок")
shampoo = HouseHoldChemicals(name="Шампунь", price=15, volume=500)
#
# Создаем пользователей
customer = Customer(username="Максим", email="mmm@blgroup.by", address="Минск, ул. Ленина, 1")
admin = Admin(username="админ_1", email="root@v.ru", admin_level=5)
#
# Создаем корзину покупок
cart = ShoppingCart()
# привязываем покупателя и сотрудника к корзине
cart.buyer = customer
cart.employee = admin
# Добавляем продукты в корзину
cart.add_item(laptop, 1)
cart.add_item(shampoo, 1)
# Выводим детали корзины
print(cart.get_details())
# время и дата создания корзины
print(f"Дата и время создания корзины: {cart.creation_time()}")