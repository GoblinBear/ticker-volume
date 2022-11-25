import heapq


class TickerDict:
    def __init__(self):
        self.tickers = {}

    # Time complexity: O(1)
    def execute_trade(self, ticker, volume):
        if ticker in self.tickers:
            self.tickers[ticker] = self.tickers[ticker] + volume
        else:
            self.tickers[ticker] = volume

    # Time complexity: O(n*logn)
    def print_top_stocks(self, top_n):
        heap = []
        # O(n)
        for i, (ticket, volume) in enumerate(self.tickers.items()):
            if i < top_n:
                # O(logn)
                heapq.heappush(heap, (volume, ticket))
            else:
                if volume > heap[0][0]:
                    # O(logn)
                    heapq.heappop(heap)
                    # O(logn)
                    heapq.heappush(heap,  (volume, ticket))

        top_n_list = []
        while heap:
            top_n_list.insert(0, heapq.heappop(heap))

        for t in top_n_list:
            print(f'{t[1]}|{t[0]}')

        return top_n_list


def main():
    ticker = TickerDict()
    ticker.execute_trade('A', 5)
    ticker.execute_trade('B', 4)
    ticker.execute_trade('C', 9)
    ticker.execute_trade('B', 3)
    ticker.execute_trade('D', 10)
    ticker.execute_trade('E', 2)
    ticker.execute_trade('F', 8)

    ticker.print_top_stocks(3)


if __name__ == '__main__':
    main()
