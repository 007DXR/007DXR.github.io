# coding:utf-8
# 姓名：董欣然
# 学号：1900013018
# 大作业名称：爬取气象台数据
# 代码实现的功能：绘制晴雨表
from pyecharts import options as opts
from pyecharts.charts import Map,Geo,Timeline
from pyecharts.charts import Bar, Grid, Line, Liquid, Page, Pie,Tab
from pyecharts.faker import Faker
from pyecharts.globals import ChartType
import pandas as pd
import sqlite3
import csv
city_name=['北京','上海','天津','重庆','哈尔滨','长春','沈阳','呼和浩特','石家庄','太原','西安','济南','乌鲁木齐','拉萨','西宁','兰州','银川','郑州','南京','武汉','杭州','合肥','福州','南昌','长沙','贵阳','成都','广州','昆明','南宁','海口','深圳']
english_name=['Beijing', 'Shanghai', 'Tianjin', 'Chongqing', 'haerbin', 'Changchun', 'Shenyang', 'huhehaote', 'Shijiazhuang', 'Taiyuan', 'Xian', 'Jinan', 'wulumuqi', 'Lasa', 'Xining', 'Lanzhou', 'Yinchuan', 'Zhengzhou', 'Nanjing', 'Wuhan', 'Hangzhou', 'Hefei', 'fujianfuzhou', 'Nanchang', 'Changsha', 'Guiyang', 'Chengdu', 'Guangzhou', 'Kunming', 'Nanning', 'Haikou', 'Shenzhen']
dicts={'北京':'北京','上海':'上海','天津':'天津','重庆':'重庆','哈尔滨':'黑龙江','长春':'吉林','沈阳':'辽宁','呼和浩特':'内蒙古','石家庄':'河北','太原':'山西','西安':'陕西','济南':'山东','乌鲁木齐':'新疆','拉萨':'西藏','西宁':'青海','兰州':'甘肃','银川':'宁夏','郑州':'河南','南京':'江苏','武汉':'湖北','杭州':'浙江','合肥':'安徽','福州':'福建','南昌':'江西','长沙':'湖南','贵阳':'贵州','成都':'四川','广州':'广东','昆明':'云南','南宁':'广西','海口':'海南','深圳':'深圳'}
tab = Tab()

for city_id in range(1,32):
    
    days=29

    conn = sqlite3.connect('../SQLite/2020天气汇总.db')
    curs = conn.cursor()
    #从数据库导入关键字为weather的数据
    curs.execute('''SELECT weather FROM %s'''%city_name[city_id])
    weather_list=curs.fetchall()
    curs.close()
    weather_dicts={}
    #统计每种天气出现的次数
    for i in range(0,days*12):
        a=weather_list[i][0].split('/')
        if a[0] in weather_dicts.keys():
            weather_dicts[a[0]]+=1
            
        else:
            weather_dicts[a[0]]=1
       
    data_list = list(weather_dicts.items())
    
    print(data_list)
    
    
    c = (
        Pie(init_opts=opts.InitOpts(
                width="1500px",
                height="800px",
                animation_opts=opts.AnimationOpts(animation=True),
                page_title="晴雨表",
            ),)
        .add(

            "",

            data_list,
            radius=["30%", "55%"],
            center=["50%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(
                position="outside",
                formatter="{a|天数}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                background_color="#eee",
                border_color="#aaa",
                border_width=1,
                border_radius=4,
                rich={
                    "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                    "abg": {
                        "backgroundColor": "#e3e3e3",
                        "width": "100%",
                        "align": "right",
                        "height": 22,
                        "borderRadius": [4, 4, 0, 0],
                    },
                    "hr": {
                        "borderColor": "#aaa",
                        "width": "100%",
                        "borderWidth": 0.5,
                        "height": 0,
                    },
                    "b": {"fontSize": 16, "lineHeight": 33},
                    "per": {
                        "color": "#eee",
                        "backgroundColor": "#334455",
                        "padding": [2, 4],
                        "borderRadius": 2,
                    },
                },
            ),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="%s晴雨表"%(city_name[city_id])),
           legend_opts=opts.LegendOpts(
                pos_left="15%",
                pos_right="30%"
            ),
        )
    )
    tab.add(c, (city_name[city_id]))

tab.render("晴雨表.html")
