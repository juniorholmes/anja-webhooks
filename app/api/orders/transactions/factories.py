import json
from app.models.orders.transaction import Transaction

def parseHotmartRequest(request):

            platform = 'hotmart'
            currency = request.json['currency']
            transactionCode = request.json['transaction']
            paymentType = request.json['payment_type']
            status = request.json['status']
            customerName = request.json['first_name'] + ' ' + request.json['last_name']
            phoneLocalCode = request.json['phone_checkout_local_code']
            phoneCheckoutNumber = request.json['phone_checkout_number']
            orderBump = request.json['order_bump']
            customerEmail = request.json['email']
            productName = request.json['prod_name']
            productPrice = request.json['price']
            sck = request.json['sck']

            customerPhone = phoneLocalCode + ' ' + phoneCheckoutNumber

            return Transaction(transactionCode, currency, platform, paymentType, status, customerName,
                           customerEmail, customerPhone, productName, productPrice, orderBump, sck)



def createTransactionObject(origin, request):

    if origin == 'hotmart':

        return parseHotmartRequest(request)

