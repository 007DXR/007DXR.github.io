# coding:utf-8
# 姓名：董欣然
# 学号：1900013018
# 大作业名称：爬取气象台数据
# 代码实现的功能：爬取数据并导入数据库
import sqlite3

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyquery import PyQuery as pq
city_name=['北京','上海','天津','重庆','哈尔滨','长春','沈阳','呼和浩特','石家庄','太原','西安','济南','乌鲁木齐','拉萨','西宁','兰州','银川','郑州','南京','武汉','杭州','合肥','福州','南昌','长沙','贵阳','成都','广州','昆明','南宁','海口','深圳','台北']
english_name=['Beijing', 'Shanghai', 'Tianjin', 'Chongqing', 'haerbin', 'Changchun', 'Shenyang', 'huhehaote', 'Shijiazhuang', 'Taiyuan', 'Xian', 'Jinan', 'wulumuqi', 'Lasa', 'Xining', 'Lanzhou', 'Yinchuan', 'Zhengzhou', 'Nanjing', 'Wuhan', 'Hangzhou', 'Hefei', 'fujianfuzhou', 'Nanchang', 'Changsha', 'Guiyang', 'Chengdu', 'Guangzhou', 'Kunming', 'Nanning', 'Haikou', 'Shenzhen','taibei']
dicts={'北京':'北京','上海':'上海','天津':'天津','重庆':'重庆','哈尔滨':'黑龙江','长春':'吉林','沈阳':'辽宁','呼和浩特':'内蒙古','石家庄':'河北','太原':'山西','西安':'陕西','济南':'山东','乌鲁木齐':'新疆','拉萨':'西藏','西宁':'青海','兰州':'甘肃','银川':'宁夏','郑州':'河南','南京':'江苏','武汉':'湖北','杭州':'浙江','合肥':'安徽','福州':'福建','南昌':'江西','长沙':'湖南','贵阳':'贵州','成都':'四川','广州':'广东','昆明':'云南','南宁':'广西','海口':'海南','深圳':'深圳','台北':'台湾'}
options = Options()
#options.add_argument("--headless")  # 不打开浏览器界面，以节省时间
browser = webdriver.Chrome(options=options)
conn = sqlite3.connect('2011-2021天气汇总.db')
print ("Opened database successfully")

#创建游标，可以用来执行SQL查询等
curs = conn.cursor()


# SQL = "CREATE TABLE if not exists shanghai(data,weather,temperature,wind);"
# curs.execute(SQL)
# print ("Table created sucessfully")
#注：对数据库操作后只是将数据缓存在内存中，并没有真正的写入数据库

#提交，这样才可以将修改真正的保存到文件中
#应该在每次修改数据库后都进行提交，而不仅仅是准备关闭时才提交
conn.commit()



for city_id in range(18,len(city_name)):
   #创建表，在数据库2011-2021天气汇总.db中创建名为省份名称的表

    SQL = "CREATE TABLE if not exists %s(data,weather,temperature,wind);"%(dicts[city_name[city_id]])
    curs.execute(SQL)
    print ("%sTable created sucessfully"%(city_name[city_id]))
    
    #创建临时文件，用于储存从网上爬取的信息
    temporary_filename = './output/a.csv'
     #创建名为省份名称的文件，用于对网上爬取的信息做备份
    result_filename = './output/%s.csv'%(city_name[city_id])
    result_file = open(result_filename, 'w')
    for year in range(2011,2021):
        for mon in range(1,13):
            url='http://www.tianqihoubao.com/lishi/%s/month/%d%02d.html'%(english_name[city_id],year,mon);
            print(url)
            browser.get(url)
            #等待2s保证网页加载完成
            time.sleep(2)
            
            #发现网站存在广告弹窗，解决方式是：点击网页任意位置，弹窗消失
            inbox = browser.find_element_by_css_selector('body')
            inbox.click()

            pq_doc = pq(browser.page_source) 
            #获得网页内容，记作pq_doc
            #打开临时文件，每次文件内容清空
            temporary_file = open(temporary_filename, 'w')
            #枚举日期
            for i in range(2,30):
                for j in range(1,5):
                    item = pq_doc('#content > table > tbody > tr:nth-child({}) > td:nth-child({})'.format(i,j))  
                    citem=item.text().strip()
                    #将爬取的内容存入临时文件，和省份名称的文件中
                    result_file.write(citem)
                    temporary_file.write(citem)
                    if j!=4:
                        result_file.write(',')
                        temporary_file.write(',')
                    else:
                        result_file.write('\n')
                        temporary_file.write('\n')
                    # print(citem)
                
            temporary_file.close() 
            #阶段性爬取完信息后，将文件导入数据库中
            query = "INSERT INTO %s VALUES(?,?,?,?)"%(dicts[city_name[city_id]])
            
            #从csv文件向表格中导入数据
            for line in open(temporary_filename):
                line = line.strip('\n')
                fields = line.split(',')
                curs.execute(query,fields)
                
            print('month {} insert data sucessfully'.format(mon))
            conn.commit()
            
            #执行查询，检查数据是否插入成功
            # curs.execute('SELECT *FROM beijing')
            # print(curs.fetchall())
            print ("Operation done successfully")
    result_file.close() 
#关闭数据库        
conn.close()