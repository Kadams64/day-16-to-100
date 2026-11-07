from bs4 import BeautifulSoup
import requests

'''https://news.ycombinator.com/news'''
response = requests.get("https://news.ycombinator.com/news")

page_content = response.text
# a hef class=storylink

soup=BeautifulSoup(page_content,"html.parser")

# A single title from ycombinator looks kind of like the following, with multiple anchor tags
"""<span class="titleline">
    <a href="https://hunch.net/?p=13764006">The end of Microsoft Research's AI Frontiers group</a>
        <span class="sitebit comhead"> 
            (<a href="from?site=hunch.net">
            <span class="sitestr">hunch.net</span></a>)
        </span>
   </span>"""
stories = soup.find_all(name="span", class_="titleline")

article_texts = []
article_links = []
for story in stories:
    a_tag = story.find("a") # find the first anchor tag
                            # note that there were multiple anchor tags in the titleline
                            # span I downloaded
    article_texts.append(a_tag.text)
    article_links.append(a_tag["href"])

# use list comprehension to get a list of all the scores as integers
article_scores =[int(score.get_text().split()[0]) for score in soup.select("span.score")]

max_index = article_scores.index(max(article_scores))

print(article_texts[max_index])
print(article_links[max_index])
print(article_scores[max_index])