# coding:utf-8
# 姓名：董欣然
# 学号：1900013018
# 大作业名称：爬取气象台数据
# 代码实现的功能：绘制折线柱状图
from pyecharts import options as opts
from pyecharts.charts import Map,Geo,Timeline
from pyecharts.faker import Faker
from pyecharts.globals import ChartType
import pandas as pd
import sqlite3
import csv
city_name=['北京','上海','天津','重庆','哈尔滨','长春','沈阳','呼和浩特','石家庄','太原','西安','济南','乌鲁木齐','拉萨','西宁','兰州','银川','郑州','南京','武汉','杭州','合肥','福州','南昌','长沙','贵阳','成都','广州','昆明','南宁','海口','深圳']
english_name=['Beijing', 'Shanghai', 'Tianjin', 'Chongqing', 'haerbin', 'Changchun', 'Shenyang', 'huhehaote', 'Shijiazhuang', 'Taiyuan', 'Xian', 'Jinan', 'wulumuqi', 'Lasa', 'Xining', 'Lanzhou', 'Yinchuan', 'Zhengzhou', 'Nanjing', 'Wuhan', 'Hangzhou', 'Hefei', 'fujianfuzhou', 'Nanchang', 'Changsha', 'Guiyang', 'Chengdu', 'Guangzhou', 'Kunming', 'Nanning', 'Haikou', 'Shenzhen']
dicts={'北京':'北京','上海':'上海','天津':'天津','重庆':'重庆','哈尔滨':'黑龙江','长春':'吉林','沈阳':'辽宁','呼和浩特':'内蒙古','石家庄':'河北','太原':'山西','西安':'陕西','济南':'山东','乌鲁木齐':'新疆','拉萨':'西藏','西宁':'青海','兰州':'甘肃','银川':'宁夏','郑州':'河南','南京':'江苏','武汉':'湖北','杭州':'浙江','合肥':'安徽','福州':'福建','南昌':'江西','长沙':'湖南','贵阳':'贵州','成都':'四川','广州':'广东','昆明':'云南','南宁':'广西','海口':'海南','深圳':'深圳'}
conn = sqlite3.connect('weather.db')
curs = conn.cursor()

import requests
from typing import List, Union

from pyecharts import options as opts
from pyecharts.charts import Kline, Line, Bar, Grid

days=29
#设置横坐标
data_x=["{}月{}日".format(i + 1,j+1) for i in range(12) for j in range(days)]

#设置柱状图的基本参数
kline = (
    Kline()
    .add_xaxis(xaxis_data=data_x)
    
    .set_global_opts(
        
        title_opts=opts.TitleOpts(title="2020年全国温度分析"),

        legend_opts=opts.LegendOpts(
            # is_show=True,
            # pos_top=10
            pos_left="15%",
            pos_right="30%"
        ),
        #设置可拖拽时间轴
        datazoom_opts=[
            opts.DataZoomOpts(
                is_show=True,
                type_="inside",
                xaxis_index=[0, 1],
                range_start=2,
                range_end=100,
            ),
            opts.DataZoomOpts(
                is_show=True,
                xaxis_index=[0, 1],
                type_="slider",
                pos_top="85%",
                range_start=2,
                range_end=100,
            ),
        ],
        yaxis_opts=opts.AxisOpts(
            is_scale=True,
            splitarea_opts=opts.SplitAreaOpts(
                is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
            ),
            name="最高温/最低温℃"
        ),
        #设置标签页
        tooltip_opts=opts.TooltipOpts(
            trigger="axis",
            axis_pointer_type="cross",
            background_color="rgba(245, 245, 245, 0.8)",
            border_width=1,
            border_color="#ccc",
            textstyle_opts=opts.TextStyleOpts(color="#000"),
        ),

        axispointer_opts=opts.AxisPointerOpts(
            is_show=True,
            link=[{"xAxisIndex": "all"}],
            label=opts.LabelOpts(background_color="#777"),
        ),
        brush_opts=opts.BrushOpts(
            x_axis_index="all",
            brush_link="all",
            out_of_brush={"colorAlpha": 0.1},
            brush_type="lineX",
        ),
    )
)
#设置折线图基本参数
line = (
    Line()
    .add_xaxis(xaxis_data=data_x)
    .set_global_opts(
        legend_opts=opts.LegendOpts(
            is_show=False, 
            pos_bottom="5%", 
            # pos_right="30%"
        ),
        xaxis_opts=opts.AxisOpts(type_="category"),
                    yaxis_opts=opts.AxisOpts(
                        grid_index=1,
                        is_scale=True,
                        split_number=2,
                        name="平均温度℃"
                    ),
))

 #设定每个城市的颜色  
def chose_color(city_id):
    if city_id%3==0:
        return "rgba({},{},{},{})".format(0,city_id*6,city_id*5,0.5)
    if city_id%3==1:
        return "rgba({},{},{},{})".format(city_id*6,0,city_id*5,0.5)
    if city_id%3==2:
        return "rgba({},{},{},{})".format(city_id*6,city_id*5,0,0.5)

for city_id in range (1,32):    
   #从数据库导出数据
    curs.execute('''SELECT temperature FROM %s'''%city_name[city_id])
    temperature_list=curs.fetchall()

    data_y=[]
    data_average_y=[]

    
    for i in range(0,days*12):
        a,b=temperature_list[i][0].split('/')
        high_t=eval(a[:len(a)-2])
        low_t=eval(b[:len(b)-1])
        #设置纵坐标
        data_y.append([low_t,high_t,low_t,high_t])
        data_average_y.append((high_t+low_t)/2)

    kline.add_yaxis(
        is_selected=(False if city_id%13 else True),
                series_name=city_name[city_id],
                y_axis=data_y,
                itemstyle_opts=opts.ItemStyleOpts(color=chose_color(city_id),border_color=chose_color(city_id)),
            )
    line.add_yaxis(
        is_selected=(False if city_id%13 else True),
        series_name="%s"%(city_name[city_id]),
        y_axis=data_average_y,
        is_smooth=True,
        is_hover_animation=False,
        linestyle_opts=opts.LineStyleOpts(width=3, opacity=0.5),
        label_opts=opts.LabelOpts(is_show=False),
        itemstyle_opts=opts.ItemStyleOpts(color=chose_color(city_id),border_color=chose_color(city_id)),
            
    )
curs.close()

#折线图和柱状图做成并行图
grid_chart = Grid(
    init_opts=opts.InitOpts(
        width="1500px",
        height="800px",
        animation_opts=opts.AnimationOpts(animation=True),
        page_title="温度柱状图/折线图",
    ),
    
)

grid_chart.add(
    kline,
    grid_opts=opts.GridOpts(pos_left="10%", pos_right="8%", pos_top="10%",height="45%"),
)
grid_chart.add(
    
    line,
    grid_opts=opts.GridOpts(
        pos_left="10%", pos_right="8%", pos_top="63%", height="16%"
    ),
)
grid_chart.render("2020年全国温度分析.html")