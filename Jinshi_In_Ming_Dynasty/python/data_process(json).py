import xlrd
import json

def subject_process(x):
    subject={"書經","春秋","詩經","禮記","易經"}
    if len(x)<2 :
        return '其他'
    for i in subject:
        if x[0]==i[0]:
            return i
    return '其他'

def huji_process(huji):
    # huji={'民籍','軍籍','灶籍','官籍','匠籍'}
    if huji=='儒籍' or huji=='醫籍':
        huji='民籍'
    if huji=='竈籍' or huji=='鹽籍':
        huji='灶籍'
    if huji=='旗籍' or huji=='衛籍':
        huji='軍籍'
    if len(huji)<2 :
        return '其他'
    for i in {'民籍','軍籍','灶籍','官籍','匠籍'}:
        if huji[0]==i[0]:
            return i
    return '其他'

def read_xlsx_file(filename):
    # jsFile = open("ming_data.json", "w+", encoding='utf-8')
    # jsFile.write("var data=[")
    
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_index(0)
    rows = table.nrows
    title=table.row_values(0, start_colx=1, end_colx=20)
    data = []
    for i in range(1, rows):
        values = table.row_values(i, start_colx=1, end_colx=20)
        subject=subject_process(values[10].strip())
        huji =huji_process(values[9].strip()[-2:])
        data.append(({
            
            title[1]: values[1],
            # //進士年份
            title[2]: int(values[2]),
            title[3]: values[3],
           
            title[6]: values[6],
            title[7]: values[7],
            title[8]: values[8], 
            title[9]: huji,
            title[10]: subject, 
            # age?
            title[13]:values[13],
            }))
    return data  
      
                        
    

if __name__ == '__main__':
    file_name = "ming_jinshilu_52y_release.xlsx"
    data = read_xlsx_file(file_name)
    js = json.dumps(data,sort_keys=False,ensure_ascii=False,indent=4, separators=(',', ': '))
    jsFile = open("ming_data.json", "w+", encoding='utf-8')
    jsFile.write("var data=")
    jsFile.write(js)
    jsFile.close()
  