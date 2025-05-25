import requests


query = input("enter your query")
API="your_Api_key_here"


url=f"https://newsapi.org/v2/everything?q={query}&from=2025-04-25&sortBy=publishedAt&apiKey={API}"


print(url)

c=requests.get(url)

data = c.json()
articles= data["articles"]

# for index , article in enumerate(articles):
#     print(index+1 , "Title:", article["title"])
#     print("Description:", article["description"])
#     print("URL:", article["url"])
#     print("Published At:", article["publishedAt"])
#     print("-" * 80)  # Separator for readability

with open("news.txt","w", encoding= "utf-8") as f:
    f.write("This is a news file\n")
    for index , article in enumerate(articles):
        f.write(str(index+1) + "Title: " + article.get("title", "N/A") + "\n")
        f.write("Description: " + article.get("description", "N/A") + "\n")
        f.write("URL: " + article.get("url", "N/A") + "\n")
        f.write("Published At: " + article.get("publishedAt", "N/A") + "\n")
        f.write("-" * 80 + "\n")

print("News articles have been written to news.txt")