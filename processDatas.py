import numpy as np
import xlsxwriter
from xml.sax.handler import feature_external_ges

file = open('pgsm3.txt', 'r')
workbook = xlsxwriter.Workbook('pgsm3.xlsx')
worksheet = workbook.add_worksheet()

datas = file.readlines()

tuple_data = []

for i, line in enumerate(datas):
    isEmpity = len(line.split('#'))
    label_class_type = line.split('#')[0]
    
    if(isEmpity != 1 and label_class_type != 'null2'):
        
        label_class = int(line.split('#')[0])
       
        signal_numbers = line.split('#')[1]
        signal_numbers = list(map(float,signal_numbers.replace('\n', '').replace('\t', ' ').split(' ')[1:]))
        
        standardDeviation_column = np.std(signal_numbers)
        maximum_column = max(signal_numbers)
        minimum_column =  min(signal_numbers)
        range_column = maximum_column - minimum_column
        tuple_data.append((label_class, [standardDeviation_column,maximum_column,minimum_column, range_column]))
 
print(len(tuple_data))


count_indoor = 0
count_outdoor = 0

indoor_datas = []
outdoor_datas = []

for i, (label, datas) in enumerate(tuple_data):
    print(label)
    if(label == 1):
        indoor_datas.append((label, datas))
        count_indoor = count_indoor + 1


      
for i, (label, datas) in enumerate(tuple_data):   
    if(label == 2):
        outdoor_datas.append((label, datas))
        count_outdoor = count_outdoor + 1    

final_GSM_datas = indoor_datas[:680] + outdoor_datas[:680]
print(count_indoor, count_outdoor)
print(indoor_datas, outdoor_datas)
print(len(final_GSM_datas))

for i, (label, features) in enumerate(final_GSM_datas):
    
    worksheet.write(i, 0, label)
    worksheet.write(i, 1, features[0])
    worksheet.write(i, 2, features[1])
    worksheet.write(i, 3, features[2])
    worksheet.write(i, 4, features[3])

workbook.close()
