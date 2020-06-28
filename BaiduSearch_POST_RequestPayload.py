import requests
param={"wd":"乌龟"}
r=requests.get("https://www.baidu.com/s",params=param,headers={
    "user-agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
})
import webbrowser as we
we.open(r.url) #用默認瀏覽器自動打開該鏈接

data={"firstname":"Alex","lastname":"Fan"}
r2=requests.post(
    "http://pythonscraping.com/pages/files/processing.php",
    data=data)
print(r2.text)

fi={"uploadFile":open("倉鼠.jpg",mode="rb")}
r3=requests.post(
    "http://pythonscraping.com/pages/files/processing2.php",
    files=fi)
print(r3.text)
# import os 
# url=r"C:\Users\ALEX\Desktop\資料暫存\倉鼠.jpg"
# print(os.path.dirname(url))

# payload={"username":"Alex","password":"password"}
# r4=requests.post(
#     "http://pythonscraping.com/pages/cookies/welcome.php",
#     data=payload)
# print(r4.cookies.get_dict())

# r4=requests.get(
#     "http://pythonscraping.com/pages/cookies/welcome.php",
#     cookies=r4.cookies)
# print(r4.text)

session=requests.Session()
payload={"username":"Alex","password":"password"}
r4=session.post(
    "http://pythonscraping.com/pages/cookies/welcome.php",
    data=payload)
print(r4.cookies.get_dict())
print(r4.cookies)
print("-----------------------------------------")
r4=requests.get("http://pythonscraping.com/pages/cookies/welcome.php")
print(r4.text)

r4=session.get("http://pythonscraping.com/pages/cookies/welcome.php")
print(r4.text)
print("-----------------------------------------")