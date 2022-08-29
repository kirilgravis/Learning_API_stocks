from alpaca.data import StockDataStream

keys = [x.strip() for x in open('keys.txt', 'r').readlines()]

# keys required
stock_stream = StockDataStream(keys[0], keys[1])


# async handler
async def quote_data_handler(data: any):
    # quote data will arrive here
    print(data)


stock_stream.subscribe_quotes(quote_data_handler, "SPY")

stock_stream.run()
