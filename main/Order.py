class Order:
    """
      Represents an order in a financial trading system.

      Attributes
      ----------
      side: str
        The side of the order, either 'BUY' or 'SELL'.
      price: float
        The price at which the order is placed.
      quantity: int
        The quantity of the asset to be bought or sold.
      contract: str
        The contract associated with the order, such as a futures contract identifier.
    """

    def __init__(self, side, price, quantity, contract):
        if side not in ["BUY", "SELL"]:
            raise ValueError("side must be either 'BUY' or 'SELL'")
        self.side = side
        self.price = price
        self.quantity = quantity
        self.contract = contract

    def __repr__(self):
        return f'Price: {self.price}, Quantity: {self.quantity}, Contract: {self.contract}'

    def is_buy(self):
        """
        Checks if the order is a buy order.

        :return: True if the order is a buy order, False otherwise.
        """
        return self.side == "BUY"

    def is_sell(self):
        """
        Checks if the order is a sell order.

        :return: True if the order is a sell order, False otherwise.
        """
        return self.side == "SELL"
