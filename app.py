from flask import Flask, request
from decouple import config
import pprint
import requests

API_TOKEN = config('API_TOKEN')     # 상수는 대문자.
CHAT_ID = config('CHAT_ID')
base_url = 'http://api.telegram.org'
token = config('API_TOKEN')

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World'


@app.route('/greeting/<name>')
def greeting(name):
    return f'안녕하시오 {name}'


@app.route(f'/{API_TOKEN}', methods=['POST'])
def telegram():
    from_telegram = request.get_json()
#    pprint.pprint(from_telegram)
    if from_telegram.get('message') is not None:
        #우리가 원하는 로직 테레그램 메시지가 있는지 확인해보규.
        chat_id = from_telegram.get('message').get('chat').get('id')
        text = from_telegram.get('message').get('text') #이건 사용자가 보내는 텍스트임. 딕셔너리로 저장된 자료에서 빼온거야.

        if text == '점심메뉴':
            text = '치킨'
        if text == '집가고싶어요':
            text = '바로 가자'
        if text == '졸려':
            text = '한숨 자고와'
        if text == '자니?':
            text = '너는 지금 뭐해 자니 밖이야'



        api_url = f'{base_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
        response = requests.get(api_url)
        
        

    return '', 200



if __name__ == '__main__':
    app.run(debug=True)
