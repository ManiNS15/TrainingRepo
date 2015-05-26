__author__ = 'Manitra.Rakotozafy'
import csv

from src import functions


reader = csv.DictReader(open('../data/congress-clean.csv'))

sampleBase = []
for row in reader:
    sampleBase.append(row)

attributes = functions.collect_all_attribute(sampleBase)
'''attributes_value = functions.all_attributes_value_except_t_att(sampleBase,"party")
target_attributes = functions.regroup_by_t_att_value(sampleBase,"party")'''
target_attributes_repartition_count = functions.regroup_by_t_att_value_and_count(sampleBase,"party")
t_att="party"


attributes_value = functions.all_attributes_value_except_t_att(sampleBase,t_att)
t_att_r = {}
for item in sampleBase:
    for att in item:
        if (att == t_att and not(t_att_r.__contains__(item[att]))):
            t_att_r[item[att]] = {}
for key in t_att_r:
    for att in attributes_value:
        t_att_r[key][att] =  attributes_value[att]
i=-1
for row in sampleBase:
    i+=1
    for att in row:
        if att != t_att:
            t_att_r[row[t_att]][att][sampleBase[i][att]] += 1

print t_att_r