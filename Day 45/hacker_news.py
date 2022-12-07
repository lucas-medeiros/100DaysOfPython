# @author   Lucas Cardoso de Medeiros
# @since    07/12/2022
# @version  1.0

# Hacker News - Beautiful Soup web scrapping

from bs4 import BeautifulSoup
import requests

URL = "https://news.ycombinator.com/"

response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
article_span = soup.find_all(class_="titleline")

articles = []
for span in article_span:
    articles.append(span.find(name="a"))

articles_text = []
articles_links = []
for article in articles:
    articles_text.append(article.getText())
    articles_links.append(article.get("href"))

articles_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

if len(articles_text) != len(articles_upvote):  # Fix
    articles_upvote.insert(7, 0)

print(f"articles_text: {articles_text}")
print(f"articles_links: {articles_links}")
print(f"articles_upvote: {articles_upvote}")

max_index = articles_upvote.index(max(articles_upvote))
print(f"\n{articles_text[max_index]} - <{articles_links[max_index]}> ({articles_upvote[max_index]} points)")
