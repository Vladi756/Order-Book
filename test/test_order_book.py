import unittest
from main.Order import Order
from main.OrderBook import OrderBook


class TestOrderBook(unittest.TestCase):
    """
    Unit tests for the OrderBook class.
    """

    def setUp(self):
        """
        Sets up a new OrderBook instance before each test.
        """
        self.order_book = OrderBook()

    def test_add_buy_order(self):
        """
        Test that a buy order is correctly added to the buy_orders list.
        """
        order = Order("BUY", 102.5, 10, "GCQ4 Comdty")
        self.order_book.add_order(order)
        self.assertEqual(len(self.order_book.buy_orders), 1)
        self.assertEqual(len(self.order_book.sell_orders), 0)
        self.assertEqual(self.order_book.buy_orders[0].price, 102.5)

    def test_add_sell_order(self):
        """
        Test that a sell order is correctly added to the sell_orders list.
        """
        order = Order("SELL", 101.5, 5, "GCQ4 Comdty")
        self.order_book.add_order(order)
        self.assertEqual(len(self.order_book.sell_orders), 1)
        self.assertEqual(len(self.order_book.buy_orders), 0)
        self.assertEqual(self.order_book.sell_orders[0].price, 101.5)

    def test_match_order(self):
        """
        Test that matching orders are correctly matched and quantities are updated.
        """
        buy_order = Order("BUY", 100.0, 10, "GCQ4 Comdty")
        sell_order = Order("SELL", 100.0, 5, "GCQ4 Comdty")
        self.order_book.add_order(buy_order)
        self.order_book.add_order(sell_order)
        self.assertEqual(len(self.order_book.buy_orders), 1)
        self.assertEqual(len(self.order_book.sell_orders), 0)
        self.assertEqual(self.order_book.buy_orders[0].quantity, 5)
        self.assertEqual(self.order_book.matches["GCQ4 Comdty"][0],
                         "Match: BUY 10@100.0 with SELL 5@100.0 on GCQ4 Comdty")

    def test_display_order_book(self):
        """
        Test that the display method correctly shows the state of the order book.
        """
        buy_order = Order("BUY", 101.0, 10, "GCQ4 Comdty")
        sell_order = Order("SELL", 101.0, 10, "GCQ4 Comdty")
        self.order_book.add_order(buy_order)
        self.order_book.add_order(sell_order)
        self.assertIn("GCQ4 Comdty", self.order_book.matches)
        self.assertEqual(len(self.order_book.matches["GCQ4 Comdty"]), 1)
        self.assertEqual(
            self.order_book.matches["GCQ4 Comdty"][0],
            "Match: BUY 10@101.0 with SELL 10@101.0 on GCQ4 Comdty"
        )
        self.assertEqual(len(self.order_book.buy_orders), 0)
        self.assertEqual(len(self.order_book.sell_orders), 0)
