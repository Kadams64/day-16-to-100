from bs4 import BeautifulSoup

with open("website.html", "r") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     print(tag.get_text())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading= soup.find(name="h3", class_="heading")
# print(section_heading)

#use a css selector to identify an element
# select_one finds the first match; select returns a matching list
company_url = soup.select_one(selector="p a")
print(company_url)

