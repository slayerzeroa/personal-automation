from translator import translate_english_to_korean
from get_news_contents import get_cnn_news, get_summary
from upload_site import upload_tistory

contents = get_cnn_news()
summary = get_summary(contents[1])

translated_title = translate_english_to_korean(contents[0])
translated_contents = translate_english_to_korean(summary)
url = contents[2]

upload_tistory(translated_title, translated_contents, url)