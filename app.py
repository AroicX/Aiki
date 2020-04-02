good_credit=input('good_credit: ')

price = 1000000
if good_credit:
    print("price of the house is 1 million dollars")
    down_payment=0.1*price
else:
    print('they need to put down 20%')
    down_payment=0.2*price
print(f"Down payment: ${down_payment}")