import requests
from bs4 import BeautifulSoup

import gzip

def http_request():
    url = 'https://httpbin.org/anything'
    myobj = {'isadmin' :1}
    x= requests.post(url, params = myobj)
    myobj2= {'user-agent' : "a test"}
    y =requests.post(url, params = myobj2)
    return x.text
   

class ReadAGz:
    

    def __readFile__(self): 
         with gzip.open("data.json.gz", "rb") as f:
            data= f.read()
            print(data)



url = 'https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas'
response = requests.get(url)
if response.ok :

    soup = BeautifulSoup(response.text,'html.parser')
    title= soup.find('title')
    print(title.text)