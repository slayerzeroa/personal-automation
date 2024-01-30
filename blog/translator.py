from openai import OpenAI
import os
import sys
import urllib.request
import json


# OpenAI API Key
f = open("blog/env/openai_api.txt", 'r')
api_key = f.readline().strip()
org_key = f.readline().strip()
f.close()

openai_client = OpenAI(
    api_key=api_key
)

# Papago API Key
f = open("blog/env/papago_api.txt", 'r')
papago_id = f.readline().strip()
papago_secret = f.readline().strip()
f.close()

# Chatgpt 한국어 -> 영어 번역
def openai_korean_to_english(korean_text):
    # ChatGPT에 한국어 문장을 전달하여 번역 요청
    response = openai_client.chat.completions.create(
        # model="gpt-3.5-turbo-1106",  # 사용할 엔진 선택
        
        model="gpt-4",  # 사용할 엔진 선택
        messages=[{"role": "system", "content": f"영어로 번역해주세요: {korean_text}\n"}],
        temperature=0.7,  # 낮을수록 보수적인 답변, 높을수록 다양한 답변
        max_tokens=3000  # 반환되는 최대 토큰 수
    )
    # API 응답에서 영어로 번역된 부분 추출
    translation = response.choices[0].message.content
    return translation


# Chatgpt 영어 -> 한국어 번역
def openai_english_to_korean(english_text):
    response = openai_client.chat.completions.create(
        model="gpt-4", 
        messages=[{"role": "system", "content": f"Translate to Korean: {english_text}\n"}],
        temperature=0.7,
        max_tokens=3000 
    )
    translation = response.choices[0].message.content
    return translation

# papago 영어 -> 한국어 번역
def papago_english_to_korean(english_text):
    encText = urllib.parse.quote(english_text)
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", papago_id)
    request.add_header("X-Naver-Client-Secret", papago_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        translation = json.loads(response_body.decode('utf-8'))['message']['result']['translatedText']
        return translation
    else:
        return("Error Code:" + rescode)