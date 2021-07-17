# coding:utf-8
# 姓名：董欣然
# 学号：1900013018
# 大作业名称：爬取气象台数据
# 代码实现的功能：爬取数据并用pandas制作表格


import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyquery import PyQuery as pq
import pandas as pd
city_name=['北京','上海','天津','重庆','哈尔滨','长春','沈阳','呼和浩特','石家庄','太原','西安','济南','乌鲁木齐','拉萨','西宁','兰州','银川','郑州','南京','武汉','杭州','合肥','福州','南昌','长沙','贵阳','成都','广州','昆明','南宁','海口','深圳']
english_name=['Beijing', 'Shanghai', 'Tianjin', 'Chongqing', 'haerbin', 'Changchun', 'Shenyang', 'huhehaote', 'Shijiazhuang', 'Taiyuan', 'Xian', 'Jinan', 'wulumuqi', 'Lasa', 'Xining', 'Lanzhou', 'Yinchuan', 'Zhengzhou', 'Nanjing', 'Wuhan', 'Hangzhou', 'Hefei', 'fujianfuzhou', 'Nanchang', 'Changsha', 'Guiyang', 'Chengdu', 'Guangzhou', 'Kunming', 'Nanning', 'Haikou', 'Shenzhen']
category=["","data","weather","temperature","wind"]

options = Options()
#options.add_argument("--headless")  # 不打开浏览器界面，以节省时间
browser = webdriver.Chrome(options=options)


city_id=0
year=2020
data={}
for j in range(1,5):
    data[category[j]]=[]
for mon in range(1,3):
    
    url='http://www.tianqihoubao.com/lishi/%s/month/%d%02d.html'%(english_name[city_id],year,mon);
    print(url)
    browser.get(url)
    
    time.sleep(2)
    
    #获得网页内容，记作pq_doc
    pq_doc = pq(browser.page_source) 
    

    
    #枚举日期
    for i in range(2,30):
        for j in range(1,5):
            item = pq_doc('#content > table > tbody > tr:nth-child({}) > td:nth-child({})'.format(i,j))  
            citem=item.text().strip()
            
            data[category[j]].append(citem)
browser.close()
print(data)
df = pd.DataFrame(data)  

# ------------------------------
# 输出到Excel文件
trgt_filename = './pandas.xlsx'
df.to_excel(trgt_filename)


# 注：如果多次输出到同一个文件，只会保存最后一次输出的工作表（Sheet）
