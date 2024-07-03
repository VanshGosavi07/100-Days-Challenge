from bs4 import BeautifulSoup

# Open and read the HTML file
with open("website.html", encoding="utf-8") as file:
    content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(content, "html.parser")

# Print the parsed HTML content
# print(soup)
print(soup.body.p.em.strong.a)
print(soup.find(name="h1", id='name'))

