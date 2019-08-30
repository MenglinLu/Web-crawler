# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:09:29 2019

@author: Jolin
"""

import urllib
import json
import pandas as pd
##疾病
url='http://zstp.pcl.ac.cn:8002/load_tree/%E7%96%BE%E7%97%85'
response=urllib.request.urlopen(url)
rrr=response.read()
json_rrr=json.loads(rrr)

cat_dict={2:'百种常见病',3:'儿科常见病',4:'其他常见病',5:'其他病'}
res_i=[]
for iii in range(2,6):
    a=[j['id'] for j in [i for i in json_rrr['nodes'] if i['pId']==iii]]
    b=[i for i in json_rrr['nodes'] if i['pId'] in a]
    for ii in b:
        res_i.append([ii['name'],cat_dict[iii]])
pd_res=pd.DataFrame(res_i,columns=['name','class'])
pd_res.to_csv(r'E:\crawl_graph\disease.csv',encoding='utf-8-sig',index=False)

##药物
url='http://zstp.pcl.ac.cn:8002/load_tree/%E8%8D%AF%E7%89%A9'
response=urllib.request.urlopen(url)
rrr=response.read()
json_rrr=json.loads(rrr)
cat_dict={2:'中成药',3:'中草药',4:'西药'}
res_i=[]
for iii in range(2,5):
    a=[j['id'] for j in [i for i in json_rrr['nodes'] if i['pId']==iii]]
    b=[i for i in json_rrr['nodes'] if i['pId'] in a]
    for ii in b:
        res_i.append([ii['name'],cat_dict[iii]])
pd_res=pd.DataFrame(res_i,columns=['name','class'])
pd_res.to_csv(r'E:\crawl_graph\drug.csv',encoding='utf-8-sig',index=False)

##症状
url='http://zstp.pcl.ac.cn:8002/load_tree/%E7%97%87%E7%8A%B6'
response=urllib.request.urlopen(url)
rrr=response.read()
json_rrr=json.loads(rrr)
res_i=[]
a=[j['id'] for j in [i for i in json_rrr['nodes'] if i['pId']==1]]
b=[i for i in json_rrr['nodes'] if i['pId'] in a]
for ii in b:
    res_i.append([ii['name'],'症状'])
pd_res=pd.DataFrame(res_i,columns=['name','class'])
pd_res.to_csv(r'E:\crawl_graph\symptom.csv',encoding='utf-8-sig',index=False)

##治疗
url='http://zstp.pcl.ac.cn:8002/load_tree/%E8%AF%8A%E7%96%97'
response=urllib.request.urlopen(url)
rrr=response.read()
json_rrr=json.loads(rrr)
res_i=[]
a=[j['id'] for j in [i for i in json_rrr['nodes'] if i['pId']==1]]
b=[i for i in json_rrr['nodes'] if i['pId'] in a]
for ii in b:
    res_i.append([ii['name'],'检查诊疗技术'])
pd_res=pd.DataFrame(res_i,columns=['name','class'])
pd_res.to_csv(r'E:\crawl_graph\treat.csv',encoding='utf-8-sig',index=False)