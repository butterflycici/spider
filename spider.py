import requests
import re
from bs4 import BeautifulSoup
for i in range(1,3073):
    url_1="http://apps.webofknowledge.com/full_record.do?product=WOS&search_mode=GeneralSearch&qid=9&SID=R2pzNDSEViFRe9HKGNA&doc="
    url_2=str(i)
    url='{0}{1}'.format(url_1,url_2)
    #print(url)
    try:
        
        #timeout = 20    
        #socket.setdefaulttimeout(timeout)#这里对整个socket层设置超时时间。后续文件中如果再使用到socket，不必再设置  
        #sleep_download_time = 10  
        #time.sleep(sleep_download_time) #这里时间自己设定  
        #request = urllib.request.urlopen(url)#这里是要读取内容的url  
        #content = request.read()#读取，一般会在这里报异常  
        #request.close()
        r=requests.get(url,timeout=(3.05, 27))
        html=r.content
        soup = BeautifulSoup(html,'html.parser')
        #value= soup.find('div',{'class':'title'}).findNext('value') 
        address=soup.findAll('td',{'class':'fr_address_row2'})
        #print(E.text)
        if len(address)>=1:
            Address=address[0]
            f=open("country+Annals of Operations Research.txt", "a", encoding = "utf-8")
            f.write(str(i)+"|  |"+Address.text.split(", ")[-2]+"|"+Address.text.split(", ")[-1].split(".")[0]+"\r")
            f.close()

            #print(value.text,99,Address.text.split(", ")[-2],99,Address.text.split(", ")[-1].split(".")[0])
                
        else:
            f=open("country+Annals of Operations Research.txt", "a", encoding = "utf-8")
            f.write(str(i)+"|  |  |"+"\r")
            f.close()
                #R=soup.find(text=re.compile("Reprint Address")).findNext("a")
                #print(E.string)
                #print(value.text,Address.text.split(", ")[-1])
    except Exception as e:
        print (Exception,":",e) 
