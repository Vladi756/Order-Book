import unittest
from main.Order import Order


class TestOrder(unittest.TestCase):
    """
    Test cases for the Order class.
    """

    def test_order_initialization(self):
        """
        Test that an Order is correctly initialized with given attributes.
        """
        order = Order("BUY", 102.5, 10, "GCQ4 Comdty")
        self.assertEqual(order.side, "BUY")
        self.assertEqual(order.price, 102.5)
        self.assertEqual(order.quantity, 10)
        self.assertEqual(order.contract, "GCQ4 Comdty")

    def test_is_buy(self):
        """
        Test that is_buy method correctly identifies buy orders.
        """
        buy_order = Order("BUY", 102.5, 10, "GCQ4 Comdty")
        sell_order = Order("SELL", 102.5, 10, "GCQ4 Comdty")
        self.assertTrue(buy_order.is_buy())
        self.assertFalse(sell_order.is_buy())

    def test_is_sell(self):
        """
        Test that is_sell method correctly identifies sell orders.
        """
        buy_order = Order("BUY", 102.5, 10, "GCQ4 Comdty")
        sell_order = Order("SELL", 102.5, 10, "GCQ4 Comdty")
        self.assertFalse(buy_order.is_sell())
        self.assertTrue(sell_order.is_sell())

    def test_invalid_side(self):
        """
        Test that initializing an Order with an invalid side raises a ValueError.
        """
        with self.assertRaises(ValueError):
            Order("HOLD", 102.5, 10, "GCQ4 Comdty")


if __name__ == "__main__":
    unittest.main()
