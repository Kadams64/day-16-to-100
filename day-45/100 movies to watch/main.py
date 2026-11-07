import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
# example entry
"""<div class="article-title-description__text">
  <h3 class="title">100) Stand By Me</h3>
    <div class="descriptionWrapper">
      <p class="description"></p>
      <p><strong>1986</strong><br>
        <a href="https://web.archive.org/web/20200518073855/https://www.empireonline.com/people/rob-reiner/">
        Rob Reiner</a>'s adaptation of 
        <a href="https://web.archive.org/web/20200518073855/https://www.empireonline.com/people/stephen-king/">
        Stephen King</a>'s novella The Body is a stirring, touching adventure film which knows the real world is 
        exciting and scary enough just as it is. It's also a coming-of-age movie which celebrates the intensity of 
        childhood friendship, while gently mourning the transience of such bonds. Which is why, unlike its central 
        character, it'll never get old.<br><br>
        <a href="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/reviews/stand-review/">
        Read Empire's review of Stand By Me</a>
        <br><a href="https://web.archive.org/web/20200518073855/https://www.amazon.co.uk/gp/product/B003BNY6YE/ref=as_li_tl?ie=UTF8&amp;tag=baucitnet-21&amp;camp=1634&amp;creative=6738&amp;linkCode=as2&amp;creativeASIN=B003BNY6YE&amp;linkId=5dd32860f2c5126a8a53f2668f114778" rel="nofollow" class="amazon-link">Buy the film now</a><br></p>
      <p></p>
    </div>
</div>"""
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
results = soup.select("div .article-title-description__text h3")

# reverse the list using slicing
reversed_results = results[::-1]

with open("movies.txt", "a") as file:
    for movie in reversed_results:
        file.write(movie.text + "\n")
