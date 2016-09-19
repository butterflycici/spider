import requests
import re
from bs4 import BeautifulSoup
for i in range(189):
    #url = r"http://apps.webofknowledge.com/summary.do?product=WOS&parentProduct=WOS&search_mode=GeneralSearch&parentQid=&qid=2&SID=Y1wnVLcTXuG7Kw7Aq4E&&update_back2search_link_param=yes&page="+str(i+1)
    url=r"http://apps.webofknowledge.com/summary.do?product=WOS&parentProduct=WOS&search_mode=GeneralSearch&parentQid=&qid=1&SID=1BazTC7TWcKnx8RCPeT&&update_back2search_link_param=yes&page="+str(i+1)
    #这是一本期刊的查询结果的起始网址，总共189页，有30本候选期刊，至少有30个起始网址
    r=requests.get(url)
    html=r.content
    soup = BeautifulSoup(html,'html.parser')
    a= soup.findAll("a", class_='smallV110') 
    for j in range(len(a)):
        value=a[j].find('value',attrs={"lang_id": ""})
        #因为我需要的部分是局部动态加载的，下面这个网址是从控制台network里的XHR找到的
        url1=r"http://apps.webofknowledge.com/ViewAbstract.do?product=WOS&search_mode=GeneralSearch&viewType=ViewAbstract&qid=1&SID=1BazTC7TWcKnx8RCPeT&page="+str(i+1)+"&doc="+str((i*10+j+1)
        r1 = requests.get(url1)
        html1 = r1.content
        soup1 = BeautifulSoup(html1,'html.parser')
        div=soup1.findAll('div')
        f=open("Operations Research-1.txt", "a", encoding = "utf-8")
        if len(div)>1:
                f.write(value.string+";"+div[1].string+"\r\n")
        else:
                f.write(value.string+";"+"None"+"\r\n")
