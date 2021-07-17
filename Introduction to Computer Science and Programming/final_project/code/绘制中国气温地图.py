# coding:utf-8
# 姓名：董欣然
# 学号：1900013018
# 大作业名称：爬取气象台数据
# 代码实现的功能：绘制中国气温地图
from pyecharts import options as opts
from pyecharts.charts import Map, Geo, Timeline
from pyecharts.faker import Faker
from pyecharts.globals import ChartType
import pandas as pd
import sqlite3
import csv
city_name=['北京','上海','天津','重庆','哈尔滨','长春','沈阳','呼和浩特','石家庄','太原','西安','济南','乌鲁木齐','拉萨','西宁','兰州','银川','郑州','南京','武汉','杭州','合肥','福州','南昌','长沙','贵阳','成都','广州','昆明','南宁','海口','深圳','台北']
english_name=['Beijing', 'Shanghai', 'Tianjin', 'Chongqing', 'haerbin', 'Changchun', 'Shenyang', 'huhehaote', 'Shijiazhuang', 'Taiyuan', 'Xian', 'Jinan', 'wulumuqi', 'Lasa', 'Xining', 'Lanzhou', 'Yinchuan', 'Zhengzhou', 'Nanjing', 'Wuhan', 'Hangzhou', 'Hefei', 'fujianfuzhou', 'Nanchang', 'Changsha', 'Guiyang', 'Chengdu', 'Guangzhou', 'Kunming', 'Nanning', 'Haikou', 'Shenzhen','taibei']
dicts={'北京':'北京','上海':'上海','天津':'天津','重庆':'重庆','哈尔滨':'黑龙江','长春':'吉林','沈阳':'辽宁','呼和浩特':'内蒙古','石家庄':'河北','太原':'山西','西安':'陕西','济南':'山东','乌鲁木齐':'新疆','拉萨':'西藏','西宁':'青海','兰州':'甘肃','银川':'宁夏','郑州':'河南','南京':'江苏','武汉':'湖北','杭州':'浙江','合肥':'安徽','福州':'福建','南昌':'江西','长沙':'湖南','贵阳':'贵州','成都':'四川','广州':'广东','昆明':'云南','南宁':'广西','海口':'海南','深圳':'深圳','台北':'台湾'}
#连接数据库
conn = sqlite3.connect('2011-2021天气汇总.db')
curs = conn.cursor()

days=28
#枚举年份，每个年份都绘制一张地图
for year in range(2011,2021):
    newlist = []
    for i in range(0,13):
        newlist.append([])
        #枚举城市
    for city_id in range(0,len(city_name)-1):
        #从数据库导入数据
        curs.execute('''SELECT temperature FROM %s'''%dicts[city_name[city_id]])
        mon_temperature_list=curs.fetchall()
        print("year%s city %s"%(year,city_name[city_id]),len(mon_temperature_list))
        line_start=(year-2011)*12*days;
        line_end=(year-2010)*12*days;
        sum=0
        for i in range(line_start,line_end):
            #数据的清洗，可能出现数据不存在的情况
            if not mon_temperature_list[i] or not mon_temperature_list[i][0] or mon_temperature_list[i][0].find('/')==-1:
                sum=sum+50
                print("error"*10)
            else:
                a,b=mon_temperature_list[i][0].split('/')
                #注意条件判断，可能出现数据不规范的情况
                if not a[:len(a)-2].strip() or not b[:len(b)-1].strip():
                    sum=sum+50
                    print("error"*10)                
                else:
                    high_temperature=eval(a[:len(a)-2])
                    low_temperature=eval(b[:len(b)-1])
                    sum=sum+high_temperature+low_temperature
            #计算月平均气温
            if i%days==days-1:
                average_temperature=sum/days/2;
                mon=int((i-line_start)/days)+1;
                newlist[mon].append((dicts[city_name[city_id]], average_temperature))
                sum=0

    print("year%s well done"%(year))
    #绘制中国气温地图
    tl = Timeline(
        init_opts=opts.InitOpts(
            width="1500px",
            height="500px",
            animation_opts=opts.AnimationOpts(animation=True),
            page_title="%d年中国气温变化"%(year),
        ),
    )
    for i in range(1, 13):
        map0 = (
            Map()
            .add("",
                 newlist[i],
                 "china",
                 is_map_symbol_show=False,)
            .set_global_opts(
                title_opts=opts.TitleOpts(title="{}年{}月全国气温图".format(year,i)),
                visualmap_opts=opts.VisualMapOpts(max_=35, min_=-15),
            )
        )
        tl.add(map0, "{}月".format(i))
    tl.render('./output/中国%d年气温变化.html'%(year))
   