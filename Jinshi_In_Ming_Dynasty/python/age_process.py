import xlrd
import json


def read_xlsx_file(filename):
    data = xlrd.open_workbook(filename)
    table = data.sheet_by_index(0)
    rows = table.nrows
    data = []

    subject_dict={}
    
    for i in range(1, rows):
        values = table.row_values(i, start_colx=1, end_colx=20)
        if values[13]=='':
            continue
        subject=values[10].strip()
        if len(subject)<2 or subject[0]=='□':
            continue
        subject=subject[0]+subject[-1]
        
        age=int(values[13])
        if subject not in subject_dict:
            subject_dict[subject]={}
       
        if age not in subject_dict[subject]:
            subject_dict[subject][age]=0;
        subject_dict[subject][age]+=1;
        
    for subject,subject_dict in zip(subject_dict.keys(),subject_dict.values()):
        subject_data=[]

        for age in range(13,68):
            if age not in subject_dict:
                
                subject_data.append(({"value":0}))
            else:
                subject_data.append(({"value":subject_dict[age]}))
        series_dict={"type": "bar",
                    "legendHoverLink": True,
                    "showBackground": False,
                    "stack": "stack1",
                    "barMinHeight": 0,
                    "barCategoryGap": "50%",
                    "barGap": "30%",
                    "large": False,
                    "largeThreshold": 400,
                    "seriesLayoutBy": "column",
                    "datasetIndex": 0,
                    "clip": True,
                    "zlevel": 0,
                    "z": 2,
                    # "label": {
                    #     "show": True,
                    #     "position": "right",
                    #     "margin": 8,
                    #     "formatter": x.data.value
                    #         # function(x){return str(x.data.value)+"人";}
                    # },
                    "rippleEffect": {
                        "show": True,
                        "brushType": "stroke",
                        "scale": 2.5,
                        "period": 4
                    }}
        series_dict["data"]=subject_data
        series_dict['name']=subject
        data.append(series_dict)
                        
    return data

if __name__ == '__main__':
    file_name = "ming_jinshilu_52y_release.xlsx"
    data = read_xlsx_file(file_name)
    # data = {"name":"mingjinshi", "children": data}
    js = json.dumps(data,sort_keys=False,ensure_ascii=False,indent=4, separators=(',', ': '))
    jsFile = open("subject_age.json", "w+", encoding='utf-8')
    jsFile.write(js)
    jsFile.close()