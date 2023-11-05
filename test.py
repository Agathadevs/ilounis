#import requests
#from bs4 import BeautifulSoup

#url = 'https://www.cwa.gov.tw/V8/C/'
#web = requests.get(url)                        # 取得網頁內容
#soup = BeautifulSoup(web.text, "html5lib")  # 轉換成標籤樹
                           # 取得 title
#print(soup.css.select(".icon")[0 ])  
import requests

url = 'https://opendata.cwa.gov.tw/fileapi/v1/opendataapi/F-C0032-001?Authorization=CWA-877EA591-BC8A-4DD2-8B60-4272DAC4BBAC&downloadType=WEB&format=JSON'
data = requests.get(url)   
data_json = data.json()    
location = data_json['cwaopendata']['dataset']['location']   # 取出 location 的內容
for i in location:
    city = i['locationName']    # 縣市名稱
    wx8 = i['weatherElement'][0]['time'][0]['parameter']['parameterName']    # 天氣現象
    maxt8 = i['weatherElement'][1]['time'][0]['parameter']['parameterName']  # 最高溫
    mint8 = i['weatherElement'][2]['time'][0]['parameter']['parameterName']  # 最低溫
    ci8 = i['weatherElement'][3]['time'][0]['parameter']['parameterName']    # 舒適度
    pop8 = i['weatherElement'][4]['time'][0]['parameter']['parameterName']   # 降雨機率
    print(f'{city}未來 8 小時{wx8}，最高溫 {maxt8} 度，最低溫 {mint8} 度，降雨機率 {pop8} %')
  