# Ticker Volume

## Run

```shell
$ python3 ticker_dict.py
```

Features:
- `execute_trade()`
- `print_top_stocks()`

```python
ticker = TickerDict()
ticker.execute_trade('A', 5)
ticker.execute_trade('B', 4)
ticker.execute_trade('C', 9)
ticker.execute_trade('B', 3)
ticker.execute_trade('D', 10)
ticker.execute_trade('E', 2)
ticker.execute_trade('F', 8)

ticker.print_top_stocks(3)
```
```
D|10
C|9
F|8
```

### Run Tests

```shell
$ python3 -m unittest -v tests/test_ticker_dict.py
```

## File Structure

```
📦ticker-volume
 ┣ 📂tests
 ┃ ┗ 📜test_ticker_dict.py
 ┗ 📜ticker_dict.py
```
- `ticker_dict.py`: The data structure of ticker.
