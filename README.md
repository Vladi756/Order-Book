# Central Limit Order Book (CLOB) Project

This project implements a simplified Central Limit Order Book (CLOB) in Python. The order book handles buy and sell orders for financial instruments, matches orders based on price, and maintains the state of outstanding orders and matched orders.

## Table of Contents
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)
    - [Creating Orders](#creating-orders)
    - [Adding Orders to the Order Book](#adding-orders-to-the-order-book)
    - [Displaying the Order Book](#displaying-the-order-book)
    - [Examples of Matched Orders](#examples-of-matched-orders)

## Features

- Handles buy and sell orders.
- Matches orders based on price and updates quantities accordingly.
- Displays the state of the order book, including matched and outstanding orders.
- Supports contracts for financial instruments (e.g. futures contracts).

## Getting Started

### Prerequisites

Ensure you have Python 3.x installed on your system.

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/order-book.git
    cd order-book
    ```

2. Install dependencies (if any). For this project, no external dependencies are required.

## Usage

### Creating Orders

Create `Order` instances to represent buy and sell orders. Each order must have a side ("BUY" or "SELL"), a price, a quantity, and a contract identifier.

```python
from main.Order import Order

# Example orders
buy_order = Order("BUY", 102.5, 10, "GCQ4 Comdty")
sell_order = Order("SELL", 101.5, 5, "GCQ4 Comdty")
```

### Adding Orders to the Order Book
Create an OrderBook instance and add orders to it. The order book will automatically match orders based on price and update quantities accordingly.

````python
from main.OrderBook import OrderBook

# Create an OrderBook instance
order_book = OrderBook()

# Add orders to the order book
order_book.add_order(buy_order)
order_book.add_order(sell_order)

````

### Displaying the Order Book
The display method prints the state of the order book, showing matched orders and outstanding buy and sell orders.

````python
# Display the current state of the order book
order_book.display()

````
The result of the above looks like this: 
````commandline
GCZ4 Comdty: 
BUY ORDERS:
Price: 102.5, Quantity: 10, Contract: GCZ4 Comdty
SELL ORDERS:
Price: 101.5, Quantity: 5, Contract: GCZ4 Comdty
````

### Examples of Matched Orders

When orders are added that can be matched, the order book updates to reflect these matches. Here is an example: 

````python
from main.Order import Order
from main.OrderBook import OrderBook

# Create an OrderBook instance
order_book = OrderBook()

# Add matching orders
buy_order1 = Order("BUY", 100.0, 10, "GCQ4 Comdty")
sell_order1 = Order("SELL", 100.0, 5, "GCQ4 Comdty")
order_book.add_order(buy_order1)
order_book.add_order(sell_order1)

# Add more matching orders
buy_order2 = Order("BUY", 101.0, 10, "GCQ4 Comdty")
sell_order2 = Order("SELL", 101.0, 10, "GCQ4 Comdty")
order_book.add_order(buy_order2)
order_book.add_order(sell_order2)

# Display the current state of the order book
order_book.display()
````
The result of the above display: 

````python
Match: BUY 10@100.0 with SELL 5@100.0 on GCQ4 Comdty

GCQ4 Comdty:
BUY ORDERS:
Price: 100.0, Quantity: 5, Contract: GCQ4 Comdty

Match: BUY 10@101.0 with SELL 10@101.0 on GCQ4 Comdty

GCQ4 Comdty:
No open orders.
````
In this example:

- The first match shows that 10 units from the buy order are partially matched with 5 units from the sell order at a price of 100.0.
- The second match shows that 10 units from the buy order are fully matched with 10 units from the sell order at a price of 101.0.-
- The order book correctly updates to show the remaining quantity for partially matched orders and indicates when there are no open orders.

