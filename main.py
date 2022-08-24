from turtle import title
import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"


# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify)

# Step 3: HTML Tree traversal

# Commonly used types of objects:

# print(type(title))   # 1. Tag
# print(type(title.string))  # 2. NavigableString
# print(type(soup))   # 3. BeautifulSoup

# 4. Comment

markup = "<p><!-- this is a comment --></p>"
soup2 = BeautifulSoup(markup)
print(soup2.p)   #to print the paragraph
print(soup2.p.string)    #to print the string
print(type(soup2.p.string))  # to know the type
# exit()   # it is used when we want to run the code till now


# Get the title of the HTML page
title = soup.title

# Get all the paragraphs from the page
paras = soup.find_all('p')
# print(paras)



# Get first element in the HTML page
print(soup.find('p'))

# Get classes of any element in the HTML page
print(soup.find('p')['class'])

# find all the elements with class lead
print(soup.find_all("p", class_="lead"))

# get the text from the tags/soup
print(soup.find('p').get_text())

# to get all the text from html page
print(soup.get_text())

# Get all the anchor tags from the page
anchors = soup.find_all('a')
all_links = set()
# Get all the links on the page:
for link in anchors:
    if(link.get('href') != '#'):
        linkText = "https://codewithharry.com" + link.get('href')
        all_links.add(link)
        print(linkText)

# To get the div as output --- actually navbarSupportedContent is the id of element div
navbarSupportedContent = soup.find(id='navbarSupportedContent')
print(navbarSupportedContent)
print(navbarSupportedContent.contents)  # it gives all content which is inside div

# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator
for elem in navbarSupportedContent.contents:
    print(elem)


for item in navbarSupportedContent.strings:
    print(item)    #it will print all string

for item in navbarSupportedContent.stripped_strings:
    print(item)    

print(navbarSupportedContent.parent)

for item in navbarSupportedContent.parents:
    print(item.name)

# print(navbarSupportedContent.next_sibling.next_sibling)
# print(navbarSupportedContent.previous_sibling.previous_sibling)

elem = soup.select('#loginModel')  # to select specific id or class
print(elem)     