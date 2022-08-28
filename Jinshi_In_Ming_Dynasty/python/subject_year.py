import xlrd
import json


def read_xlsx_file(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_index(0)
    rows = table.nrows
    year_list=[1371, 1451, 1454, 1457, 1460, 1464, 1466, 1469, 1472, 1475, 1478, 1400, 1481, 1487, 1490, 1493, 1496, 1502, 1505, 1511, 1517, 1521, 1412, 1529, 1532, 1535, 1538, 1541, 1544, 1547, 1550, 1553, 1556, 1430, 1559, 1562, 1565, 1568, 1571, 1574, 1577, 1580, 1583, 1586, 1433, 1592, 1610, 1439, 1442, 1445, 1448]
    data = []
    others=[]
    ming_dict={}
    title = table.row_values(0, start_colx=1, end_colx=12)
    for i in range(1, rows):
        values = table.row_values(i, start_colx=1, end_colx=12)
        huji=values[10].strip()
        if len(huji)<2 or huji[0]=='□':
            continue
        if huji[0]=='書':
            huji="書經"
        if huji[0]=='春':
            huji="春秋"
        if huji[0]=='詩':
            huji="詩經"
        if huji[0]=='禮':
            huji="禮記"
        if huji[0]=='易':
            huji="易經"
        
        # huji=huji[0]+huji[-1]

        if huji not in ming_dict:
            ming_dict[huji]={}
       
        if int(values[2]) not in ming_dict[huji]:
            ming_dict[huji][int(values[2])]=0;
        ming_dict[huji][int(values[2])]+=1;
        
    for huji,year_dict in zip(ming_dict.keys(),ming_dict.values()):
        huji_data=[]
        num=0
        for year in year_list:
            if year not in year_dict:
                huji_data.append([str(year),0])
            else:
                huji_data.append([str(year),year_dict[year]])
                num+=year_dict[year]
        if num>100:
            # print(huji)
            # huji_dict={"type": "line",        
            # "connectNulls": False,
            # "symbolSize": 4,
            # "showSymbol": True,
            # "smooth": False,
            # "clip": True,
            # "step": False,
            # "stack": 0,
            # "hoverAnimation": True,
            # "label": {
            #     "show": False,
            #     "position": "top",
            #     "margin": 8
            # },
            # "lineStyle": {
            #     "show": True,
            #     "width": 1,
            #     "opacity": 1,
            #     "curveness": 0,
            #     "type": "solid"
            # },
            # "areaStyle": {
            #     "opacity": 0
            # },
            # "zlevel": 0,
            # "z": 0
            # }
            huji_dict={"type": "bar",
                    "legendHoverLink": True,
                    "showBackground": False,
                    "stack": "stack1",
                    "barMinHeight": 0,
                    "barCategoryGap": "10%",
                    "barGap": "10%",
                    "large": False,
                    "largeThreshold": 400,
                    "seriesLayoutBy": "column",
                    "datasetIndex": 0,
                    "clip": True,
                    "zlevel": 0,
                    "z": 2,
                    "rippleEffect": {
                        "show": True,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }}
            huji_dict["name"]=huji
            huji_dict["data"]=huji_data
            data.append(huji_dict)
                        
    return data

if __name__ == '__main__':
    file_name = "ming_jinshilu_52y_release.xlsx"
    data = read_xlsx_file(file_name)
    # data = {"name":"mingjinshi", "children": data}
    js = json.dumps(data,sort_keys=False,ensure_ascii=False,indent=4, separators=(',', ': '))
    jsFile = open("subject_year_data.json", "w+", encoding='utf-8')
    jsFile.write("var subject_year_data=")
    jsFile.write(js)
    jsFile.close()