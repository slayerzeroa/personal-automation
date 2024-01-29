from openai import OpenAI

# OpenAI API Key
f = open("naver-blog/env/openai_api.txt", 'r')
api_key = f.readline()
f.close()


client = OpenAI(
    api_key=api_key
)


# 한국어 -> 영어 번역
def translate_korean_to_english(korean_text):
    # ChatGPT에 한국어 문장을 전달하여 번역 요청
    response = client.chat.completions.create(
        # model="gpt-3.5-turbo-1106",  # 사용할 엔진 선택
        
        model="gpt-4",  # 사용할 엔진 선택
        messages=[{"role": "system", "content": f"영어로 번역해주세요: {korean_text}\n"}],
        temperature=0.7,  # 낮을수록 보수적인 답변, 높을수록 다양한 답변
        max_tokens=3000  # 반환되는 최대 토큰 수
    )
    # API 응답에서 영어로 번역된 부분 추출
    translation = response.choices[0].message.content
    return translation


# 영어 -> 한국어 번역
def translate_english_to_korean(english_text):
    response = client.chat.completions.create(
        model="gpt-4", 
        messages=[{"role": "system", "content": f"Translate to Korean: {english_text}\n"}],
        temperature=0.7,
        max_tokens=3000 
    )
    translation = response.choices[0].message.content
    return translation