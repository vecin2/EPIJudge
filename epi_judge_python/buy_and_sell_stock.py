from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    lowest, diff = 10000000000000000000000.0, 0.0

    for item in prices:
        if item < lowest:
            lowest = item
        elif item - lowest > diff:
            diff = item - lowest

    return diff


if __name__ == "__main__":
    exit(
        generic_test.generic_test_main(
            "buy_and_sell_stock.py", "buy_and_sell_stock.tsv", buy_and_sell_stock_once
        )
    )
