#This code is using the HTMLSession library in Python to connect to a particular news website
#(in this case, Google News with the URL. 
#It is looping through all the articles on the page, and for each article, 
#it is printing the title and the link associated with the article.

# session = HTMLSession()

# url = 'https://news.google.com/home?hl=en-KE&gl=KE&ceid=KE:en'

# r = session.get(url)
# r.html.render(sleep=1, scrolldown=0)

# articles = r.html.find('article')

# for item in articles:
#     try:
#         newsitem = item.find('h4', first=True)
#         title = newsitem.text
#         link =newsitem.absolute_links

#         print(title, link)
#     except:
#         pass


#This code uses the HTML Session library to make a GET request to the given URL.
#It then renders the HTML with a 1 second sleep and scrolls down 5 times. 
#It locates all the articles on the page and stores them in a list. 
#It then loops through the list of articles and pulls out the title each article, storing them in a dictionary.
#The dictionary is then appended to the newslist list and the contents of the first item in the list are printed.

from requests_html import HTMLSession

session = HTMLSession()

url = 'https://news.google.com/home?hl=en-KE&gl=KE&ceid=KE:en'

r = session.get(url)
r.html.render(sleep=1, scrolldown=5)
articles = r.html.find('article')

newslist =[]

for item in articles:
    try:
        newsitem = item.find('h4',first=True)
        newsarticle ={
        'title' : newsitem.text,  # Added a comma
        'link' : newsitem.absolute_links
        }
        newslist.append(newsarticle)
  
    except:
        pass
print(newslist[0])