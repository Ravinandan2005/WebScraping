from bs4 import BeautifulSoup as bs
import requests,re,openpyxl,pandas as pd
try:
    hacker_news = {'Rank': [],'Title' : [], 'Link' : [],'Votes': []}
    url = requests.get("https://news.ycombinator.com/")
    html_parser = bs(url.text,'html.parser')
    hackernews = html_parser.findAll("tr",class_='athing')
    subtext = html_parser.findAll('td',class_='subtext')
    
    for news in hackernews:
        index = news.find("td",class_='title').span.text
        index = re.sub('\D',"",index)
        heading = news.find('a',class_='titlelink').get_text(strip=True)
        heading=re.sub("\(.*?\)","()",heading).replace("()","")
        heading=re.sub("\[.*?\]","[]",heading).replace('[]',"")
        link = news.find('a',class_='titlelink').get('href',None)
        hacker_news["Rank"].append(index)
        hacker_news['Title'].append(heading)
        hacker_news['Link'].append(link)
    for moreinfo in subtext:
        pts = moreinfo.select(".score")[0].get_text()
        hacker_news['Votes'].append(pts)
except Exception as err:
    print('Techno Mindz Says Your Code as an ERROR !\n\n>>>',err)
Data_Frame = pd.DataFrame(data = hacker_news)
Data_Frame.to_excel('Hacker-News.xlsx',index=False)
