import requests
from bs4 import BeautifulSoup


def scrape_hacker_news():
  url = "https://news.ycombinator.com/news"
  headers = {
      "User-Agent": (
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
          "AppleWebKit/537.36 (KHTML, like Gecko) "
          "Chrome/122.0.0.0 Safari/537.36"
      )
  }

  response = requests.get(url, headers=headers)
  response.raise_for_status()

  soup = BeautifulSoup(response.text, "html.parser")

  # Hacker News places main story titles inside <span class="titleline"><a>
  titlelines = soup.find_all("span", class_="titleline")
  print(titlelines)

  stories = []
  for line in titlelines:
    a_tag = line.find("a")
    if a_tag:
      title = a_tag.get_text(strip=True)
      href = a_tag.get("href")
      stories.append({"title": title, "link": href})

  return stories


if __name__ == "__main__":
  articles = scrape_hacker_news()
  print(len(articles))
  for i, article in enumerate(articles[:15], 1):
    print(f"{i}. {article['title']}")
    print(f"   URL: {article['link']}\n")