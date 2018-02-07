## Exchange Rate Calculator

print("Exchange Rate Calculator")

while True:

    # Input
    source_currency = input("Source Currency: ")
    target_currency = input("Target Currency: ")
    source_amount = eval(input("Starting Amount ({0}): ".format(source_currency)))
    exchange_rate = eval(input("Exchange Rate ({1}/{0}): "
                               .format(target_currency,source_currency)))
    fee = eval(input("Transfer fee (as a percentange of starting amount): "))

    # Processing
    transaction_fees = source_amount * fee / 100
    target_amount = (source_amount - transaction_fees) * exchange_rate

    # Output
    print("Exchanged {0:,.2f} {1} for {2:,.2f} {3}".format(source_amount,
                                                           source_currency,
                                                           target_amount,
                                                           target_currency))
    print("Paid {0:,.2f} {1} in fees.".format(transaction_fees,
                                              source_currency))
