from flask import Flask
from flask import request
from flask import Response
import requests

TOKEN = '5679408218:AAFaEL5SL7b17dIGcPgJQfzQ3faJSAfAlXo'

groupsIds = dict()
groupsIds['adr'] = ''
groupsIds['totalBlues'] = '-1001638158841'

app = Flask(__name__)

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
        'parse_mode': 'HTML
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
   
    r = requests.post(url,json=payload)
    return r

def tel_send_select_group_button(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': "Em qual grupo você quer que eu envie a mensagem?",
        'reply_markup': {
            "inline_keyboard": [[
                {
                    "text": "Nieri TEAM",
                    "callback_data": "send_msg_support.0"
                },
                {
                    "text": "Total Blues",
                    "callback_data": "send_msg_support.-1001638158841"
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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()

        chat_id,txt = tel_parse_message(msg)

        try:

            if txt == '/msg_suporte':
                tel_send_select_group_button(chat_id)
        
            elif "send_msg_support" in txt:

                groupId = txt.split('.')[1]

                print(tel_send_message(chat_id, '<b>Opa! Precisa de ajuda ou suporte técnico sobre algum assunto relacionado ao curso?</b>\n\nFique tranquilo! Nossa equipe técnica vai te ajudar!'))
                tel_send_support_urls(chat_id)
                tel_send_message(chat_id, '<i>Lembrando que nosso suporte funciona em <b>horário comercial</b> e qualquer mensagem relacionada à este assunto deve ser enviada em dos meios de contato acima, ok?</i><br />Obrigado!')
        except:
            print("fromindex-->")

        try:
            file_id = tel_parse_get_message(msg)
            tel_upload_file(file_id)
        except:
            print("No file from index-->")


        return Response('ok', status=200)
    else:
        return 'erro!'

if __name__ == '__main__':
   app.run(threaded=True)


   