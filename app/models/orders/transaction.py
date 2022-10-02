class Transaction:
    def __init__(self, transactionCode, currency, platform, paymentType, status, customerName, customerEmail, customerPhone, productName, offerPrice, orderBump, sck):
        self.code = transactionCode
        self.currency = currency
        self.platform = platform
        self.paymentType = paymentType
        self.status = status
        self.customer = {
            'name': customerName,
            'email': customerEmail,
            'mobile_phone': customerPhone
        }

        self.product = {
            'name': productName
        }

        self.offer = {
            'price': offerPrice,
            'full_price': offerPrice
        }

        self.track = {
            'sck': sck
        }

        self.orderbump = orderBump