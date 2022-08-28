import xlrd
import json


def read_xlsx_file(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_index(0)
    rows = table.nrows
    year_list=[1371, 1451, 1454, 1457, 1460, 1464, 1466, 1469, 1472, 1475, 1478, 1400, 1481, 1487, 1490, 1493, 1496, 1502, 1505, 1511, 1517, 1521, 1412, 1529, 1532, 1535, 1538, 1541, 1544, 1547, 1550, 1553, 1556, 1430, 1559, 1562, 1565, 1568, 1571, 1574, 1577, 1580, 1583, 1586, 1433, 1592, 1610, 1439, 1442, 1445, 1448]
    data = []
    ming_dict={}
    title = table.row_values(0, start_colx=1, end_colx=12)
    for i in range(1, rows):
        values = table.row_values(i, start_colx=1, end_colx=12)
        if values[9] not in ming_dict:
            ming_dict[values[9]]={}
        if int(values[2]) not in sets:
            sets.append(int(values[2]))
        if int(values[2]) not in ming_dict[values[9]]:
            ming_dict[values[9]][int(values[2])]=0;
        ming_dict[values[9]][int(values[2])]+=1;
        
    for huji,year_dict in zip(ming_dict.keys(),ming_dict.values()):
        huji_data=[]
        for year,poeple in zip(year_dict.keys(),year_dict.values()):
            huji_data.append(["'"+str(year)+"'",poeple])
        data.append(({huji:huji_data}))
    print(sets)
    return data

if __name__ == '__main__':
    file_name = "ming_jinshilu_52y_release.xlsx"
    data = read_xlsx_file(file_name)
    # data = {"name":"mingjinshi", "children": data}
    js = json.dumps(data,sort_keys=False,ensure_ascii=False,indent=4, separators=(',', ': '))
    jsFile = open("huji2.json", "w+", encoding='utf-8')
    jsFile.write(js)
    jsFile.close()