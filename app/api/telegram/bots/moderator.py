from flask import jsonify, request, url_for, abort, Response
from app.api import bp
from app.api.errors import bad_request

from app.api.telegram.utils import tel_send_support_urls, tel_send_message, tel_parse_message, tel_send_select_group_button

groupsIds = dict()
groupsIds['adr'] = ''
groupsIds['totalBlues'] = '-1001447351738'
groupsIds['totalBlues'] = '-1001620121463'

@bp.route('/bots/telegram/anja_moderator', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()

        chat_id,txt = tel_parse_message(msg)

        if txt == '/msg_suporte':
            tel_send_select_group_button(chat_id)
        elif "send_msg_support" in txt:
            groupId = txt.split('.')[1]

            print(tel_send_message(chat_id, '<b>Opa! Precisa de ajuda ou suporte técnico sobre algum assunto relacionado ao curso?</b>\n\nFique tranquilo! Nossa equipe técnica vai te ajudar!'))
            tel_send_support_urls(chat_id)
            tel_send_message(chat_id, '<i>Lembrando que nosso suporte funciona em <b>horário comercial</b> e qualquer mensagem relacionada à este assunto deve ser enviada em dos meios de contato acima, ok?</i><br />Obrigado!')


        return Response('ok', status=200)
    else:
        return Response('Método não suportado')
