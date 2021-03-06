#!/usr/bin/env python3 
# #File: chaos.py

import csv
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#print(os.getcwd())

cwd_filename = '108061119.csv'
data = []
header = []
with open(cwd_filename) as csvfile:
    mycsv = csv.DictReader(csvfile)
    header = mycsv.fieldnames
    for row in mycsv:
        data.append(row)

# Remove the data whose value of the PRES (pressure) column is '-99.000' or '-999.000'.
rm_list = []
for i in data:
    if i['PRES'] == '-99.000' or i['PRES'] == '-999.00':
        rm_list.append(i)

for i in rm_list:
    data.remove(i)

# Find out the mean of the PRES value from C0A880, C0F9A0, C0G640, C0R190, C0X260.

target_ids = ['C0A880', 'C0F9A0', 'C0G640', 'C0R190', 'C0X260']
target_contents = []
for i in data:
    if i['station_id'] in target_ids:
        target_contents.append(i)

num_list = [0, 0, 0, 0, 0]
ave_list = [0.0, 0.0, 0.0, 0.0, 0.0]
for i in target_contents[:10]:
    ave_list[target_ids.index(i['station_id'])] += float(i['PRES'])
    num_list[target_ids.index(i['station_id'])] += 1

for i in range(len(ave_list)):
    ave_list[i] = ave_list[i] / num_list[i]

target_data = []
for i in range(len(ave_list)):
    if ave_list[i]] > 0:
        target_data.append([target_ids[i],ave_list[i]])
    else
        target_data.append([target_ids[i], 'None')

print(target_data)

        