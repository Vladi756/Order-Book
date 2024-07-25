import unittest
from main.Order import Order


class TestOrder(unittest.TestCase):
    """
    Test cases for the Order class.
    """

    def test_order_initialization(self):
        """
        Test order initialization with valid attributes.
        """
        order = Order("BUY", 102.5, 10, "GCQ4 Comdty")
        self.assertEqual(order.side, "BUY")
        self.assertEqual(order.price, 102.5)
        self.assertEqual(order.quantity, 10)
        self.assertEqual(order.contract, "GCQ4 Comdty")
        self.assertTrue(order.month_codes.keys().__contains__("Q"))
        self.assertEqual(order.market, "Comdty")
        self.assertEqual(order.product_code, "GC")

    def test_is_buy(self):
        """
        Test is_buy method.
        """
        buy_order = Order("BUY", 102.5, 10, "GCQ4 Comdty")
        sell_order = Order("SELL", 102.5, 10, "GCQ4 Comdty")
        self.assertTrue(buy_order.is_buy())
        self.assertFalse(sell_order.is_buy())

    def test_is_sell(self):
        """
        Test is_sell method.
        """
        buy_order = Order("BUY", 102.5, 10, "GCQ4 Comdty")
        sell_order = Order("SELL", 102.5, 10, "GCQ4 Comdty")
        self.assertFalse(buy_order.is_sell())
        self.assertTrue(sell_order.is_sell())

    def test_invalid_side(self):
        """
        Test invalid side raises ValueError.
        """
        with self.assertRaises(ValueError) as context:
            Order("HOLD", 100.0, 10, "GCQ4 Comdty")
        self.assertTrue("HOLD does not conform to acceptable values 'BUY' or 'SELL'." in str(context.exception))

    def test_negative_price(self):
        """
        Test negative price raises ValueError.
        """
        with self.assertRaises(ValueError) as context:
            Order("BUY", -100.0, 10, "GCQ4 Comdty")
        self.assertTrue("Price and quantity must be positive." in str(context.exception))

    def test_negative_quantity(self):
        """
        Test negative quantity raises ValueError.
        """
        with self.assertRaises(ValueError) as context:
            Order("SELL", 100.0, -10, "GCQ4 Comdty")
        self.assertTrue("Price and quantity must be positive." in str(context.exception))

    def test_invalid_month_code(self):
        """
        Test invalid month code raises ValueError.
        """
        with self.assertRaises(ValueError) as context:
            Order("BUY", 100.0, 10, "GCA4 Comdty")
        self.assertTrue(f"Contract code A does not conform to valid set of month codes: {', '.join(Order.month_codes.keys())}")

    def test_invalid_product_code(self):
        """
        Test invalid product code raises ValueError.
        """
        with self.assertRaises(ValueError) as context:
            Order("SELL", 100.0, 10, "ZZQ4 Comdty")
        self.assertTrue("Unsupported product code [ZZ]. Product must be Gold [GC]." in str(context.exception))

    def test_invalid_market(self):
        """
        Test invalid market raises ValueError.
        """
        with self.assertRaises(ValueError) as context:
            Order("BUY", 100.0, 10, "GCQ4 Equity")
        self.assertTrue(
            "Unsupported market [Equity]. Order must be for commodity [Comdty] market." in str(context.exception))

    def test_valid_order(self):
        """
        Test valid order creation.
        """
        try:
            order = Order("BUY", 100.0, 10, "GCQ4 Comdty")
            self.assertEqual(order.side, "BUY")
            self.assertEqual(order.price, 100.0)
            self.assertEqual(order.quantity, 10)
            self.assertEqual(order.contract, "GCQ4 Comdty")
            self.assertEqual(order.product_code, "GC")
            self.assertEqual(order.month_code, "Q")
            self.assertEqual(order.market, "Comdty")
        except ValueError:
            self.fail("Valid order raised ValueError unexpectedly!")
