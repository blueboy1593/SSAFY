import requests     # 요청을 하기 위한 모듈
import pprint
from decouple import config

base_url = 'http://api.telegram.org'
token = config('API_TOKEN')
chat_id = config('CHAT_ID')
text = '디커플 테스트'

api_url = f'{base_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
print(api_url)

# 요청을 해서 --라는 메세지를 보내라는 뜻.
response = requests.get(api_url) # 신호를 보내는건 아무래도 여기겠지??
pprint.pprint(response.json())

#저장하고 실행하는 순간 리퀘스트를 통해서 채팅을 바로 하나 봄. 