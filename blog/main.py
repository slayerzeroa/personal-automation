from translator import papago_english_to_korean, openai_english_to_korean, openai_korean_to_english
from get_news_contents import get_cnn_news, get_summary
from upload_site import upload_tistory

contents = get_cnn_news()
summary = get_summary(contents[1])

translated_title = papago_english_to_korean(contents[0])
translated_contents = papago_english_to_korean(contents[1])
url = contents[2]

upload_tistory(translated_title, translated_contents, url)