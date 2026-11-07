from bs4 import BeautifulSoup
import requests

'''https://news.ycombinator.com/news'''
response = requests.get("https://news.ycombinator.com/news")

page_content = response.text
# a hef class=storylink

soup=BeautifulSoup(page_content,"html.parser")

stories = soup.select("span.titleline a[href]")
# spans = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []
for story in stories:
    article_texts.append(story.text)
    article_links.append(story.get("href"))

article_scores =[int(score.get_text().split()[0]) for score in soup.select("span.score")]

# print(article_scores)
max_index = article_scores.index(max(article_scores))
#print(max_index)
print(article_texts)
print(article_links)
# print(article_texts[max_index])
# print(article_links[max_index])
# print(article_scores[max_index])