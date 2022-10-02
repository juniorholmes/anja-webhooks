from flask import jsonify, request, url_for, abort, Response, jsonify, make_response
import json
import phonenumbers

from app.models.orders.transaction import Transaction
from app.api.telegram.utils import sendSaleNotification

from app.api import bp
from app.api.errors import bad_request

@bp.route('/orders/transactions/hotmart/purchase_approved', methods=['GET', 'POST'])
def hotmart():
    if request.method == 'POST':
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

        if status == 'approved':
            transaction = Transaction(transactionCode, currency, platform, paymentType, status, customerName, customerEmail, customerPhone, productName, productPrice, orderBump, sck)
            sendSaleNotification(transaction)

            return Response(jsonify({'success': True}), 200)

    else:
        return Response('Método não suportado')