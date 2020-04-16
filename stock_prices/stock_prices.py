#!/usr/bin/python

import argparse


def find_max_profit(prices):
  for i in range(len(prices)):
    current_index = i 
    buy_price = current_index 
    sell_price = current_index
    profit = None
    for x in range(buy_price, len(prices) - 1):
      if prices[buy_price] > prices[x]:
        buy_price = x
        sell_price = x 
      elif prices[sell_price] < prices[x]:
        sell_price = x 
      
    if buy_price == sell_price:
      sell_price = sell_price + 1      
    profit = prices[sell_price] - prices[buy_price]
    return profit
   

    



print(find_max_profit([1050, 270, 1540, 3800, 2]))
if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))