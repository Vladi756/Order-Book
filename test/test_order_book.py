import contextlib
import textwrap
import unittest
from io import StringIO

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

    def test_display_order_book_with_no_matches(self):
        """
        Test that the display method correctly shows the state of the order book
        when there are no matches, displaying outstanding buy and sell orders.
        """
        buy_order = Order("BUY", 101.0, 10, "GCQ4 Comdty")
        sell_order = Order("SELL", 102.0, 10, "GCQ4 Comdty")
        self.order_book.add_order(buy_order)
        self.order_book.add_order(sell_order)

        # Capture the output of the display method
        captured_output = StringIO()
        with contextlib.redirect_stdout(captured_output):
            self.order_book.display()

        # Verify the captured output
        output = captured_output.getvalue().strip()
        expected_output = textwrap.dedent("""
        GCQ4 Comdty: 
        BUY ORDERS:
        Price: 101.0, Quantity: 10, Contract: GCQ4 Comdty
        SELL ORDERS:
        Price: 102.0, Quantity: 10, Contract: GCQ4 Comdty
        """).strip()
        self.assertEqual(output, expected_output)

    def test_display_order_book(self):
        """
        Test that the display method correctly shows the state of the order book.
        """
        buy_order = Order("BUY", 101.0, 10, "GCQ4 Comdty")
        sell_order = Order("SELL", 101.0, 10, "GCQ4 Comdty")
        self.order_book.add_order(buy_order)
        self.order_book.add_order(sell_order)

        # Capture the output of the display method
        captured_output = StringIO()
        with contextlib.redirect_stdout(captured_output):
            self.order_book.display()

        # Verify the captured output
        output = captured_output.getvalue().strip()
        expected_output = textwrap.dedent("""
        Match: BUY 10@101.0 with SELL 10@101.0 on GCQ4 Comdty
        
        GCQ4 Comdty: 
        No open orders.
         """).strip()
        self.assertEqual(output, expected_output)
