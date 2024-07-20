from OrderBook import OrderBook
from Order import Order


def main():
    orders = [
        {"type": "BUY", "price": 1500, "quantity": 2, "contract": "GCQ4 Comdty"},
        {"type": "SELL", "price": 1500, "quantity": 2, "contract": "GCQ4 Comdty"},
        {"type": "BUY", "price": 1550, "quantity": 3, "contract": "GCZ4 Comdty"},
        {"type": "SELL", "price": 1550, "quantity": 1, "contract": "GCZ4 Comdty"}
    ]
    order_book = OrderBook()
    for order in orders:
        new_order = Order(order["type"], order["price"], order["quantity"], order.get("contract"))
        order_book.add_order(new_order)
    order_book.display()


if __name__ == "__main__":
    main()
