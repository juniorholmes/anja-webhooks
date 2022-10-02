from app.models.orders.transaction import Transaction

def parseHotmartRequest(request):
            platform = 'hotmart'
            currency = response.json['currency']
            transactionCode = response.json['transaction']
            paymentType = response.json['payment_type']
            status = response.json['status']
            customerName = response.json['first_name'] + ' ' + response.json['last_name']
            phoneLocalCode = response.json['phone_checkout_local_code']
            phoneCheckoutNumber = response.json['phone_checkout_number']
            orderBump = response.json['order_bump']
            customerEmail = response.json['email']
            productName = response.json['prod_name']
            productPrice = response.json['price']
            sck = response.json['sck']

            customerPhone = phoneLocalCode + ' ' + phoneCheckoutNumber

            return platform, currency, transactionCode, paymentType, status, customerName, phoneLocalCode, phoneCheckoutNumber, orderBump, customerEmail, customerName, productPrice, productName, sck

def parseKiwifyRequest(request):
            platform = 'hotmart'
            currency = response.json['currency']
            transactionCode = response.json['transaction']
            paymentType = response.json['payment_type']
            status = response.json['status']
            customerName = response.json['first_name'] + ' ' + response.json['last_name']
            phoneLocalCode = response.json['phone_checkout_local_code']
            phoneCheckoutNumber = response.json['phone_checkout_number']
            orderBump = response.json['order_bump']
            customerEmail = response.json['email']
            productName = response.json['prod_name']
            productPrice = response.json['price']
            sck = response.json['sck']

            customerPhone = phoneLocalCode + ' ' + phoneCheckoutNumber

            return platform, currency, transactionCode, paymentType, status, customerName, phoneLocalCode, phoneCheckoutNumber, orderBump, customerEmail, customerName, productPrice, productName, sck

def parseGuruRequest(request):
            platform = 'hotmart'
            currency = response.json['currency']
            transactionCode = response.json['transaction']
            paymentType = response.json['payment_type']
            status = response.json['status']
            customerName = response.json['first_name'] + ' ' + response.json['last_name']
            phoneLocalCode = response.json['phone_checkout_local_code']
            phoneCheckoutNumber = response.json['phone_checkout_number']
            orderBump = response.json['order_bump']
            customerEmail = response.json['email']
            productName = response.json['prod_name']
            productPrice = response.json['price']
            sck = response.json['sck']

            customerPhone = phoneLocalCode + ' ' + phoneCheckoutNumber

            return platform, currency, transactionCode, paymentType, status, customerName, phoneLocalCode, phoneCheckoutNumber, orderBump, customerEmail, customerName, productPrice, productName, sck

def createTransactionObject(origin, request):
    if origin == 'hotmart':

            transactionCode, currency, platform, paymentType, status, customerName,\
                customerEmail, customerPhone, productName, productPrice, orderBump, sck = parseHotmartRequest(request)

    elif origin == 'guru':

            transactionCode, currency, platform, paymentType, status, customerName,\
                            customerEmail, customerPhone, productName, productPrice, orderBump, sck = parseGuruRequest(request)

    elif origin == 'kiwify':

                transactionCode, currency, platform, paymentType, status, customerName,\
                            customerEmail, customerPhone, productName, productPrice, orderBump, sck = parseHotmartRequest(request)



    return Transaction(transactionCode, currency, platform, paymentType, status, customerName, customerEmail, customerPhone, productName, productPrice, orderBump, sck)
