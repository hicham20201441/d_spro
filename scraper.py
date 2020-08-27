# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import lxml.html
#
url="https://dollarsprout.com"
# # Read in a page
html = scraperwiki.scrape(url)
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
urls=[e.get("href") for e in root.cssselect("a")]
while(len(urls)>0):
  if url in urls[0] and urls!=url:
    ur=urls[0]
    print("scraping: "+ur)
    html1= scraperwiki.scrape(urls[0])
    root1 = lxml.html.fromstring(html1)
    urls.pop(0)
    newrls=[e.get("href") for e in root1.cssselect("a")]
    urls=urls+newrls
    try:
      if root1.cssselect("div[class='blog-col']"):
        scraperwiki.sqlite.save(unique_keys=[ur], data={"link": ur, "blog":root1.cssselect("div[class='blog-col']") })
        print("got a blog!")
      else:
        print("no article for this link")
        pass
    except:pass
  else:pass
        
    
  
    
  #scraperwiki.sqlite.save(unique_keys=[e.get("href")], data={"link": e.get("href")})

#root.cssselect("div[class='blog-col']")
#
# # Write out to the sqlite database using scraperwiki library
#scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
