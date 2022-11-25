import unittest

from ticker_dict import TickerDict


class TestBST(unittest.TestCase):
    def test_execute_trade(self):
        ticker = TickerDict()
        ticker.execute_trade('A', 5)
        ticker.execute_trade('B', 4)
        ticker.execute_trade('C', 9)
        ticker.execute_trade('B', 3)
        ticker.execute_trade('D', 10)
        ticker.execute_trade('E', 2)
        ticker.execute_trade('F', 8)

        self.assertEqual(ticker.tickers,
                         { 'A': 5, 'B': 7, 'C': 9, 'D': 10, 'E': 2, 'F': 8 })
    
    def test_print_top_stocks(self):
        ticker = TickerDict()
        ticker.execute_trade('A', 5)
        ticker.execute_trade('B', 4)
        ticker.execute_trade('C', 9)
        ticker.execute_trade('B', 3)
        ticker.execute_trade('D', 10)
        ticker.execute_trade('E', 2)
        ticker.execute_trade('F', 8)

        self.assertEqual(ticker.print_top_stocks(3), [ (10, 'D'),
                                                       (9, 'C'),
                                                       (8, 'F')])
        
        self.assertEqual(ticker.print_top_stocks(5), [ (10, 'D'),
                                                       (9, 'C'),
                                                       (8, 'F'),
                                                       (7, 'B'),
                                                       (5, 'A')])
