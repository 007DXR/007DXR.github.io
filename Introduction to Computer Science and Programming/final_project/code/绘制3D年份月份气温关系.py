# coding:utf-8
# 姓名：董欣然
# 学号：1900013018
# 大作业名称：爬取气象台数据
# 代码实现的功能：绘制3D气温图

from pyecharts import options as opts
from pyecharts.charts import Map, Geo, Timeline,Line3D
from pyecharts.faker import Faker
from pyecharts.globals import ChartType
import pandas as pd
import sqlite3
import csv
city_name=['北京','上海','天津','重庆','哈尔滨','长春','沈阳','呼和浩特','石家庄','太原','西安','济南','乌鲁木齐','拉萨','西宁','兰州','银川','郑州','南京','武汉','杭州','合肥','福州','南昌','长沙','贵阳','成都','广州','昆明','南宁','海口','深圳','台北']
english_name=['Beijing', 'Shanghai', 'Tianjin', 'Chongqing', 'haerbin', 'Changchun', 'Shenyang', 'huhehaote', 'Shijiazhuang', 'Taiyuan', 'Xian', 'Jinan', 'wulumuqi', 'Lasa', 'Xining', 'Lanzhou', 'Yinchuan', 'Zhengzhou', 'Nanjing', 'Wuhan', 'Hangzhou', 'Hefei', 'fujianfuzhou', 'Nanchang', 'Changsha', 'Guiyang', 'Chengdu', 'Guangzhou', 'Kunming', 'Nanning', 'Haikou', 'Shenzhen','taibei']
dicts={'北京':'北京','上海':'上海','天津':'天津','重庆':'重庆','哈尔滨':'黑龙江','长春':'吉林','沈阳':'辽宁','呼和浩特':'内蒙古','石家庄':'河北','太原':'山西','西安':'陕西','济南':'山东','乌鲁木齐':'新疆','拉萨':'西藏','西宁':'青海','兰州':'甘肃','银川':'宁夏','郑州':'河南','南京':'江苏','武汉':'湖北','杭州':'浙江','合肥':'安徽','福州':'福建','南昌':'江西','长沙':'湖南','贵阳':'贵州','成都':'四川','广州':'广东','昆明':'云南','南宁':'广西','海口':'海南','深圳':'深圳','台北':'台湾'}
conn = sqlite3.connect('2011-2021天气汇总.db')
curs = conn.cursor()

days=28
newlist = []

for year in range(2011,2021):
    for city_id in range(0,1):
        curs.execute('''SELECT temperature FROM %s'''%dicts[city_name[city_id]])
        mon_temperature_list=curs.fetchall()
        print("year%s city %s"%(year,city_name[city_id]),len(mon_temperature_list))
        line_start=(year-2011)*12*days;
        line_end=(year-2010)*12*days;
        sum=0
        for i in range(line_start,line_end):
            if not mon_temperature_list[i] or not mon_temperature_list[i][0] or mon_temperature_list[i][0].find('/')==-1:
                sum=sum+50
                print("error"*10)
            else:
                a,b=mon_temperature_list[i][0].split('/')
                #注意条件判断
                if not a[:len(a)-2].strip() or not b[:len(b)-1].strip():
                    sum=sum+50
                    print("error"*10)
                 
                else:
                    high_temperature=eval(a[:len(a)-2])
                    low_temperature=eval(b[:len(b)-1])
                    sum=sum+high_temperature+low_temperature
            #分别将月份，年份，温度作为x,y,z坐标添加到坐标轴上
            if i%days==days-1:
                average_temperature=sum/days/2;
                mon=int((i-line_start)/days)+1;
                newlist.append((mon, year-2010,average_temperature))
                sum=0


(
    Line3D(init_opts=opts.InitOpts(
            width="1500px",
            height="600px",
            animation_opts=opts.AnimationOpts(animation=True),
            page_title="北京近十年各月份气温变化",
        ),)
    .add(
        "",
        newlist,
        xaxis3d_opts=opts.Axis3DOpts(name="月份",type_="category"),
        yaxis3d_opts=opts.Axis3DOpts(name="年份:201x",type_="category"),
        zaxis3d_opts=opts.Axis3DOpts(name="温度(℃)",splitnum=1),
        grid3d_opts=opts.Grid3DOpts(width=100, height=100, depth=100),
        # is_hover_animation=True,
        label_opts=opts.LabelOpts(is_show=True),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="北京近十年各月份气温变化"),
        visualmap_opts=opts.VisualMapOpts(
            dimension=2,
            max_=30,
            min_=0,
            range_color=[
                "#313695",
                "#4575b4",
                "#74add1",
                "#abd9e9",
                "#e0f3f8",
                "#ffffbf",
                "#fee090",
                "#fdae61",
                "#f46d43",
                "#d73027",
                "#a50026",
            ],
        )
    )
    .render("北京近十年各月份气温变化.html")
)   