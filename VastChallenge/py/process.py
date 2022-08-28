from unittest import result
import xlrd
import xlwt
import pandas as pd
import os 
import json

path = './formatting.xls'
data = xlrd.open_workbook(path)
table = data.sheets()[0]
nrows = table.nrows
# print(table.row_values(0))
# print(table.row(2))
# # print(table.row_values(2))

result = []

kinds = ['ID', 'Year', 'Month', 'Day', 'Time', 'Media', 'Author', 'Title', 'Date', 'Content']

for i in range(1, nrows):
    line = table.row_values(i)
    item_dict = {}
    for j in range(5):
        item_dict[kinds[j]] = str(int(line[j]))
    for j in range(5, 9):
        item_dict[kinds[j]] = line[j]
    sentence = ''
    length = len(line)
    for j in range(9, length):
        if line[j] =='':
            break
        sentence+=line[j]
    item_dict['Content'] = sentence
    result.append(item_dict)

table = data.sheets()[1]
nrows = table.nrows

for i in range(1, nrows):
    line = table.row_values(i)
    item_dict = {}
    for j in range(4):
        item_dict[kinds[j]] = str(int(line[j]))
    for j in range(4, 9):
        item_dict[kinds[j]] = line[j]
    sentence = ''
    length = len(line)
    for j in range(9, length):
        if line[j] =='':
            break
        sentence+=line[j]
    item_dict['Content'] = sentence
    result.append(item_dict)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False)