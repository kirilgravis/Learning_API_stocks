from alpaca.data import CryptoDataStream

keys = [x.strip() for x in open('keys.txt', 'r').readlines()]

# keys are required for live data
crypto_stream = CryptoDataStream(keys[0], keys[1])


# async handler
async def quote_data_handler(data: any):
    # quote data will arrive here
    print(data)

crypto_stream.subscribe_quotes(quote_data_handler, "BTC/USD")

crypto_stream.run()
