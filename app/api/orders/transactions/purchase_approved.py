from flask import jsonify, request, url_for, abort, Response, jsonify, make_response
import json

from app.models.orders.transaction import Transaction
from app.api.telegram.utils import sendSaleNotification

from app.api import bp
from app.api.errors import bad_request

from app.api.orders.transactions.factories import createTransactionObject

@bp.route('/orders/transactions/purchase_approved/<platform>', methods=['GET', 'POST'])
def purchaseApproved(platform):
    if request.method == 'POST':

        if request.json['status'] == 'approved':

            transaction = createTransactionObject(platform, request)
            sendSaleNotification(transaction)

            return Response(jsonify({'success': True}), 200)

    else:
        return Response('Método não suportado')