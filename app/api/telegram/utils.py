from currency_converter import CurrencyConverter
from flask import Flask
from flask import request
from flask import Response
from flask import jsonify
from flask import make_response
import locale
import requests
import babel.numbers, decimal

currencyConverter = CurrencyConverter()

TOKEN = '5686796450:AAG4H8N1ua04f2SDOmQg5CZCdNwAAz9r7II'

def sendSaleNotification(transaction):

    paymentTypeFormatted = ''
    if transaction.paymentType == 'credit_card':
        paymentTypeFormatted = 'Cartão de crédito'
    elif transaction.paymentType == 'paypal':
        paymentTypeFormatted = 'Paypal'
    elif transaction.paymentType == 'balance_hotmart':
        paymentTypeFormatted = 'Saldo da Hotmart'
    elif transaction.paymentType == 'picpay':
        paymentTypeFormatted = 'PicPay'
    elif transaction.paymentType == 'billet':
        paymentTypeFormatted == 'Boleto bancário'
    elif transaction.paymentType == 'samsung_pay':
        paymentTypeFormatted = 'Samsung Pay'
    elif transaction.paymentType == 'google_pay':
        paymentTypeFormatted = 'Google Pay'
    else:
        paymentTypeFormatted = 'Outros'


    notificationMessageHtml = '\U00002747 <b>VENDA REALIZADA!</b>\r\n\r\n'
    notificationMessageHtml += '<b>Produto:</b>' + transaction.product['name'] + '\r\n'
    notificationMessageHtml += '<b>Plataforma:</b> ' + transaction.platform + '\r\n'
    notificationMessageHtml += '<b>Comprador:</b> ' + transaction.customer['name'] + '\r\n'
    notificationMessageHtml += '<b>E-mail:</b> ' + transaction.customer['email'] + '\r\n'
    notificationMessageHtml += '<b>Código da transação:</b> ' + transaction.code + '\r\n'
    notificationMessageHtml += '<b>Método de pagamento</b>: ' + paymentTypeFormatted + '\r\n'
    notificationMessageHtml += '<b>Moeda</b>: ' + transaction.currency + '\r\n'
    notificationMessageHtml += '<b>Valor:</b> ' + str(babel.numbers.format_currency( decimal.Decimal( transaction.offer['price'] ), transaction.currency )) + '\r\n'

    if(transaction.currency != 'BRL'):
        notificationMessageHtml += '<b>(aproximadamente ' + str(babel.numbers.format_currency(currencyConverter.convert(transaction.offer['price'], transaction.currency, 'BRL'), 'BRL')) + ')</b>\r\n'

    notificationMessageHtml += '<b>Telefone:</b> ' + transaction.customer['mobile_phone']

    telegramResponse = tel_send_message('-1001447351738', notificationMessageHtml)

    return telegramResponse


def tel_parse_message(message):
    print("message-->", message)
    try:
        chat_id = message['message']['chat']['id']
        txt = message['message']['text']
        print("chat_id-->", chat_id)
        print("txt-->", txt)

        return chat_id, txt
    except:
        print("NO text found-->>")

    try:
        cha_id = message['callback_query']['from']['id']
        i_txt = message['callback_query']['data']
        print("cha_id-->", cha_id)
        print("i_txt-->", i_txt)

        return cha_id, i_txt
    except:
        pass

def tel_send_support_urls(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': "<b>Selecione uma das opções abaixo:</b>",
        'reply_markup': {
            "inline_keyboard": [
                [
                    {"text": "Suporte via WhatsApp", "url": "https://wa.me/+5519995576925&text=Olá!%20Preciso%20de%20suporte%20técnico!"},
                    {"text": "Suporte via e-mail", "url": "mailto:suporte@anjadigital.com.br?subject=Suporte+t%C3%A9cnico"}
                ]
            ]
        },
        'parse_mode': 'HTML'
    }
    r = requests.post(url, json=payload)
    return r

def tel_send_message(chat_id, text):

    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': text,
                'parse_mode': 'HTML'
                }

    return requests.post(url,json=payload)



def tel_send_select_group_button(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

    payload = {
        'chat_id': chat_id,
        'text': "Em qual grupo você quer que eu envie a mensagem?",
        'reply_markup': {
            "inline_keyboard": [[
                {
                    "text": "Nieri TEAM",
                    "callback_data": "send_msg_support." + configs.groupsIds['adr']
                },
                {
                    "text": "Total Blues",
                    "callback_data": "send_msg_support." + configs.groupsIds['totalBlues']
                },
                {
                    "text": "Cancelar solicitação",
                    "callback_data": "exit"
                }
                ]
            ]
        }
    }
    r = requests.post(url, json=payload)
    return r