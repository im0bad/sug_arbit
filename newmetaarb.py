import ccxt

def find_arbitrage():
    # Get all available exchanges
    exchanges = ccxt.exchanges 

    currencies = ["BTC", "ETH", "XRP"]

    for exch1 in exchanges:
        # Initialize exchange 1 
        if exch1 in ['ace' , 'alpaca']:
            continue
        exchange1 = getattr(ccxt, exch1)()

        for exch2 in exchanges:
            if exch2 in ['ace' , 'alpaca']:
                continue
            # Only check arbitrage between different exchanges 
            if exch1 != exch2:
                # Initialize exchange 2
                exchange2 = getattr(ccxt, exch2)()  
                # Get prices of all currency pairs for the two exchanges
                prices1 = {}
                prices2 = {}
                for cur1 in currencies:
                    for cur2 in currencies:
                        try:
                            pair = cur1 + "/" + cur2
                            prices1[pair] = exchange1.fetch_order_book(pair)["bids"][0][0]
                            # print(prices1)  
                            prices2[pair] = exchange2.fetch_order_book(pair)["asks"][0][0]
                            # print(prices2)
                        except:
                            continue  
                
                # Check for arbitrage opportunities       
                for pair in prices1:
                    try:    
                        price1 = prices1[pair]
                        price2 = prices2[pair]
                        if price2 < price1:
                            profit_percentage = (price1 - price2) / price2 * 100
                            print(f"Arbitrage opportunity between {exch1} and {exch2}! \
                                Buy {pair} on {exch2} and sell on {exch1} for {profit_percentage:.2f}% profit")
                    except : 
                        continue

if __name__ == "__main__": 
    find_arbitrage()