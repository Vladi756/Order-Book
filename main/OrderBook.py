from collections import defaultdict


class OrderBook:
    """
      A class used to represent a Central Limit Order Book (CLOB).

      Attributes
      ----------
      buy_orders : list
        stores outstanding buy orders
      sell_orders : list
        stores outstanding sell orders
      matches: dict
        stores matched orders
      """

    def __init__(self):
        self.buy_orders = []
        self.sell_orders = []
        self.matches = defaultdict(list)

    def add_order(self, order):
        """
        Checks if the incoming order matches an existing one and updates the quantity of the matched orders accordingly.
        Any unmatched orders are then appended to their corresponding list in the OrderBook.
        :param order: the incoming order
        :return: void
        """
        if order.is_buy():
            self.match_order(order, self.sell_orders, lambda a, b, x, y: a == b and x == y)
            if order.quantity > 0:
                self.buy_orders.append(order)
            self.buy_orders.sort(key=lambda o: o.price, reverse=True)  # sort the highest buy prices first
        else:
            self.match_order(order, self.buy_orders, lambda a, b, x, y: a == b and x == y)
            if order.quantity > 0:
                self.sell_orders.append(order)
            self.sell_orders.sort(key=lambda o: o.price)

    def match_order(self, order, opposite_orders, match_condition):
        """
        Check if a given order matches with an order with a corresponding direction based on a specified match condition.
        :param order: The incoming order for which a match is to be determined.
        :param opposite_orders:  The list of all orders with an opposite direction to the input order. This represents all the potential matches the incoming order may have.
        :param match_condition: The condition which any order must satisfy in order to be matched with the incoming order.
        :return: void
        """
        i = 0
        while i < len(opposite_orders) and order.quantity > 0:
            opposite_order = opposite_orders[i]
            if match_condition(order.contract, opposite_order.contract, order.price, opposite_order.price):
                match_quantity = min(order.quantity, opposite_order.quantity)
                (self.matches[order.contract].append(
                    f"Match: {opposite_order.side} {opposite_order.quantity}@{order.price} with {order.side} {order.quantity}@{order.price} on {order.contract}"))
                order.quantity -= match_quantity
                opposite_order.quantity -= match_quantity
                if opposite_order.quantity == 0:
                    opposite_orders.pop(i)  # reduces the length of the list and shifts subsequent elements left - no need to increment i
                else:
                    i += 1
            else:
                i += 1

    def display(self):
        """
        Displays the current state of the order book.
        :return: str
        """
        buy_orders_by_contract = defaultdict(list)
        sell_orders_by_contract = defaultdict(list)
        for order in self.buy_orders:
            buy_orders_by_contract[order.contract].append(order)
        for order in self.sell_orders:
            sell_orders_by_contract[order.contract].append(order)

        all_contracts = set(buy_orders_by_contract.keys()).union(set(sell_orders_by_contract.keys())).union(set(self.matches.keys()))

        for contract in sorted(all_contracts):
            for match in self.matches[contract]:
                print(f'\n{match}')
            print(f"\n{contract}: ")
            if buy_orders_by_contract[contract]:
                for order in buy_orders_by_contract[contract]:
                    if order.quantity == 0:
                        break
                    print("BUY ORDERS:")
                    print(f'{order}')
            if sell_orders_by_contract[contract]:
                for order in sell_orders_by_contract[contract]:
                    if order.quantity == 0:
                        break
                    print("SELL ORDERS:")
                    print(order)
            elif not sell_orders_by_contract[contract] and not buy_orders_by_contract[contract]:
                print("No open orders.")
