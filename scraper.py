from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import pandas as pd
page_link_list=[]
link_list=[]
article_list=[]
article_title_list=[]
#https://journalistesfaxien.tn/category/%D8%B1%D9%8A%D8%A7%D8%B6%D8%A9/page/  Sport
#https://journalistesfaxien.tn/category/%D9%86%D8%A8%D8%B6-%D8%B5%D9%81%D8%A7%D9%82%D8%B3/page/ Sfax
#https://journalistesfaxien.tn/category/%D8%A7%D9%84%D8%A3%D8%AE%D8%A8%D8%A7%D8%B1/%D8%A7%D9%84%D8%A3%D8%AE%D8%A8%D8%A7%D8%B1-%D8%A7%D9%84%D9%88%D8%B7%D9%86%D9%8A%D8%A9/page/   national
main_link_list=['https://journalistesfaxien.tn/category/%D9%86%D8%A8%D8%B6-%D8%B5%D9%81%D8%A7%D9%82%D8%B3/page/','https://journalistesfaxien.tn/category/%D8%A7%D9%84%D8%A3%D8%AE%D8%A8%D8%A7%D8%B1/%D8%A7%D9%84%D8%A3%D8%AE%D8%A8%D8%A7%D8%B1-%D8%A7%D9%84%D9%88%D8%B7%D9%86%D9%8A%D8%A9/page/','https://journalistesfaxien.tn/category/%D8%B1%D9%8A%D8%A7%D8%B6%D8%A9/page/']
for k in main_link_list:
      for i in range(10):
            page_link_list.append(k+str(i+1))
            if i==2 & k== 'https://journalistesfaxien.tn/category/%D8%B1%D9%8A%D8%A7%D8%B6%D8%A9/page/': 
              break;                 
      for i in page_link_list :   #extracing (link , type ) of each article
        # URl to web scrap from.
        # # in this example we web scrap graphics cards from Newegg.com
        # # opens the connection and downloads html page from url
        uClient = uReq(i)

        # parses html into a soup data structure to traverse html
        # class="col-md-6 mb-2"
        page_soup = soup(uClient.read(), "html.parser")
        uClient.close()
        containers = page_soup.findAll("div", {"class": "col-md-9"})
        container = containers[0].findAll("div", {"class": "col-md-6 mb-2"}) 
        for con in container:
              #con contains the code of  one article
              link=con.a["href"] 
              link_list.append(link)     #fils link_list with all articles links
              article_title_list.append(con.img["alt"])

      for i in range(len(link_list)):  
        ch=""
        #Scraping One Page Code    
        uClient = uReq(link_list[i])
        page_soup = soup(uClient.read(), "html.parser")
        uClient.close()
        containers = page_soup.findAll("div" ,{"class" : "card-body single-body"})
        for i in containers[0].findAll("p"):
              ch+=i.text
              article_list.append(ch)

Type=''
data={  'title' : article_title_list , 'article' : article_list ,'link'  : link_list,'type': Type}
df1 = pd.DataFrame (data, columns = ['link','article','title','type'])