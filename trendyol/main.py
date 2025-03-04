import datetime
import random


class ClientProfile:
    def __init__(self, full_name: str, gender: str, age: int):
        self.full_name = full_name
        self.age = age
        self.gender = gender


class OrderStatusConfig:
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DELIVERED = "Delivered"
    CANCELLED = "Cancelled"


class Product:
    def __init__(self, title: str, price: int, created_at: datetime.datetime, expires_at: datetime.datetime, rating: float):
        self.title = title
        self.price = price
        self.rating = rating
        self.created_at = created_at
        self.expires_at = expires_at


class Order:
    def __init__(self, client_profile: ClientProfile, status: str):
        self.client_profile = client_profile
        self.cart = []
        self.status = status
        self.created_at = datetime.datetime.now()
        self.status_history = [(self.created_at, status)]

    def add_to_cart(self, prod: Product):
        self.cart.append(prod)

    def calculate_total_cost(self):
        return sum(product.price for product in self.cart)

    def _change_status(self, status: str):
        if status in OrderStatusConfig.__dict__.values():
            self.status = status
            self.status_history.append((datetime.datetime.now(), status))

    def approve(self):
        self._change_status(OrderStatusConfig.APPROVED)

    def reject(self):
        self._change_status(OrderStatusConfig.REJECTED)

    def pend(self):
        self._change_status(OrderStatusConfig.PENDING)

    def deliver(self):
        self._change_status(OrderStatusConfig.DELIVERED)

    def cancel(self):
        self._change_status(OrderStatusConfig.CANCELLED)


class WishList:
    def __init__(self):
        self.product_list = []

    def add_product(self, product: Product):
        self.product_list.append(product)

    def is_product_available(self, product_name: str):
        return any(p.title == product_name for p in self.product_list)


product1 = Product("Jersey", 
                   15, 
                   datetime.datetime.now(), 
                   datetime.datetime.now() + datetime.timedelta(days=30), 
                   random.uniform(0, 5)
                )

client1 = ClientProfile("Yusif Teymurlu", "Male", 17)

wishing_product_name = input("Enter your product name >> ").title()

wish_list = WishList()
wish_list.add_product(product1)


if wish_list.is_product_available(wishing_product_name):
    order = Order(client1, OrderStatusConfig.PENDING)
    order.add_to_cart(product1)
    print(f"Order created for {client1.full_name}. Total cost: ${order.calculate_total_cost()}")
else:
    print("Requested product is not available in the wish list.")