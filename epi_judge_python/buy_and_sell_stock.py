from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    min = float('inf')
    profit = 0.0
    for price in prices:
        if price < min:
            # print(f"current price ({price}) less than min ({min})")
            min = price

        current_profit = round(price - min,1)
        # print(f"current_profit: {max} - {min} = {current_profit}")
        if current_profit > profit:
            # print(f"update profit because {current_profit} > {profit}")
            profit = current_profit


            
    return profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
