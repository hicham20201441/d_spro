# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
# -*- coding: utf-8 -*-
import scraperwiki
import lxml.html
#
url="https://dollarsprout.com"
# # Read in a page
html = scraperwiki.scrape(url)
#
# # Find something on the page using css selectors
root = lxml.html.fromstring(html)
urlss=[e.get("href") for e in root.cssselect("a")]
urls=[]
for k in urlss:
    if url in k and url!=k:
        urls.append(k)
        scraperwiki.sqlite.save(unique_keys=["link"], data={"link":k})
nlist=set()
nlist.add(url)
while(len(urls)>0):
    if urls[0] not in nlist:
        print("scraping: "+urls[0])
        nlist.add(urls[0])
        html1= scraperwiki.scrape(urls[0])
        root1 = lxml.html.fromstring(html1)
        newrls=[e.get("href") for e in root1.cssselect("a")]
        for u in newrls:
            if url in u and url!=u:
                urls.append(u)
                scraperwiki.sqlite.save(unique_keys=["link"], data={"link": u})
        urls.pop(0)
        
 
        
    
  
    
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
