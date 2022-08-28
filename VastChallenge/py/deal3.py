import pandas as pd
import numpy as np
import json
reader=pd.read_csv("resumes.csv",encoding='utf-8')
reader=pd.DataFrame(reader)
# dicts={}
# del reader['Name']
resume_data=[]
for index,line in reader.iterrows():
    # line['']
    # print(line)
    flag={}
    person=[]
    for a in line.items() :
        
        if a[0]=='Name':
            name='.'.join(a[1].split(' '))
            continue
        
        if pd.isna(a[1]): #np.isnan(a[1]):
            person.append(0)
            continue
        
        for workplace in a[1].split('|')[-1:]:
            workplace=workplace.strip()
            if workplace=='Armed Forces of Kronos' or workplace=='Armed Forces - Kronos' or workplace=='Kronos Military':
                person.append(1)
            elif workplace=='GASTech - Kronos' or workplace=='GASTech – Kronos':
                person.append(2)
            elif workplace=='Tethan Defense Forces' or workplace=='Tethys Defense Force Army' or workplace=='Tethan Defense Force' or workplace=='Tethys Defense Force':
                person.append(3)
            elif workplace=='Myxllink, Ltd.,  Tethys' or workplace=='G&A Engineering, Ltd.' or workplace=='Industrial Resources, Ltd., Tethys' or workplace=='Dalekanium Engineering, Ltd., Tethys':
                person.append(4)
            elif workplace=='Abila Community College, Kronos' or workplace=='Abila Community College':
                print(name)
                person.append(5)
            else:
                person.append(0)
    resume_data.append({'name':name,'type': 'line','data':person})
jsFile = open("resume_data.json", "w+", encoding='utf-8')
jsFile.write(json.dumps(resume_data,indent=4, separators=(',', ': ')))
jsFile.close()

# writer=open('test.txt','w',encoding='utf-8')
# for a in dicts.keys():
#     # print(a)
#     # if dicts[a]>1:
#     writer.write(a+str(dicts[a])+'\n')
