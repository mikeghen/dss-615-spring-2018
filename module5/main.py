# ## Lab 1: Reading a CSV file
# filename = './data/inpatient_payments_data.csv'
# is_header = True
#
# with open(filename, 'r') as inpatient_payments_data:
#     for datum in inpatient_payments_data:
#         values = datum.split(',')
#
#         if is_header:
#             header = [values[2], values[-4], values[-3], values[-2], values[-1]]
#             is_header = False
#         else:
#             provider_name = values[2]
#             total_discharges = values[-4].replace('$','')
#             avg_covered_charges = values[-3].replace('$','')
#             average_total_payments = values[-2].replace('$','')
#             avg_medicare_payment = values[-1].replace('$','')
#
# #             print(','.join([provider_name, total_discharges, avg_covered_charges, average_total_payments, avg_medicare_payment]))
# #
# # #
# # ## Lab 2: Working with Dictionaries
# from pprint import pprint
#
# bitcoin_data = {
#                  "ticker": {
#                     "base":"BTC",
#                     "target":"USD",
#                     "markets": [ { "market":"BitFinex",
#                                    "price":"7764.00000000",
#                                    "volume":195270.39909915
#                                  },
#                                  { "market":"Bitstamp",
#                                    "price":"7830.93000000",
#                                    "volume":70962.37875181
#                                  }
#                                 ]
#                  },
#                  "timestamp":1517960522
#                }
#
# ticker_data = bitcoin_data["ticker"]
# timestamp = bitcoin_data["timestamp"]
#
# btc_markets_records = []
# for market_record in ticker_data["markets"]:
#     record_tuple = ( timestamp,
#                      market_record["market"],
#                      market_record["price"],
#                      market_record["volume"])
#
#     btc_markets_records.append(record_tuple)
#
# print("Dictionary:")
# pprint(bitcoin_data)
# print("\nList:")
# pprint(btc_markets_records)
# #
#
## Lab 3: Using the json module
import json

filename = './data/beyonce.json'

with open(filename, 'r') as beyonce_file:
    beyonce_instagram = json.load(beyonce_file)

    print(beyonce_instagram["instagram"])

    # for key, value in beyonce_instagram.items():
    #     print(key, type(value))
    #     if type(value) == dict:
    #         for k, v in value.items():
    #             print("\t", k, type(v))
