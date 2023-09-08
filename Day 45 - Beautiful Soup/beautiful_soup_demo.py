# @author   Lucas Cardoso de Medeiros
# @since    07/12/2022
# @version  1.0

# Beautiful Soup web scrapping

from bs4 import BeautifulSoup

try:
    with open("website.html") as file:
        contents = file.read()
except Exception as e:
    print('Failed to open file: ' + str(e))
    exit(-1)

soup = BeautifulSoup(contents, "html.parser")

# Get first html element
print(soup.title)
print(soup.title.name)
print(soup.title.string)

# Get all html elements
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.get("href"))

# Get element by id
heading = soup.find(name="h1", id="name")
print(heading)

# Get element by class
section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

# Select elements by id
name = soup.select_one(selector="#name")
print(name)

# Select elements by class
headings = soup.select(".heading")
print(headings)
