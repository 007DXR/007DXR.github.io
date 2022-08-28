from importlib.resources import path
import os
import json

path = './data_.json'
with open(path, 'r' ,encoding='utf-8') as f:
    data = json.load(f)
save_path = './data_save.json'

count_year_list = []
year_dict = {}
for item in data:
    year = item['Year']
    if not year in year_dict.keys():
        year_dict[year] = len(year_dict.keys())
        year_info = {}
        year_info['Year'] = year
        year_info['Count'] =  {}
        count_year_list.append(year_info)
    id = year_dict[year]
    this_year = count_year_list[id]['Count']
    words = item['Count']
    for key in words.keys():
        if key in this_year.keys():
            this_year[key]+=words[key]
        else:
            this_year[key] =words[key]
    
with open(save_path, 'w', encoding='utf-8') as f:
    json.dump(count_year_list, f, ensure_ascii=False)