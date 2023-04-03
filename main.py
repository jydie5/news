import requests
import streamlit as st
import os

#deeplに持ってゆく関数
def translate(text):
    url_deep = "https://api-free.deepl.com/v2/translate"
    params_deep = {
        "auth_key": os.environ['DEEPL_API'],
        "text": text,
        "source_lang": "EN",
        "target_lang": "ZH"
        #"target_lang": "JA" 
        }
    response_deep = requests.post(url_deep, data=params_deep)
    if response_deep.status_code == 200:
        return response_deep.json()["translations"][0]["text"]
    else:
        return None


# NewsAPIのエンドポイントとパラメータを指定する
url = 'https://newsapi.org/v2/top-headlines'
params = {
    'country': 'us',
    'apiKey': os.environ['NEWS_API'],
    'pageSize': '5'
}

# NewsAPIにリクエストを送信する
response = requests.get(url,params=params)

# レスポンスのJSONデータを取得する
data = response.json()

# レスポンスの記事を表示する
for article in data['articles']:
    #print(article['title'])
    #st.write(article['title'])
    st.write(f"# {article['title']}")
    st.write(translate(article['title']))
    st.write(f"# {article['description']}")    
    st.write(translate(article['description']))
    st.write('==========================================')