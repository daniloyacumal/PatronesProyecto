from models.order import Order

class OrderFactory:

    @staticmethod
    def create_order(order_type, description, base_amount):
        return Order(description, base_amount)
