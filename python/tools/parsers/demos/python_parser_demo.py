import bs4 as bs
import urllib.request as request

sauce = request.urlopen('https://pythonprogramming.net/parsememcparseface/').read()
soup = bs.BeautifulSoup(sauce, 'html5lib')

# print soup
#print(soup)
#print('\n')

# print title
#print(soup.title)
#print('\n')

# intro
#print(soup.p)
#print('\n')

# find paragraph tags
#print(soup.find_all('p'))
#print('\n')

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



