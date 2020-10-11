import bs4 as bs
import urllib.request as request
import requests as req
sauce = request.urlopen('https://suckless.org').read()
soup = bs.BeautifulSoup(sauce, 'html5lib')

# print soup
#print(soup)

# print title
#print(soup.title)

# print intro
#print(soup.p)

# search soup by tag
#print(soup.find_all('p'))

# print all paragraphs
#for paragraph in soup.find_all('p'):
#    print(paragraph)

# print all paragraphs and tags
#for paragraph in soup.find_all('p'):
#    print(paragraph.text)

# print all paragraphs as string
#for paragraph in soup.find_all('p'):
#    print(paragraph.string)

# print ALL text
#print(soup.get_text())

#a = soup.get_text()
#a = a.split("\n")
#for lines in a:
#    print(lines)




