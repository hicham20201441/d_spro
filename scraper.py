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
nour=set(url)
while(len(urls)>0):
    print("scraping: "+urls[0])
    html1= scraperwiki.scrape(urls[0])
    root1 = lxml.html.fromstring(html1)
    newrls=[e.get("href") for e in root1.cssselect("a")]
    urls=urls+newrls
    print(str(len(newrls))+" new urls"
    scraperwiki.sqlite.save(unique_keys=[urls[0]], data={"link": ur, "body":html1 })
        
 
        
    
  
    
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
