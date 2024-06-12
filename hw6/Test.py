def amount_payment(payments):
    total_payment = 0
    for payment in payments:
        if payment > 0:
            total_payment += payment
    return total_payment

payments = [1500, -2050, 2200, -1930, 250]
print(amount_payment(payments))