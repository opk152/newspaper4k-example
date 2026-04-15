
from newspaper import Article
import json

def analyze_article(url):
    """
    Извлечение данных из статьи с помощью newspaper4k.
    """
    try:
        # 1. Инициализация статьи
        article = Article(url, language='ru') # Чтобы указать язык
        
        # 2. Загрузка и парсинг
        article.download()
        article.parse()
        
        # 3. NLP анализ (ключевые слова и саммари)
        article.nlp()
        
        # 4. Сбор данных в структуру
        data = {
            "title": article.title,
            "authors": article.authors,
            "publish_date": str(article.publish_date),
            "top_image": article.top_image,
            "keywords": article.keywords,
            "summary": article.summary,
            "text_clean": article.text.strip()
        }
        
        return data

    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # Тестовый URL (можно заменить на любой новостной сайт)
    test_url = "https://ria.ru/20260415/tekhnologii-12345678.html"
    
    print(f"--- АНАЛИЗ СТАТЬИ: {test_url} ---")
    result = analyze_article(test_url)
    
    # Вывод в формате JSON (как просил заказчик)
    print(json.dumps(result, indent=4, ensure_ascii=False))
    
    # Сохранение в файл
    with open("result.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=4, ensure_ascii=False)
        print("\n[INFO] Результат сохранен в result.json")
