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
    product_code: str
        The product code extracted from the contract.
    month_code: str
        The month code extracted from the contract.
    market: str
        The market associated with the order, extracted from the contract.
    month_codes: dict
        A dictionary mapping single-letter month codes to their full month names.
    """

    month_codes = {'F': 'January', 'G': 'February', 'H': 'March', 'J': 'April', 'K': 'May', 'M': 'June',
                   'N': 'July', 'Q': 'August', 'U': 'September', 'V': 'October', 'X': 'November', 'Z': 'December'}

    def __init__(self, side, price, quantity, contract):
        self.side = side
        self.price = price
        self.quantity = quantity
        self.contract = contract
        self.product_code = contract[:2]
        self.month_code = contract[2:3]
        self.market = contract[5:]
        self.sanitize_input()

    def __repr__(self):
        return f'Price: {self.price}, Quantity: {self.quantity}, Contract: {self.contract}'

    def sanitize_input(self):
        """
        Validates the attributes of an order instance to ensure they meet the required criteria.

        Raises:
            InvalidOrderException: If any attribute does not meet the criteria.
        :return:
        """
        if self.side not in ["BUY", "SELL"]:
            raise ValueError(f"{self.side} does not conform to acceptable values 'BUY' or 'SELL'.")
        if self.price <= 0 or self.quantity <= 0:
            raise ValueError("Price and quantity must be positive.")
        if self.month_code not in self.month_codes:
            raise ValueError(f"Contract code {self.month_codes} does not conform to valid set of month codes: {', '.join(self.month_codes.keys())}")
        if self.product_code != "GC":
            raise ValueError(f"Unsupported product code [{self.product_code}]. Product must be Gold [GC].")
        if self.market != "Comdty":
            raise ValueError(f"Unsupported market [{self.market}]. Order must be for commodity [Comdty] market.")

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
