from enum import Flag
import json
path="map_simplified.json"
xian="data.json"
reader=open(path,"r+",encoding="utf-8")
jsonData=json.load(reader)
reader.close()
reader=open(xian,"r+",encoding="utf-8")
cbdbData=json.load(reader)
cnt=0
for i in jsonData['features']:
    print(i['properties']['NAME_FT'])
    name=i['properties']['NAME_FT']
    name2=i['properties']['NAME_CH']
    i['people']=[]
    if len(name)>2:
       name=name.strip()[:-1]
       name2=name2.strip()[:-1]
    flag=0
    for j in cbdbData:
        if j['司']==name or j['府']==name or j['县']==name\
        or j['司']==name2 or j['府']==name2 or j['县']==name2:
            i['people'].append(j)
            # break
    print(len(i['people']))
#     if flag==0:
#         print(name,"error")
#     cnt+=flag
# print("succes",cnt)
# js = json.dumps(jsonData,sort_keys=False,ensure_ascii=False,indent=4, separators=(',', ': '))
js = json.dumps(jsonData, separators=(',', ': '))
jsFile = open("map_people.json", "w+", encoding='utf-8')
jsFile.write(js)
jsFile.close()