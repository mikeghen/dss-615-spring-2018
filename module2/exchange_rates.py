from pprint import pprint

exchange_rates = [ ('BitFinex', 180.92000000, 12309, 0.25),
                   ('Bittrex', 182.97999999, 4343, 0.1),
                   ('C-Cex', 197.49000000, 5, 1.50),
                   ('Exmo', 191.52000000, 342, 0.25),
                   ('Hitbtc', 181.01500000, 2345, 0.10),
                   ('Kraken', 179.23000000, 3442, 0.50),
                   ('Livecoin', 190.00000000, 234, 0.25) ]

investment = float(input("Enter the amount to arbitrage: "))

# Find the expected return going from a -> b exchange
results = []
for a in range(len(exchange_rates)):
    for b in range(len(exchange_rates)):
        starting_balance = (investment - (investment * exchange_rates[a][3] / 100)) / exchange_rates[a][1]
        ending_balance = (starting_balance - (starting_balance * exchange_rates[b][3] / 100)) * exchange_rates[b][1]
        results.append( (exchange_rates[a][0],exchange_rates[b][0],ending_balance) )

sorted_results = sorted(results, key=lambda result: result[2])
pprint(sorted_results)


#
# bitrex = (investment - (investment * exchange_rates[1][3] / 100 )) / exchange_rates[1][1]
# ccex = (investment - (investment * exchange_rates[2][3] / 100)) / exchange_rates[2][1]
# exmo = (investment - (investment * exchange_rates[3][3] / 100)) / exchange_rates[3][1]
# hitbtc = (investment - (investment * exchange_rates[4][3] / 100)) / exchange_rates[4][1]
# kraken = (investment - (investment * exchange_rates[5][3] / 100)) / exchange_rates[5][1]
# livecoin = (investment - (investment * exchange_rates[6][3] / 100)) / exchange_rates[6][1]
#
# starting_balances = [bitfinex, bitrex, ccex, exmo, hitbtc, kraken, livecoin]
#
# pprint(starting_balances)
#
#
# bitfinex_bitrex = (bitfinex - (bitfinex * exchange_rates[1][3] / 100)) * exchange_rates[1][1]
# bitfinex_ccex = (bitfinex - (bitfinex * exchange_rates[2][3] / 100)) * exchange_rates[2][1]
# bitfinex_exmo = (bitfinex - (bitfinex * exchange_rates[3][3] / 100)) * exchange_rates[3][1]
# bitfinex_hitbtc = (bitfinex - (bitfinex * exchange_rates[4][3] / 100)) * exchange_rates[4][1]
# bitfinex_kraken = (bitfinex - (bitfinex * exchange_rates[5][3] / 100)) * exchange_rates[5][1]
# bitfinex_livecoin = (bitfinex - (bitfinex * exchange_rates[6][3] / 100)) * exchange_rates[6][1]
#
# ending_balances = [('bitrex',bitfinex_bitrex),
#                      ('ccex', bitfinex_ccex),
#                      ('exmo', bitfinex_exmo),
#                      ('hitbtc', bitfinex_hitbtc),
#                      ('kraken',bitfinex_kraken),
#                      ('livecoin', bitfinex_livecoin)]
#
# bitrex_bitfinix = (bitrex - (bitrex * exchange_rates[0][3] / 100)) * exchange_rates[0][1]
# bitrex_ccex = (bitrex - (bitrex * exchange_rates[2][3] / 100)) * exchange_rates[2][1]
# bitrex_exmo = (bitrex - (bitrex * exchange_rates[3][3] / 100)) * exchange_rates[3][1]
# bitrex_hitbtc = (bitrex - (bitrex * exchange_rates[4][3] / 100)) * exchange_rates[4][1]
# bitrex_kraken = (bitrex - (bitrex * exchange_rates[5][3] / 100)) * exchange_rates[5][1]
# bitrex_livecoin = (bitrex - (bitrex * exchange_rates[6][3] / 100)) * exchange_rates[6][1]
#
# ending_balances = [('bitrex_bitfinix',bitrex_bitfinix),
#                      ('ccex', bitrex_ccex),
#                      ('exmo', bitrex_exmo),
#                      ('hitbtc', bitrex_hitbtc),
#                      ('kraken',bitrex_kraken),
#                      ('livecoin', bitrex_livecoin)]
#
# pprint(ending_balances)
# Move from one exchange to another (A->B)
# Convert back to USD

















# # NOTE: Getting real time
# import urllib.request
# import json
#
# url = 'https://api.cryptonator.com/api/full/btc-usd'
# response = urllib.request.urlopen(url)
# extracted_data = json.load(response)
#
# ticker_data  = extracted_data["ticker"]
#
# ltc_markets_rates = []
# for market_record in ticker_data["markets"]:
#     record_tuple = (market_record["market"], market_record["price"], market_record["volume"])
#     ltc_markets_rates.append(record_tuple)
#
# print(ltc_markets_rates)
