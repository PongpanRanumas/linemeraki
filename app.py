# encoding: utf-8

import datetime
import errno
import os
import sys
import tempfile
import requests
import meraki

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    LineBotApiError, InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom)

app = Flask(__name__)

line_bot_api = LineBotApi('eEZje2r/ClGNk6XMHgy4pqlnDOEQXZGafKFIZDkUkaBaIs3KsvkZvam/QWZpjQWPWA4KDgzWa6Nksv/BERIXRGVixAffr2IvW/5m6CFE0OZt+LfffE/aosDKFV2VyCuXmdJahzez+3v3gmfpl/69NQdB04t89/1O/w1cDnyilFU=') #Your Channel Access Token
handler = WebhookHandler('ebe5661d1aa37be0f97a0ec4dc1346ca') #Your Channel Secret

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text #message from user
    
    if (text.lower()) == 'organization':
            line_bot_api.reply_message(event.reply_token,TextMessage(text=meraki.orgdetail()))
    else : 
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='What is '+text+' MerakiPongpan Not Understand'))
            
if __name__ == "__main__":
  app.run(host='0.0.0.0',port=os.environ['PORT'])
