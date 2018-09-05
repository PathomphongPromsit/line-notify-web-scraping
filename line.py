import requests,json
import urllib
import requests
from time import sleep
from pyquery import PyQuery as pq

LINE_ACCESS_TOKEN="KLNGqiyWpecmLbYw25G3iNRZimykEeVVP9irGRjNvPN"

LINE_ACCESS_TOKEN2="tFGeHtjvEcJGLEsQptvRPZ6M3v5U7rcTqNTGQwm7Rka"
url = "https://notify-api.line.me/api/notify"
b= "http://www.radd-atc.com/patitin_31.html"
c= "Not"
while True:
        doc = pq(url = "http://www.radd-atc.com/patitin_31.html")
        data = doc('a[href$="668.pdf"]')
        #print (len(data))
        chk = 1
        if len(data) != 1 and len(data) != 0:
        	print(len(data))
        	# message = b
        	# msg = urllib.parse.urlencode({"message":message})
        	# LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN1}
        	# session = requests.Session()
        	# a=session.post(url, headers=LINE_HEADERS, data=msg)
        	# print(a.text)
        	break
        

        else:
            print (len(data))
            if len(data) == 0:
                chk = 0
            else:
                chk = 1 
            #if len(data) == 0 and chk == 0:
                #CLOSE WEB

                # message = b
                # msg = urllib.parse.urlencode({"message":message})
                # LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN2}
                # session = requests.Session()
                # a=session.post(url, headers=LINE_HEADERS, data=msg)
                # print(a.text)
                



            # message = c
            
            # msg = urllib.parse.urlencode({"message":message})
            # #msg = "message = Not"
            # LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN2}
            # session = requests.Session()
            # a=session.post(url, headers=LINE_HEADERS, data=msg)
            # print(a.text)
        sleep(30)
                

# message = b
# msg = urllib.parse.urlencode({"message":message})
# LINE_HEADERS = {'Content-Type':'application/x-www-form-urlencoded',"Authorization":"Bearer "+LINE_ACCESS_TOKEN}
# session = requests.Session()
# a=session.post(url, headers=LINE_HEADERS, data=msg)
# print(a.text)
