import requests

query = input("What type of news are you interested in today?")
api = "c092347d641146d3a78dd524d62632c3"  # Here you need to use your own api key. so, create a api key from news api

url = f"https://newsapi.org/v2/everything?q={query}&sortBy=publishedAt&apiKey={api}"
# print(url)

r = requests.get(url)
data = r.json()

if data.get("status") == "ok":
    articles = data.get("articles", [])
    for index, article in enumerate(articles):
        print(index+1, article["title"])
        print(article["url"])
        print("\n***************************\n")
else:
    print("API Error:")
    print(data.get("message"))